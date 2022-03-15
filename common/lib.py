import random
import base64
from PIL import Image
import io
import os

def make_id():
    str = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    id = ""
    for i in range(16):
        id += random.choice(str)
    return id

def make_big_id():
    str = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    id = ""
    for i in range(51):
        if i != 0 and i%10==0:
            id += "-"
        id += random.choice(str)
    return id

def convert_img_to_b64(img):
    with open(img, "rb") as img_file:
        str_64 = base64.b64encode(img_file.read())
    return "data:image/jpeg;base64," +  str(str_64)[2:-1]

def convert_arr_b64_to_image(b64, post_id, index):
    handle_image = str(b64).split('base64,')[1]

    base = base64.b64decode(handle_image)
    img = Image.open(io.BytesIO(base))


    if os.path.exists(f'./common/images/posts/{post_id}') == False:
        os.makedirs(f'./common/images/posts/{post_id}')
    img = img.convert('RGB')
    img.save(f"./common/images/posts/{post_id}/{index}.jpg")
    return f"./common/images/posts/{post_id}/{index}.jpg"