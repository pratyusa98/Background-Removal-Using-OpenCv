import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()

# imgBG = cv2.imread("images/1.jpg") #for Single Image

#for multiple img
listImg = os.listdir("images")
print(listImg)
imgList = []

for imgpath in listImg:
    img = cv2.imread(f'images/{imgpath}')
    imgList.append(img)

indexImg = 0

while True:
    success,img = cap.read()
    # imgOut = segmentor.removeBG(img, imgBG, threshold=0.8) #for single img
    imgOut = segmentor.removeBG(img,imgList[indexImg],threshold=0.8) #for Multi Image

    imgstack = cvzone.stackImages([img,imgOut],2,1)
    cv2.imshow("image",imgstack)

    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break