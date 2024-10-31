from PIL import Image

#THIS IS LOW QUALITY, USE AN ONLINE PLATOFRM TO MAKE THIS BETTER

coverPageID = 1
startID = 2
endID = 257

imList = []
cover = Image.open("1.png")
for i in range (startID, endID+1):

    imList.append(Image.open(f"{i}.png").convert("RGB"))


cover.save('Textbook.pdf',save_all=True, append_images=imList)
