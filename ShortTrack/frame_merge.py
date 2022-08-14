from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx


def frame_merge(video,total_score):
    print(total_score)
    total_score[5]=5
    total_score[20]=6
    #스코어 가장 큰거 찾기
    for i in range(0,len(total_score)):
        if (i==0):
            score_frame=i
        if(total_score[i]>total_score[i-1]):
            score_frame=i

    highlight = VideoFileClip(video).subclip(score_frame-2,score_frame+2)

    combined = concatenate_videoclips([highlight])
    combined.write_videofile("./ShortTrack/output.mp4")
