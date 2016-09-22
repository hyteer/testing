from PIL import Image

im = Image.open("F:/Pics/male.jpg")

#im.save("F:/Pics/test4_converted_by_pil.jpg")
size = (120,120)
#im.thumbnail(size)
#im.save("F:/Pics/male_120.jpg","JPEG")
im.save("F:/Pics/male_strans.png","PNG")
#im.show()

