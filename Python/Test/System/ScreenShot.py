import wx
from datetime import datetime
now = datetime.now()
strnow = now.strftime("%Y%m%d_%H%M%S_") + str(now.microsecond)

app = wx.App()  # Need to create an App instance before doing anything
screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.EmptyBitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem  # Release bitmap
bmp.SaveFile('D:\\Temp\\'+strnow+'.png', wx.BITMAP_TYPE_PNG)