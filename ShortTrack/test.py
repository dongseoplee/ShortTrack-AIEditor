import tkinter
from tkinter import filedialog
import os
import shutil
import frame_divide
import frame_merge
import highlight


#tkinter 초기설정들
window=tkinter.Tk()
#UI초기값
window.title("Short Track Highlight Edition")
window.geometry("640x400+500+200")
window.resizable(False, False)
window_cutsin=tkinter.Tk()
window_cutsin.title("Short Track Highlight Edition")
window_cutsin.geometry("640x400+500+200")
window_cutsin.resizable(False, False)
label_cutsin=tkinter.Label(window_cutsin, text="Input CutSin.", width=30, height=3, fg="black", relief="solid")

#문구 설정
label=tkinter.Label(window, text="Please Input the Video.", width=30, height=3, fg="black", relief="solid")
label.pack()

#버튼 클릭시
def opendir():
    root = tkinter.Toplevel()#toplevel은 새창
    root.withdraw()
    #동영상이 있는 폴더 실행
    #폴더가 아닌 파일을 하고 싶은 경우 filedialog.askopenfilename()
    video_path = filedialog.askopenfilename(parent=root,initialdir='./',title='Please select a video')
    #fame_divide로 동영상 파일 넘긴뒤 실행
    count,imagePath = frame_divide.frame_divide(video_path)
    print("Finish divide")
    
    #하이라이트 실행
    total_score=highlight.highlight(count)
    print(total_score)

    #merge실행
    frame_merge.frame_merge(video_path,total_score)

    #폴더 열기
    path_finish="./outputVideo"#결과창
    path = os.path.realpath(path_finish)
    os.startfile(path)

#컷신 버튼 클릭시
def open_cutsin():
	window.destroy()
    #문구 설정
	label_cutsin.pack()
#종료시
def on_closing(n):
	if(n == 1):
		#캐쉬파일 삭제
		if os.path.exists("./__pycache__"):
			shutil.rmtree("./__pycache__")
		window.destroy()
	if(n == 2):
		window_cutsin.destroy()
def open_cutsin_video():
	button_Start.pack()
	button_Cut.pack()
	button_Finish.pack()
	button_Cutsin_close.pack()

#메인 버튼 설정
button = tkinter.Button(window, text="파일 경로", overrelief="solid", width=15, command=opendir, repeatdelay=1000, repeatinterval=100)
button.pack()
button_Cutsin = tkinter.Button(window, text="컷신", overrelief="solid", width=15, command=open_cutsin, repeatdelay=1000, repeatinterval=100)
button_Cutsin.pack()
#컷신 버튼 설정
button_Start = tkinter.Button(window_cutsin, text="Start", overrelief="solid", width=15, command=open_cutsin_video, repeatdelay=1000, repeatinterval=100)
button_Cut = tkinter.Button(window_cutsin, text="Cut", overrelief="solid", width=15, command=open_cutsin_video, repeatdelay=1000, repeatinterval=100)
button_Finish = tkinter.Button(window_cutsin, text="Finish", overrelief="solid", width=15, command=open_cutsin_video, repeatdelay=1000, repeatinterval=100)
button_Cutsin_close = tkinter.Button(window_cutsin, text="Finish", overrelief="solid", width=15, command=on_closing(2), repeatdelay=1000, repeatinterval=100)


		
window.protocol("WM_DELETE_WINDOW", on_closing(1))

window_cutsin.mainloop()
window.mainloop()