import cv2
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import threading

class DetectionView:
    
    stop = False

    def load(self):
        window = Tk()
        window.title('Cheating Detection App')
        frame = Frame(window, padx=28, pady=28, bg='yellow')
        frame.grid(row=0, column=0, padx=20, pady=20)
        
        self.l1 = Label(frame)
        self.l1.grid(row=1, column=0, columns=3, sticky='nesw')

        b1 = Button(frame, text='start', command=self.start_cam, pady = 15)
        b1.grid(row=2, column=0, sticky='nesw', pady = 10)

        b2 = Button(frame, text='stop', command=self.stop_cam, pady=15)
        b2.grid(row=2, column=1, sticky='nesw', pady = 10)

        b3 = Button(frame, text='capture', command=self.captureImage, pady=15)
        b3.grid(row=2, column=2, sticky='nesw', pady = 10)

        self.l2 = Label(frame, text='camera has started', font=('Courier', 30), pady=28)
        self.l2.grid(row=3, column=0, columns=3)

        self.start_cam()
        window.mainloop()

    def start_cam(self):
        self.stop = False
        self.cap = cv2.VideoCapture(0)

        self.cascade = cv2.CascadeClassifier('lib/nose.xml')

        t = threading.Thread(target=self.webcam, args=())
        t.start()

    def webcam(self):
        try:
            # capture each frame (image)
            ret, frame = self.cap.read()
            frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
            self.img = Image.fromarray(frame)

            # change the color to RBG
            colorimg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            #core functionality
            r = self.cascade.detectMultiScale(grayimg, 1.7, 11)
            print(r)

            if(len(r) != 0):
                for (x, y, w, h) in r:
                    cv2.rectangle(colorimg, (x, y), (x+w, y+h),(0, 255, 0), 4)
                    self.l2.config(text='Mask is not used properly')

            else:
                self.l2.config(text='The user covered his face')
            
            # converting the image to tkinter compatible image
            self.img = Image.fromarray(colorimg)
            imgtk = ImageTk.PhotoImage(self.img)
            
            self.l1.configure(image=imgtk)
            self.l1.image=imgtk
            
            if(self.stop == False):
                self.l1.after(10, self.webcam)

            else:
                self.l1.image = None

        except:
            print("there is some error")


    def stop_cam(self):

        self.stop = True

    def captureImage(self):
        image = self.img
        image.save('images/1.jpg')
        messagebox.showinfo('alert', 'image saved')
        

    

