import os
import json
import io
from google.cloud import storage
from google.cloud import speech
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt
import moviepy.editor as mp

# clip = mp.VideoFileClip("./VideoFile/30second.mp4")  #처음 wav파일로 바꿀 mp4파일 것
# clip.audio.write_audiofile("audio.wav")    #저장할 wav파일 이름 설정

# sample_rate, data = wavfile.read('audio.wav') #저장한 wav파일을 읽음
# arr1, arr2 = np.split(data, 2, axis=1)

# time = np.linspace(0, len(data) / sample_rate, len(data))



# times = np.arange(len(data)) / sample_rate
# up_frequency = times[np.argwhere(np.squeeze(arr2) >= 28000)].squeeze() #주파수 28000이상 저장

# for i in range(len(up_frequency)):  #int형으로 변환
#     up_frequency[i] = int(up_frequency[i])

    
# up_frequency = list(set(up_frequency))


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"./google_json/short-stt-359905-6d7af470e878.json"

# client = speech.SpeechClient()

# storage_client = storage.Client()
# buckets = list(storage_client.list_buckets())



# bucket_name = 'short_test'  # 서비스 계정 생성한 bucket 이름 입력
# source_file_name = r'audio.wav'  # GCP에 업로드할 파일 경로
# destination_blob_name = 'audio.wav'  # 업로드할 파일을 GCP에 저장할 때의 이름

# storage_client = storage.Client()
# bucket = storage_client.bucket(bucket_name)
# blob = bucket.blob(destination_blob_name) 

# blob.upload_from_filename(source_file_name)


# word_time = [] #키워드 시간초 저장


# keyword = ["일본", "중국"]

# def transcribe_gcs(gcs_uri):
#     client = speech.SpeechClient()
#     audio = speech.RecognitionAudio(uri=gcs_uri)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         language_code='ko-KR',
#         enable_word_time_offsets=True,
#         audio_channel_count=2)
#     operation = client.long_running_recognize(request={"config": config, "audio": audio})
#     response = operation.result()



#     for result in response.results:
#         alternative = result.alternatives[0]
#         for word_info in alternative.words:
#             word = word_info.word
#             start_time = word_info.start_time.total_seconds()
           

#             if word_info.word in keyword:
#                 word_time.append(start_time)
                


#     return response



# response = transcribe_gcs("gs://short_test/audio.wav") # 구글 안에 있는 STT 파일이라서 바꾸면 안될듯





# print("단어나오는 시간")
# print(word_time)

# print("주파수 28000이상")
# print(up_frequency)
# print("completed")

def STT_detection(video="./VideoFile/30second.mp4",count=35):

    keyword = ["일본", "중국"]# 추출할 키워드들 

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"./google_json/short-stt-359905-6d7af470e878.json"

    client = speech.SpeechClient()

    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())

    clip = mp.VideoFileClip(video)  
    clip.audio.write_audiofile("audio.wav")

    bucket_name = 'short_test'  # 서비스 계정 생성한 bucket 이름 입력
    source_file_name = r'audio.wav'  # GCP에 업로드할 파일 절대경로
    destination_blob_name = 'audio.wav'  # 업로드할 파일을 GCP에 저장할 때의 이름

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name) 

    blob.upload_from_filename(source_file_name)




    

    def transcribe_gcs(gcs_uri):

        word_time=[]
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=gcs_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR',
            enable_word_time_offsets=True,
            audio_channel_count=2)
        operation = client.long_running_recognize(request={"config": config, "audio": audio})
        response = operation.result()



        for result in response.results:
            alternative = result.alternatives[0]
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time.total_seconds()
            

                if word_info.word in keyword:
                    word_time.append(start_time)
                    


        return word_time



    word_time = transcribe_gcs("gs://short_test/audio.wav")

    score=[0 for i in range(count)]
    for i in word_time:
        frame_index = i/1
        score[frame_index] = 1 
    print("STT score",score)    
    return score