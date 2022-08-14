from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx


def frame_merge(video,total_score):
    print(total_score)
    #임시로 만들어 본거
    total_score[5]=5
    total_score[20]=6
    total_score[10]=8
    #하이라이트 갯수
    max_highlight=3
    highlight = []
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


    combined = concatenate_videoclips([highlight[0],highlight[1],highlight[2]])
    combined.write_videofile("./ShortTrack/output.mp4")
