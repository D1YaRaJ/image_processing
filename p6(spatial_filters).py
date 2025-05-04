import cv2  
import numpy as np  
import matplotlib.pyplot as plt  
img=cv2.imread(r'C:\Pictures\rose.jpg',cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("The image file was not found.")
gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
median_blur=cv2.medianBlur(img,5)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)
titles=['Original Image','Gaussian Blur','Median Blur','Laplacian Filter']
images=[img,gaussian_blur,median_blur,laplacian]
plt.figure(figsize=(12,6))
for i in range(4):
    plt.subplot(1,4,i+1)  
    plt.imshow(images[i],cmap="gray")  
    plt.title(titles[i])  
    plt.axis('off') 
plt.tight_layout()  
plt.show() 
