import cv2 #OpenCV fkdlqmfjfl
import os   #파일 디렉토리 라이브러리
import numpy as np

def frame_merge(video,total_score):
    print(total_score)
    total_score[5]=5
    #스코어 가장 큰거 찾기
    for i in range(0,len(total_score)):
        if (i==0):
            score_frame=i
        if(total_score[i]>total_score[i-1]):
            score_frame=i

    cap = cv2.VideoCapture(video)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 또는 cap.get(3)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 또는 cap.get(4)
    fps = cap.get(cv2.CAP_PROP_FPS) # 또는 cap.get(5)
    print('프레임 너비: %d, 프레임 높이: %d, 초당 프레임 수: %d' %(width, height, fps))
    
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 정의
    out = cv2.VideoWriter('otter_out.avi', fourcc, fps, (int(width), int(height))) # VideoWriter 객체 정의

    count=0
    while cap.isOpened(): # cap 정상동작 확인
        ret, frame = cap.read()
        # 프레임이 올바르게 읽히면 ret은 True
        if not ret:
            print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
            break
        if(count==score_frame):
            temp=fps*3
            while (cap.isOpened() and temp>0):
                ret, frame = cap.read()
                # 프레임이 올바르게 읽히면 ret은 True
                if not ret:
                    print("프레임을 수신할 수 없습니다(스트림 끝?). 종료 중 ...")
                    break
                out.write(frame)
                count+=1
                temp-=1
        count+=1
    # 작업 완료 후 해제
    cap.release()
    out.release()
    cv2.destroyAllWindows()
