from PIL import Image, ImageDraw, ImageFont

# 创建一个白色背景图像，大小为(512, 512)
background = Image.new('RGB', (512, 512), color='white')

# 创建一个绘制对象
draw = ImageDraw.Draw(background)

# 设置文本字体和大小
font = ImageFont.truetype('arial.ttf', 128)

# 添加文本
text = 'Hello, world!'
text = 'Water\nMark'
text_width, text_height = draw.textsize(text, font=font)
text_x = (512 - text_width) / 2
text_y = (512 - text_height) / 2
draw.text((text_x, text_y), text, fill='black', font=font)

# 保存为PNG格式的文件
background.save('watermark2.png', 'PNG')