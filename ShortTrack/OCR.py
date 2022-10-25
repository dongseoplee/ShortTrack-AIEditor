#import pytesseract
import cv2
from google.cloud import vision
import io
import os
#구글 vision api 코드
#gram json 경로
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\googleCloudApiJson\shorttrack-ocr-f05377351806.json"

#MAC json 경로
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/leedongseop/googleAPIjson/shorttrack-ocr-c1a61c47c944.json"
client = vision.ImageAnnotatorClient()
#잘려진 frame 이미지 ocr 인식하기
#set, dic, hash, list
#keyword list -> keywords
keywords = ['준준결승', '준결승', '결승',
            '500m', '1000m', '1500m', '3000m', '5000m', '계주',
            '남자', '여자',
            'final lap', 'lap:', 'speed',
            '곽윤기', '최민정',
            '대한민국', '한국']

#set 딕셔너리 중복없고 순서없다.
#순위 리스트 생성
imgKeywordSet = set()

lapTime = []
ranking = []

firstPlace = ""
secondPlace = ""
thirdPlace = ""

speed = ""

for i in range(86, 87):

    #path = '/Users/leedongseop/PycharmProjects/test/imageFile/frame' + str(i) + '.png'r
    path = '/Users/leedongseop/PycharmProjects/test/367.png'

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    content = texts[0].description
    content = content.replace(',','')
    #print(content)
    #content = content.lower() 소문자로 변환을 여기서 할지 밑에서 할지 고민

    #content str 형

    #객체 지향으로 만들기
    #1.  ~ \n
    #2.  ~ \n
    #3.  ~ \n

    splitWords = content.split('\n')
    #print("splitWords: ", splitWords)
    for splitWord in splitWords:
        if splitWord.startswith("1. "):
            firstPlace = splitWord
        if splitWord.startswith("2. "):
            secondPlace = splitWord
        if splitWord.startswith("3. "):
            thirdPlace = splitWord
        if ':' in splitWord:
            lapTime.append(splitWord)
        if 'Speed' in splitWord:
            speed = splitWord



    ranking.append(firstPlace)
    ranking.append(secondPlace)
    ranking.append(thirdPlace)
    #print("first place: {}, second place: {}, thrid place: {}".format(firstPlace, secondPlace, thirdPlace))


    #content를 모두 소문자로 변경 -> 키워드 찾기
    #print("content: \n", content)

    for keyword in keywords:
        if keyword in content:
            #print(keyword, 'is in image')
            imgKeywordSet.add(keyword)


print("ranking: ", ranking)
print()
print("img keyword Set: ", imgKeywordSet)
print()
print("lap time: ", lapTime)
print()
#print("speed: ", speed)

#준결승이 content에 있으면 준결승이라 정확히 인식하지만 결승도 인식을 해버리는 문제 발생






'''

for text in texts:
    content = text.description
    content = content.replace(',','')
    print('\n"{}"'.format(content))
'''


'''
dir_path = 'cutted_images'
file_list = os.listdir(dir_path)
print(file_list)
keyword = "최민정"
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

        #원하는 키워드 입력시
        #ocr결과에 최민정이 있으면 ocr 결과 출력
        if keyword in content:
            print("======================", fileName, "======================")
            print('Texts:')
            print(content)

            ocr_score.ocrScore(fileName)




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