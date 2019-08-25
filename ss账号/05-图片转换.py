from PIL import Image  # 安装pillow 有些小坑 对了我的版本是Pillow==4.3.0
import glob, os


baseurl = "/Users/jack/Downloads/铁血战士"
paths = glob.glob("/Users/jack/Downloads/铁血战士/*/*.png")
for path in paths:
    im = Image.open(path)
    filename = path[0:-3] + 'jpg'
    new_path = os.path.join(baseurl, 'jpg图片/')
    new_file = filename.replace(baseurl, new_path)
    dir_name = os.path.dirname(new_file)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    try:
        if os.path.exists(new_file):
            continue
        im.save(new_file)
        print("图片保存:" + new_file)
    except:
        print('错误图片')
        continue
    
    