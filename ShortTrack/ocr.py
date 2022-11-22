#import pytesseract
import glob

import cv2
from google.cloud import vision
import io
import os
#구글 vision api 코드
#gram json 경로
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\googleCloudApiJson\shorttrack-ocr-f05377351806.json"

#MAC json 경로

def ocr_recognition():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./google_json/shorttrack-ocr-c1a61c47c944.json"
    client = vision.ImageAnnotatorClient()
    #잘려진 frame 이미지 ocr 인식하기
    #set, dic, hash, list
    #keyword list -> keywords
    keywords = ['준준결승', '준결승', '결승', '진출',
                '500m', '1000m', '1500m', '3000m', '5000m', '계주',
                '남자', '여자',
                'final lap', 'lap:', 'speed',
                '곽윤기', '최민정',
                '대한민국', '한국','japan']

    #set 딕셔너리 중복없고 순서없다.
    #순위 리스트 생성
    imgKeywordSet = set()

    lapTime = []
    ranking = []
    scoreList = []
    firstPlace = ""
    secondPlace = ""
    thirdPlace = ""

    speed = ""
    images = sorted(glob.glob('./images/temp/*'), key=os.path.getctime)
    i =0
    for path in images:
        #path = '/Users/leedongseop/PycharmProjects/test/imageFile/frame' + str(i) + '.png'
        #path = '/Users/leedongseop/PycharmProjects/test/367.png'
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        try:
            content = texts[0].description
        except:
            print("OCR 결과가 없습니다.")
            frameScore = 0
            scoreList.append(frameScore)
            continue
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

        # print("ranking: ", ranking)
        # print()
        print("img keyword Set: ", imgKeywordSet)
        print()
        # print("lap time: ", lapTime)
        # print()

        frameScore = len(imgKeywordSet)
        scoreList.append(frameScore)
    print("OCR score",scoreList)
    return scoreList











    #준결승이 content에 있으면 준결승이라 정확히 인식하지만 결승도 인식을 해버리는 문제 발생
