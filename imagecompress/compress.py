#By j1nj1CL qq:1653723974
#pip install pillow (glob2)
from PIL import Image
import io
import os
import glob

def compress_image(input_path, output_path, quality):
    with Image.open(input_path) as img:
        img = img.convert('RGB')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG', quality=quality)
        with open(output_path, 'wb') as f:
            f.write(img_byte_arr.getvalue())

def compress_images_in_folder(input_folder, output_folder, quality):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_formats = ['*.jpg', '*.jpeg', '*.png']
    for image_format in image_formats:
        for input_path in glob.glob(os.path.join(input_folder, image_format)):
            file_name = os.path.splitext(os.path.basename(input_path))[0] + '.jpg'
            output_path = os.path.join(output_folder, file_name)
            compress_image(input_path, output_path, quality)
compress_images_in_folder('input', 'output', 70)
#input为待压缩图片的存放位置，50为压缩比例
