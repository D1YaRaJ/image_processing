import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Pictures\rose.jpg',cv2.IMREAD_GRAYSCALE)
if img is None: 
    raise FileNotFoundError("The image file was not found.")
_,bin_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
kernel=np.ones((3,3),np.uint8)
eroded=cv2.erode(bin_img,kernel)
dilated=cv2.dilate(bin_img,kernel)
opening=cv2.morphologyEx(bin_img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(bin_img,cv2.MORPH_CLOSE,kernel)
titles=['Original Binary','Eroded','Dilated','Opening','Closing']
images=[bin_img,eroded,dilated,opening,closing]
plt.figure(figsize=(15,6))
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
