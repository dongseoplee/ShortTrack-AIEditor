#import pytesseract
import cv2
import matplotlib.pyplot as plt
from google.cloud import vision
import io
import os
import ocr_image_cut

#구글 vision api 코드
#gram json 경로
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\googleCloudApiJson\shorttrack-ocr-f05377351806.json"

#MAC json 경로
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/leedongseop/googleAPIjson/shorttrack-ocr-c1a61c47c944.json"
client = vision.ImageAnnotatorClient()

#잘려진 frame 이미지 ocr 인식하기
#path = './ShortTrack/images/temp/frame17.png'


dir_path = 'cutted_images'
file_list = os.listdir(dir_path)
print(file_list)

i = 0
for fileName in file_list:

    path = 'cutted_images/' + fileName
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations


    for text in texts:
        content = text.description
        #print(content) #단어별로 끊어서 출력

        #ocr결과에 최민정이 있으면 ocr 결과 출력
        if "최민정" in content:
            print("======================", fileName, "======================")
            print('Texts:')
            print(content)

        '''
        content = content.replace(',','') #json 형식 보기 쉽게 하려고 만든 코드
        print(content)
        print('\n"{}"'.format(content)) #json 형식 보기 쉽게 하려고 만든 코드
        '''
#test



''' pytesseract 코드
#개인 tesseract 파일 위치 적어야함
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def ocr_temp():
    i = 0
    for j in range (10):
        frameImg = cv2.imread('./ShortTrack/images/temp/frame' +str(i) + '.png')
        plt.imshow(frameImg)
        plt.show()

        cutImg = frameImg[800:1100, 250:750].copy()  # 세로, 가로
        plt.imshow(cutImg)
        plt.show()

        #ret, thresholdImg = cv2.threshold(cutImg, 127, 255, cv2.THRESH_BINARY_INV)
        grayImg = cv2.cvtColor(cutImg, cv2.COLOR_BGR2GRAY)
        #plt.imshow(thresholdImg)
        #plt.show()

        textSample = pytesseract.image_to_string(cutImg, lang='eng',
                                                 config='-c preserve_interwood_spaces=1 --psm 4')
        print("======", str(i), "======")
        #print(textSample)
        ocr_score.calculateScore(textSample)
        i += 1




def ocr_practice():
    i = 570
    for j in range(10):
        frameImg = cv2.imread(str(i) + '.jpg')
        # plt.imshow(frameImg)
        # plt.show()

        cutImg = frameImg[840:1000, 260:650].copy()  # 세로, 가로
        # plt.imshow(cutImg)
        # plt.show()

        ret, thresholdImg = cv2.threshold(cutImg, 127, 255, cv2.THRESH_BINARY_INV)
        grayImg = cv2.cvtColor(cutImg, cv2.COLOR_BGR2GRAY)
        plt.imshow(thresholdImg)
        plt.show()

        textSample = pytesseract.image_to_string(thresholdImg, lang='eng',
                                                 config='-c preserve_interwood_spaces=1 --psm 4')
        print("======", str(i), "======")
        print(textSample)
        i += 1
'''