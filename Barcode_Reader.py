from pyzbar import pyzbar
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self,master):
        
        tk.Frame.__init__(self,master)
        self.grid(row=0,column=0)
        self.master.resizable(0, 0)
        self.master.title("Cititor Coduri de bare")
        self.w=800
        self.h=400

        self.frame=tk.Frame(self.master)
        self.img=tk.Canvas(self.master, height=400, width=800)
        
        self.select=tk.Button(self.frame,command=self.scan_file,text='Selecteaza o Imagine')
        self.select.grid(row=0,column=0,sticky='w')

        self.answer=tk.Entry(self.frame,bg='white',state='readonly',width=113,readonlybackground='white')
        self.answer.grid(row=0,column=1,sticky='w')

        self.frame.grid(row=0,column=0,sticky='w')
        self.auxi=Image.open('Default.jpg')
        self.aux=ImageTk.PhotoImage(self.auxi)
        self.barcode=self.img.create_image(400,200,image=self.aux,anchor='center')
        self.img.bind("<ButtonPress-1>", self.move_start)
        self.img.bind("<B1-Motion>", self.move_move)
        self.img.bind("<MouseWheel>",self.img_zoomer)
        self.img.configure(scrollregion=(400-int(self.w)/2,200-int(self.h)/2,400+int(self.w)/2,200+int(self.h)/2))
        self.img.grid(row=1,column=0,columnspan=1)

    def scan_file(self):
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("JPEG files", "*.jpg*"), 
                                                       ("PNG files", "*.png*"),
                                                       ("all files", "*.*")))
        try:
            self.auxi=Image.open(filename)
            self.w = self.auxi.size[0]
            self.h = self.auxi.size[1]
            self.img.configure(scrollregion=(400-int(self.w)/2,200-int(self.h)/2,400+int(self.w)/2,200+int(self.h)/2))
            self.aux=ImageTk.PhotoImage(self.auxi)
            self.barcode=self.img.create_image(400,200,image=self.aux,anchor='center')

            self.info = pyzbar.decode(Image.open(filename))
            self.output = ''

            if(len(self.info)==0):
                    self.output = '  Nu s-a detectat nici un cod'
            else:
                for i in range(len(self.info)):
                    self.output+=str('  Info: ')
                    self.output+=str(self.info[i].data)
                    self.output+=str('  Tip_Cod: ')
                    self.output+=str(self.info[i].type)
                    #print(self.info[i])
            self.var=tk.StringVar()
            self.var.set(self.output)
            self.answer.config(textvariable=self.var)
            self.img.xview_moveto(0)
            self.img.yview_moveto(0)
            self.img.configure(cursor='fleur')

        except:
            pass

    def move_start(self, event):
        self.img.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.img.scan_dragto(event.x, event.y, gain=1)
    def img_zoomer(self, event):
        if (event.delta > 0):
            #print( event.x, event.y,event.delta,self.auxi.size)
            self.w*=1.1
            self.h*=1.1
            
        elif (event.delta < 0):
            #print( event.x, event.y,event.delta,self.auxi.size)
            self.w*=0.9
            self.h*=0.9
            
        self.aux=ImageTk.PhotoImage(self.auxi.resize((int(self.w),int(self.h))))
        self.barcode=self.img.create_image(400,200,image=self.aux,anchor='center')
        self.img.configure(scrollregion=(400-int(self.w)/2,200-int(self.h)/2,400+int(self.w)/2,200+int(self.h)/2))
        


def window():
    if __name__=='__main__':
        root=tk.Tk()
        app=App(root)
        app.mainloop()

window();
