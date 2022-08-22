import io
import os
from google.cloud import speech #pip install --upgrade google-cloud-speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/leedongseop/googleAPIjson/shorttrack-ocr-c1a61c47c944.json"

client = speech.SpeechClient()


with io.open('WavFile/sample8sec.wav', "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

#sample_rate_hertz 숫자를 잘 맞춰야함 값마다 출력값이 다르게 나옴
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=42700,
    language_code="ko-KR",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
