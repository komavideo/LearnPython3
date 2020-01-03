# 屏幕抓取
import time
from PIL import ImageGrab

print("Ready!")
time.sleep(2)
print("Go!")

###############################################
# 全屏抓取
# ImageGrab.grab().save(".\out\img_capture.png")

###############################################
# 指定范围抓取
img = ImageGrab.grab(bbox=(100, 10, 200, 200))
img.save(".\out\img_capture_clip.png")

