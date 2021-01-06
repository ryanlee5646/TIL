from tkinter import *
# GUI 구현으로 함수 실행

def printHello() :
    print("Hi")

root = Tk()

w = Label(root, text="Python Test")
b = Button(root, text="Hello Python", command=printHello) # 함수 실행 버튼
c = Button(root, text="Quit", command=root.quit) # 함수 종료 버튼(이미 갖고 있음)

w.pack()
b.pack()
c.pack()

root.mainloop()
