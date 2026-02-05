import qrcode as qr
link=input("Please provide the link: ")
img_name=input("Write the name by which you want to save")
img=qr.make(link)
img.save(f"{img_name}.png")