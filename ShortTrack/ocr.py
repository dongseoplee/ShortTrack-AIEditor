import pytesseract
import cv2
import matplotlib.pyplot as plt
from google.cloud import vision
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\googleCloudApiJson\shorttrack-ocr-f05377351806.json"
client = vision.ImageAnnotatorClient()

path = './ShortTrack/images/temp/frame4.png'
with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    content = text.description
    content = content.replace(',','')
    print(content)
    #print('\n"{}"'.format(content))




#개인 tesseract 파일 위치 적어야함
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
'''
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