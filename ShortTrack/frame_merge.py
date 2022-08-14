from turtle import width
from moviepy.editor import *

def frame_merge(video,total_score):
    #임시로 만들어 본거
    total_score[5]=5
    total_score[20]=6
    total_score[10]=8
    print(total_score)
    #하이라이트 갯수
    max_highlight=3
    highlight = []
    Start = VideoFileClip("./ShortTrack/CutSin/Start.mp4").subclip(0,1)
    Sin=VideoFileClip("./ShortTrack/CutSin/Sin.mp4")
    Finish=VideoFileClip("./ShortTrack/CutSin/Finish.mp4").subclip(0,1)
    #스코어 가장 큰거 찾기
    for j in range(0,max_highlight):        
        for i in range(0,len(total_score)):
            if (i==0):
                score_frame=i
            if(total_score[i]>total_score[i-1]):
                score_frame=i

        highlight.append(VideoFileClip(video).subclip(score_frame-2,score_frame+2))
        for k in range(-2,2):
            total_score[score_frame+k]=0

    output = concatenate_videoclips([Start,highlight[0],Sin,highlight[1],Sin,highlight[2],Finish],method="compose")        
    output.write_videofile("./ShortTrack/outputVideo/output.mp4")