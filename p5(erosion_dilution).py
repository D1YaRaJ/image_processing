import cv2
import numpy as np
import matplotlib.pyplot as plt
#load and preprocess the images
img=cv2.imread(r'C:\Users\Sahyadri\Pictures\Saved Pictures\rose.jpg',cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("the image file was not found")
#convert image to binary using thresholding
_,bin_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#define a 3x3 structuring element
struct_ele=np.ones((3,3),np.uint8)
#perform erosion and dilution
eroded_img=cv2.erode(bin_img,struct_ele)
dilated_img=cv2.dilate(bin_img,struct_ele)
#compute absolute differences
eroded_dif=cv2.absdiff(eroded_img,bin_img)
dilated_dif=cv2.absdiff(dilated_img,bin_img)
#display results
titles=['Original Binary','Eroded','Dilated','Erosion Diff','Dilated Diff']
images=[bin_img,eroded_img,dilated_img,eroded_dif,dilated_dif]

plt.figure(figsize=(16,6))
for i,imgs in enumerate(images):
    plt.subplot(2,3,i+1)    #arranges images in 2 row 3 column layout
    plt.imshow(imgs,cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()