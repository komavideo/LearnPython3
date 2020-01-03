Pillow - 抓取屏幕截图
==============

## 知识点

+ 使用Pillow抓图屏幕截图

## 安装

```bash
$ pip install -U pillow
```

## 实战

```python
# 屏幕抓取
import time
from PIL import ImageGrab

print("Ready!")
time.sleep(2)
print("Go!")

###############################################
# 全屏抓取
ImageGrab.grab().save(".\out\img_capture.png")

###############################################
# 指定范围抓取
# img = ImageGrab.grab(bbox=(100, 10, 200, 200))
# img.save(".\out\img_capture_clip.png")
```

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com