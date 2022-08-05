import cv2 #OpenCV 라이브러리
import os   #파일 디렉토리 라이브러리
import shutil
def frame_divide(videoPath):
    imagePath = './images/'
    file_list = os.listdir(videoPath)

    for file in file_list:
        try:
            #임시로 파일이 있으면 삭제하는거 만든거
            if os.path.exists(imagePath):
                shutil.rmtree(imagePath)
            if not (os.path.isdir(videoPath + file)):
                os.makedirs(os.path.join(imagePath + file))

                cap = cv2.VideoCapture(videoPath + file)

                #이미지 수
                count = 0

                while True:
                    ret, image = cap.read()
                    # 이미지 사이즈 960x540으로 변경
                    # image = cv2.resize(image, (960, 540))

                    if not ret:
                        break
                    
                    if(int(cap.get(1)) % 30 == 0):#30이 1초
                        cv2.imwrite(imagePath + file + "/frame%d.png" % count, image)

                        print('%d.png done' % count)
                        count += 1

                cap.release()
                imagePath = imagePath+file
                cv2.destroyAllWindows()

        except OSError as e:
            if e.errno != e.EEXIST:
                print("Failed to create directory!!!!!")
                raise
    return count,imagePath