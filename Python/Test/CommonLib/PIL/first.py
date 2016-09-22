from PIL import Image

im = Image.open("F:/Pics/test4.png")

#im.save("F:/Pics/test4_converted_by_pil.jpg")
size = (100,100)
help(im.save)

im.thumbnail(size)
im.save("F:/Pics/test4_small2.jpg","JPEG")

#im.show()

