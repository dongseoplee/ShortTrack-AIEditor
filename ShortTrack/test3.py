import os
import json
import io
from google.cloud import storage
from google.cloud import speech
from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt
import moviepy.editor as mp

clip = mp.VideoFileClip("short_cut2.mp4")  
clip.audio.write_audiofile("audio.wav")

sample_rate, data = wavfile.read('audio.wav')
arr1, arr2 = np.split(data, 2, axis=1)

time = np.linspace(0, len(data) / sample_rate, len(data))

plt.figure(figsize=(20, 10))


times = np.arange(len(data)) / sample_rate
up_frequency = times[np.argwhere(np.squeeze(arr2) >= 28000)].squeeze() #주파수 28000이상 저장

for i in range(len(up_frequency)):         #int형으로 변환
    up_frequency[i] = int(up_frequency[i])

    
up_frequency = list(set(up_frequency))


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"./google_json/shorttrack-ocr-c1a61c47c944.json"

client = speech.SpeechClient()

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())



bucket_name = 'short_test'  # 서비스 계정 생성한 bucket 이름 입력
source_file_name = r'C:\Users\박민규\Desktop\python\audio.wav'  # GCP에 업로드할 파일 절대경로
destination_blob_name = 'audio.wav'  # 업로드할 파일을 GCP에 저장할 때의 이름

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name) 

blob.upload_from_filename(source_file_name)


word_time = [] #키워드 시간초 저장

def transcribe_gcs(gcs_uri):
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
        sentence = []
        alternative = result.alternatives[0]
        sentence.append(result.alternatives[0].transcript)
        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time.total_seconds()
           
            val = word_info.word.find("일본")
            
            if val != -1:
                word_time.append(start_time)


    return response


response = transcribe_gcs("gs://short_test/audio.wav")


print("단어나오는 시간")
print(word_time)

print("주파수 28000이상")
print(up_frequency)
print("completed")