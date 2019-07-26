from glob import glob                                                           
import cv2 

"""Mass conversion from png to jpg files. The need for that was for the camera calibration script and the images that usually are taken and saved in .png.
NOTE: Drag this program to where you want to convert your files and then just run it on the terminal! It will take the images locally.""" 


def convert():
    pngs = glob('./*.png')
    for i in pngs:
        img = cv2.imread(i)
        cv2.imwrite(i[:-3] + 'jpg', img)

if __name__ == "__main__":
    convert()
