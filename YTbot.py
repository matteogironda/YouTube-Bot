# Create a pop up window
from tkinter import *
from selenium import webdriver


def window_create():

    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.init_window()
        def init_window(self):
            self.master.title('New video uploaded!')
            self.pack(fill=BOTH, expand=1)

            quitButton = Button(self, text='Cool.', command=self.client_exit)
            quitButton.place(x=200, y=600)

            goToButton = Button(self, text='Go to', command=self.client_goTo)
            goToButton.place(x=600,y=600)

        def client_exit(self):
            exit()

        def client_goTo(self):
            browser = webdriver.Chrome(r"C:\Users\giron\Desktop\Python\chromedriver.exe")
            browser.get('https://www.youtube.com/user/LordPravusGaming')
    root = Tk()
    root.geometry("800x800")
    app = Window(root)
    root.mainloop()

#reload page every minute


upload = True
def main():

    if upload == True:
        window_create()

main()
