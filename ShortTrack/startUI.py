import tkinter
from tkinter import filedialog
import os


window=tkinter.Tk()

window.title("Short Track Highlight Edition")
window.geometry("640x400+500+200")
window.resizable(False, False)


label=tkinter.Label(window, text="Please Input the Video.", width=30, height=3, fg="black", relief="solid")
label.pack()

def opendir():
    root = tkinter.Tk()
    root.withdraw()
    #동영상이 있는 폴더 실행
    dir_path = filedialog.askdirectory(parent=root,initialdir='./',title='Please select a video')
    print("\ndir_path : ", dir_path)
    #fame_divide로 동영상 파일 넘긴뒤 실행
    
    #하이라이트 실행
    
    #merge실행

    #폴더 열기
    path = os.path.realpath(dir_path)
    os.startfile(path)

button = tkinter.Button(window, text="파일 경로", overrelief="solid", width=15, command=opendir, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()