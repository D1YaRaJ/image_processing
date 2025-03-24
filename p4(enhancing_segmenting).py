import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

def enhance_contrast_color(img):
    lab_img=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    l_channel,a_channel,b_channel=cv2.split(lab_img)
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    l_channel=clahe.apply(l_channel)
    enhanced_lab=cv2.merge((l_channel,a_channel,b_channel))
    return cv2.cvtColor(enhanced_lab,cv2.COLOR_LAB2BGR)

def segment_image_color(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    threshold=threshold_otsu(gray_img)
    return(gray_img>threshold).astype(np.uint8)*255

img=cv2.imread(r'C:\Users\Sahyadri\Pictures\Saved Pictures\balloon.jpg')
if img is None:
    raise ValueError("Error:Could not load image.Check the file path")
enhanced_img=enhance_contrast_color(img)
segmented_img=segment_image_color(enhanced_img)
titles=['Original Image','Enhanced Image','Segmented Image']
images=[
    cv2.cvtColor(img,cv2.COLOR_BGR2RGB),
    cv2.cvtColor(enhanced_img,cv2.COLOR_BGR2RGB),
    segmented_img
]

plt.figure(figsize=(15,10))
for i,imgs in enumerate(images):
    plt.subplot(1,3,i+1)
    plt.imshow(imgs if i<2 else imgs,cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
