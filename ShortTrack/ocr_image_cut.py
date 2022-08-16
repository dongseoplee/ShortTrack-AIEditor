import cv2
import matplotlib.pyplot as plt
import os

#frame 이미지들 자르는 코드


dir_path = './ShortTrack/images/temp'
file_list = os.listdir(dir_path) #자르기 전 사진 저장 경로에서 파일 이름들 가져와서 list에 저장

for fileName in file_list:
    cuttedFramePath = 'cutted_images/Cutted_' + fileName #자른 사진 저장 경로 frame0.png -> Cutted_frame0.png
    framePath = './ShortTrack/images/temp/' + fileName #자르기 전 사진 저장 경로

    originImg = cv2.imread(framePath)
    cuttedImg = originImg[700:1100, 0:1920].copy()

    cv2.imwrite(cuttedFramePath, cuttedImg)
