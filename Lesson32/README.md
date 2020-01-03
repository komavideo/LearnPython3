Pillow - 处理图像基础库
================

## 官网

https://github.com/python-pillow/Pillow

## 安装

```bash
$ pip install pillow
$ pip list
```

## 图像基本信息

```python
from PIL import Image

image = Image.open("mylogo.jpg")

# 图片基本信息
print(image.filename)
print(image.format)
print(image.mode)
print(image.size)
print(image.info)

# attributes_list = [attribute for attribute in dir(image) if attribute[0].islower()]
# print(attributes_list)

# 取得某个点的RGB
print(image.getpixel((128, 256)))
```

## 图像变换(convert)

```python
from PIL import Image
 
image = Image.open("mylogo.jpg")

# 1位像素图
image.convert("1").save("img1_pixels.png", quality=100)
# 8位灰度图
image.convert("L").save("imgL_grayscale.png", quality=100)
# 8位彩图
image.convert("P").save("imgP_8_bit_colors.png", quality=100)
```

### 图片模式

https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

## 图像剪切(crop)

```python
from PIL import Image
 
image = Image.open("mylogo.jpg")

# 图片剪切：开始点x1, 开始点y1, 结束点x2, 结束点y2
image.crop((240, 30, 300, 240)).save("img_crop.png")
```

## 图像旋转(rotate)

```python
from PIL import Image
 
image = Image.open("mylogo.jpg")

image.rotate(30).save("img_rotate_30.png")
image.rotate(-30).save("img_rotate_-30.png")
image.rotate(30, Image.NEAREST, True).save("img_rotate_30_expand.png")
```

## 调整大小(resize)

```python
from PIL import Image
 
image = Image.open("mylogo.jpg")

# 指定大小
img_resize = image.resize((200, 200), Image.NEAREST)
img_resize.save("img_resized.jpg")

# 宽高取半
# img_resize = image.resize((int(image.width/2), int(image.height/2)), Image.NEAREST)
# img_resize.save("img_resized.jpg")
```

## 画图写字

```python
from PIL import Image, ImageDraw, ImageFont
 
image = Image.open("mylogo.jpg")

image_draw = ImageDraw.Draw(image)

# 画线
image_draw.line((0, image.height, image.width, 0), fill=(255, 0, 0), width=8)
# 矩形
image_draw.rectangle((100, 100, 200, 200), fill=(0, 255, 0))
# 圆形
image_draw.ellipse((250, 300, 450, 400), fill=(0, 0, 255))
# 写字
image_font = ImageFont.truetype("C:\Windows\Fonts\msyh.ttc", size=48)
image_draw.multiline_text((0, 0), 'Pillow is good!', fill=(255, 255, 0), font = image_font)

image.save("img_edited.png")
```

## 批量文件处理

```python
import os
import glob
from PIL import Image

files = glob.glob('./*.jpg')

for file in files:
    img = Image.open(file)
    # 宽高取半
    img_resize = img.resize((int(img.width/2), int(img.height/2)))
    ftitle, fext = os.path.splitext(file)
    img_resize.save(ftitle + '_half' + fext)
```

## 其他课题

+ 图片合并
+ 图片反转
+ 蒙版切除
+ Gif制作
+ 透明背景
+ 像素计算
+ 人脸识别(OpenCV)
+ 马赛克处理
+ 屏幕拷贝

## 课程文件

https://github.com/komavideo/LearnPython3

## 小马视频频道

http://komavideo.com
