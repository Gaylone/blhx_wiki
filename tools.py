# 一个工具类，包含一些html转换成图片，翻译功能
import os
import imgkit
import cv2
SAVE_PATH=os.path.dirname(__file__)
tool_path=os.path.abspath(os.path.join(os.path.dirname(__file__), 'wkhtmltopdf', 'bin','wkhtmltoimage.exe'))
"""
方法名：print_img
参数列表：无
用处：调用打印工具，打印ship_info.html成图片
返回值：无返回值，从html文件夹里读取html文件，打印的图片输出到images文件夹
"""

def print_img_ship():
    # path_wkimg = SAVE_PATH + '/\\wkhtmltopdf/\\bin/\\wkhtmltoimage.exe'  # 工具路径
    path_wkimg = tool_path
    cfg = imgkit.config(wkhtmltoimage=path_wkimg)
    options = {
    "encoding": "UTF-8",
    "enable-local-file-access": None
    }
    print("开始")
    imgkit.from_file(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ship_html', 'ship_info.html')),
                     os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_temp.png')),
                                     options=options, config=cfg) # 不管怎么样都打印这张图片
    print("结束")

"""
方法名：print_img_skin
参数列表：无
用处：调用打印工具，打印ship_skin.html成图片
返回值：无返回值，从html文件夹里读取html文件，打印的图片输出到images文件夹
"""
def print_img_skin():
    path_wkimg = tool_path  # 工具路径
    cfg = imgkit.config(wkhtmltoimage=path_wkimg)
    options = {
    "encoding": "UTF-8",
    "enable-local-file-access": None
    }
    imgkit.from_file(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ship_html', 'ship_skin.html')),
                     os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_skin_mix', 'ship_skin.png')),
                                     options=options, config=cfg) # 不管怎么样都打印这张图片


def print_img_ship_weapon():
    path_wkimg = tool_path  # 工具路径
    cfg = imgkit.config(wkhtmltoimage=path_wkimg)
    options = {
        "encoding": "UTF-8",
        "enable-local-file-access": None
    }
    imgkit.from_file(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ship_html', 'ship_weapon.html')),
                     os.path.abspath(
                         os.path.join(os.path.dirname(__file__), 'images', 'ship_weapon_temp.png')),
                     options=options, config=cfg)  # 不管怎么样都打印这张图片


"""
方法名：img_process_ship_info
参数列表：无
用处：裁剪图片
返回值：无返回值
"""


def img_process_ship_info():
    # os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_temp.png'))
    img=cv2.imread(os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_temp.png')))
    image=img.shape
    cropped = img[0:image[0],0:620]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_info.png')), cropped)

    """
    方法名：img_process_ship_weapon
    参数列表：无
    用处：裁剪图片
    返回值：无返回值
    """


def img_process_ship_weapon():
    # os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_weapon_temp.png'))
    img = cv2.imread(os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_weapon_temp.png')))
    image = img.shape
    cropped = img[0:image[0], 0:620]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(os.path.abspath(os.path.join(os.path.dirname(__file__), 'images', 'ship_weapon.png')), cropped)




