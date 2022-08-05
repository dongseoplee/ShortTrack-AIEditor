import cv2 #OpenCV fkdlqmfjfl
import os   #파일 디렉토리 라이브러리

def frame_merge(imagePath):
    pathOut = './VideoFile_output/output1.mp4'
    #초당 이미지 수
    fps = 1
    frame_array = []

    #이미지 경로
    file_list = os.listdir(imagePath)
    for file in file_list:
        print(file)
        img = cv2.imread(imagePath+file)
        #height, width, layers = img.shape
        width = 980
        height= 640
        size = (width,height)
        frame_array.append(img)
    
    #이미지 합치기
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

frame_merge("./images/30second.mp4/")