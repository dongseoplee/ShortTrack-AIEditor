import tkinter
from tkinter import filedialog
import os
import shutil
import frame_divide
import frame_merge
import highlight



window=tkinter.Tk()

#UI초기값
window.title("Short Track Highlight Edition")
window.geometry("640x400+500+200")
window.resizable(False, False)

#문구 설정
label=tkinter.Label(window, text="Please Input the Video.", width=30, height=3, fg="black", relief="solid")
label.pack()

#버튼 클릭시
def opendir():
    root = tkinter.Toplevel()#toplevel은 새창
    root.withdraw()
    #동영상이 있는 폴더 실행
    #폴더가 아닌 파일을 하고 싶은 경우 filedialog.askopenfilename()
    dir_path = filedialog.askdirectory(parent=root,initialdir='./',title='Please select a video')
    print("\ndir_path : ", dir_path)
    #fame_divide로 동영상 파일 넘긴뒤 실행
    count,imagePath = frame_divide.frame_divide(dir_path+"/")
    print("Finish divide")
    
    #하이라이트 실행
    highlight.highlight(count)
    print("highlight")

    #merge실행
    frame_merge.frame_merge(imagePath)

    #폴더 열기
    path_finish="./VideoFile_output"#결과창
    path = os.path.realpath(path_finish)
    os.startfile(path)

#버튼 설정
button = tkinter.Button(window, text="파일 경로", overrelief="solid", width=15, command=opendir, repeatdelay=1000, repeatinterval=100)
button.pack()

#종료시
def on_closing():
    #캐쉬파일 삭제
    if os.path.exists("./__pycache__"):
        shutil.rmtree("./__pycache__")
    print("끝")
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()