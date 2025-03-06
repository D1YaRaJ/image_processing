import cv2
import numpy as np

def load_img(path):
    img=cv2.imread(path)
    if img is None:
        print("error:could not load image")
        exit()
    return img

def translation(image, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    (h, w) = image.shape[:2]
    translated_image = cv2.warpAffine(image, M, (w, h))
    return translated_image

def rotation(image, angle, scale=1.0):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def scaling(image, scale_x, scale_y):
    (h, w) = image.shape[:2]
    new_width = int(w * scale_x)
    new_height = int(h * scale_y)
    scaled_image = cv2.resize(image, (new_width, new_height))
    return scaled_image

def main():
    img_path=input("Enter the image path:")
    img=load_img(img_path)
    tx=int(input("Enter translation in x direction:"))
    ty=int(input("Enter translation in y direction:"))
    angle=float(input("Enter rotation angle:"))
    scale_x=float(input("Enter scaling factor for x:"))
    scale_y=float(input("Enter scaling factor for y:"))

    translated=translation(img,tx,ty)
    rotated=rotation(img,angle)
    scaled=scaling(img,scale_x,scale_y)

    cv2.imshow('original image',img)
    cv2.imshow('translated image',translated)
    cv2.imshow('rotated image',rotated)
    cv2.imshow('scaled image',scaled)

    save_option=input("Do you want to save the transformed images?(yes/no):").strip().lower()
    if save_option=="yes":
        cv2.imwrite('translated_img.jpg',translated)
        cv2.imwrite('rotated_img.jpg',rotated)
        cv2.imwrite('scaled_img.jpg',scaled)
        print("images saved successfully!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

