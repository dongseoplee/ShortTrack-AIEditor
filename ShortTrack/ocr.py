import pytesseract
import cv2
import matplotlib.pyplot as plt

#개인 tesseract 파일 위치 적어야함
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

i = 570


for j in range(10):
    #이미지 불러오기
    print("=======", i, ".jpg=======")
    fileName = str(i) + '.jpg'
    original_img = cv2.imread(fileName)
    #original_img = cv2.imread('ocr_sample.jpg')
    #ocr 인식률 높이기 위해 이미지 흑백처리
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    #plt.imshow(gray_img, cmap='gray')
    #plt.imshow(original_img)
    #흑백 이미지 출력
    #plt.show()

    #ocr할 부분 자르기
    # 왼쪽 하단 1, 2, 3 순위
    cut_img_order = original_img[840:1000, 260:650].copy() #세로, 가로
    #자른 사진 출력
    plt.imshow(cut_img_order)
    plt.show()
    #ocr 인식
    textSample = pytesseract.image_to_string(cut_img_order, lang='eng', config='-c preserve_interwood_spaces=1 --psm 4')
    print(textSample)
    i += 1


''''
#cv2.imshow('cut_img_order', cut_img_order)
#plt.show()
#---------

# 남은 바퀴 수, LAP 타임
cut_img_Laps = gray_img[605:635, 150:440].copy() #세로, 가로
plt.imshow(cut_img_Laps)
textSample = pytesseract.image_to_string(cut_img_Laps, lang='eng+kor', config='-c preserve_interwood_spaces=1 --psm 4')
print(textSample)
#cv2.imshow('cut_img_Laps', cut_img_Laps)
#plt.show()


#----

#cv2.imshow('source', im)



text1 = pytesseract.image_to_string('OCR1.jpg', lang='eng', config='-c preserve_interwood_spaces=1 --psm 4')

text2 = pytesseract.image_to_string('OCR2.jpg', lang='eng', config='-c preserve_interwood_spaces=1 --psm 4')

text3 = pytesseract.image_to_string('OCR3.jpg', lang='eng', config='-c preserve_interwood_spaces=1 --psm 4')
'''
