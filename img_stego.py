import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import cv2

window = tkinter.Tk()
window.title("Steganography")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

def upload():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tkinter.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    for f in filename:
        global img
        img=Image.open(f) # read the image file
        img=img.resize((180,180)) # new width & height
        img=ImageTk.PhotoImage(img)
        og_img.configure(image=img)
        og_img.image = img 
        global imagecv
        global test
        imagecv = cv2.imread(f)
        test=imagecv
        imgcv = Image.open(f, 'r')
        print(imagecv.shape)
        print(imagecv)
        msg_label.grid(row=2,column=1)
        msg_entry.grid(row=2,column=2)
        encode_btn.grid(row=3,column=1)
        og_title.grid(row=3,column=0,)
        
def encode():
    data = msg_entry.get()
    data=data+"$$" #'$$'--> secrete key
    print(data)
    if len(data) == 0:
        raise ValueError("Empty data")
    global enc_img
    enc_img = str("newestt.png")
    global enc_data
    enc_data = hidedata(img, data)
   
    cv2.imwrite(enc_img, enc_data)
    print(enc_data.shape)
    a=np.array(test)
    b=np.array(enc_data)
    if np.array_equal(a,b):
        print("TRUE")
    else:
        print("FALSE")

    my_photo2=Image.open(enc_img)
    resized2=my_photo2.resize((180,180),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(resized2)
    global img1
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((180,180),Image.ANTIALIAS)
    img1.save(enc_img)
   
    en_img.configure(image=photo2)  
    en_title.grid(row=7,column=0,pady=2)  
    decode_btn.grid(row=5,column=1)

def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
        print(p)
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p

# hide data in given img

def hidedata(img, data):
    #'$$'--> secrete key
    d_index = 0
    b_data = data2binary(data)
    global len_data
    len_data = len(b_data)
    print("length:",len_data)
    print(data)
    d=int(b_data,2)
    print(d)

 #iterate pixels from image and update pixel values

    for value in imagecv:
        flag=0
        for pix in value:
          
            r, g, b = data2binary(pix)
            
            if d_index < len_data:
                
                
                s=str((r[:-1] + b_data[d_index]))
               
                
                pix[0] = int(s,2)
                
                d_index += 1
                print("index= ",d_index)
            if d_index < len_data:
               
                s1=str((g[:-1] + b_data[d_index]))
               
                
                pix[1] = int(s1,2)
               
                d_index += 1
               
            if d_index < len_data:
               
                s2=str((b[:-1] + b_data[d_index]))
               
                
                pix[2] = int(s2,2)
               
                d_index += 1
           

            if d_index==len_data:
               
                flag=1
                break
        if flag==1:
            break
   
    return imagecv


def find_data(imgs):
    bin_data = "" 
    count=0
    flag=0
    for value in imgs:
        for pix in value:
            r, g, b = data2binary(pix)
           
            bin_data += r[-1]
            count=count+1
          
            bin_data += g[-1]
            count=count+1
          
            bin_data += b[-1]
            count=count+1
           

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
   
    readable_data = ""
    array=[]
    for x in all_bytes:
        dec=int(x, 2)
        array.append(dec)
        string=chr(dec)
        readable_data = readable_data+string

        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]
    


def decode():
    img_name = enc_img
    imagen = cv2.imread(img_name)
    print(imagen)
    img=Image.open(img_name,'r')
    msg = find_data(imagen)
    print(msg)
    string="Hidden text is : "+msg
    msg_label2.grid(row=6,column=1)
    msg_label2.config(text=string)



heading_label = tkinter.Label(
    frame, text="Image Steganography", bg='#333333', fg="#FF3399", font=("Arial", 20))

og_img=tkinter.Label(
    frame,  bg='#333333', fg="#FF3399", font=("Arial", 30))

og_title=tkinter.Label(
    frame, text="Original Image", bg='#333333', fg="#FF3399", font=("Arial", 13))

en_img=tkinter.Label(
    frame, bg='#333333', fg="#FF3399", font=("Arial", 30))

en_title=tkinter.Label(
    frame, text="Image After Encryption", bg='#333333', fg="#FF3399", font=("Arial", 13))
upload_btn=tkinter.Button(
    frame, text="Upload Image", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12),command=upload)
msg_label=tkinter.Label(
    frame, text="Enter message to be hidden", bg='#333333', fg="#FF3399", font=("Arial", 13))

msg_entry = tkinter.Entry(frame, font=("Arial", 13))

encode_btn=tkinter.Button(
    frame, text="Encode", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12),command=encode)

decode_btn=tkinter.Button(
    frame, text="Decode", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12),command=decode)

msg_label2=tkinter.Label(
    frame, text="Hidden message is", bg='#333333', fg="#FF3399", font=("Arial", 13))

# placement
heading_label.grid(row=0,column=1,pady=4,padx=4)
og_img.grid(row=1,column=0,rowspan=2,)
upload_btn.grid(row=1,column=1,)
en_img.grid(row=5,column=0,rowspan=2)
frame.pack()

window.mainloop()
