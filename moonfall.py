import cv2
import os
import time

for filename in os.listdir('D:/'):
    if not os.path.exists('D:/sen'):
        os.makedirs('D:/sen')
imgcapture =cv2.VideoCapture(0)
def sen():
    try:
        for i in range(5):
            ret,frame=imgcapture.read()
            name=int(round(time.time()*1000))
            cv2.imwrite('D:/sen/{}.jpg'.format(name),frame)
        imgcapture.release()
    except:
        print("")
                