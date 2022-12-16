from tkinter import * #import GUI lib
import simple_image_download.simple_image_download as simp

def googleImgDL() :
    given_keyword = keyword.get()
    given_img_no = img_no.get()
    my_downloader.extensions = '.jpg'
    my_downloader.download(given_keyword, limit=given_img_no, verbose=True)

#use GUI module
root = Tk()
root.title("Google Image Downloader")
root.geometry("650x400")

my_downloader = simp.Downloader()

keyword = StringVar()
img_no = IntVar()

# Adding title
title = Label(root, text="Google Image Downloader",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=150, y=10)

#keyword
keyword_entry_label = Label(root, text="Enter a keyword :",
               fg="Blue", font=("Arial", 10, 'bold')).place(x=50, y=200)
keyword_entry = Entry(root,textvariable=keyword,width=30).place(x=220, y=200)

#no images
no_images_entry_label = Label(root, text="Enter number of images :",
               fg="Blue", font=("Arial", 10, 'bold')).place(x=50, y=230)
no_images_entry = Entry(root,textvariable=img_no,width=30).place(x=220, y=230)

btn = Button(master=root, text="download",fg="green", font=("Arial", 10, 'bold')
             ,command=googleImgDL).place(x=280,y=260)

photo = PhotoImage(file = "logo/img_dl.png")
root.iconphoto(False, photo)

root.mainloop()