import customtkinter
import qrcode as qr
import PIL
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("500x350")

def submit():
    url = enrty.get()
    codecolor = enrty1.get()
    backcolor = enrty2.get()
    qrimage = qr.QRCode(version=1,box_size=10,border=4,error_correction=qr.ERROR_CORRECT_H)
    qrimage.add_data(url) # make() is used to make qr code of the url or text message that we write inside the make() function
    qrimage.make(fit=True)
    img = qrimage.make_image(back_color = backcolor, fill_color = codecolor)
    img.save("QR_code.png")
    


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady = 20, padx =60, fill="both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "QR maker")

label.pack(pady = 12,padx = 10)

enrty = customtkinter.CTkEntry(master = frame, placeholder_text = "Enter your URL/Text here")
enrty.pack(pady = 12,padx = 10)

enrty1 = customtkinter.CTkEntry(master = frame, placeholder_text = "Enter color of qr code")
enrty1.pack(pady = 12,padx = 10)

enrty2 = customtkinter.CTkEntry(master = frame, placeholder_text = "Enter color of background of qr code")
enrty2.pack(pady = 12,padx = 10)

button = customtkinter.CTkButton(master=frame,text="Submit", command=submit)
button.pack(pady = 12,padx = 10)

root.mainloop()


