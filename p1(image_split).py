import cv2
import numpy as np 
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\SAHYADRI\Pictures\Saved Pictures\website.jpg')
plt.imshow(img)
cv2.waitKey(0)
newimg=np.asarray(img)
x,y,d=newimg.shape
div1=x//2
div2=y//2
tl=newimg[:div1,:div2]
tr=newimg[:div1,div2:y]
bl=newimg[div1:x,:div2]
br=newimg[div1:x,div2:y]
div_img=[tl,tr,bl,br]
fig,axs=plt.subplots(2,2,figsize=(5,5))
for idx,ax in enumerate(axs.flatten()):
    ax.imshow(div_img[idx])
    ax.set_title(f'Quadrant {idx+1}')
    ax.axis('off')
plt.show()