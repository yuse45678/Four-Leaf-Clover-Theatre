import os
import cv2
from PIL import Image
import time
def image_to_position(screen, template):
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("prob:", max_val)
    if max_val > 0.80:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        return center,max_val
    else:
        return False,max_val

def crop_screenshot(img_file, pos_x, pos_y, width, height, out_file):
    img = Image.open(img_file)
    region = (pos_x, pos_y, pos_x + width, pos_y + height)
    cropImg = img.crop(region)
    cropImg.save(out_file)
    print("exported:", out_file)

def take_screenshot():
    os.system("adb shell screencap -p /data/screenshot.png")
    os.system("adb pull /data/screenshot.png ./tmp.png")
    img=cv2.imread("tmp.png")
    return img

def adb_click(center, offset=(0, 0)):
    (x, y) = center
    x += offset[0]
    y += offset[1]
    os.system(f"adb shell input tap {x} {y}")

def adb_init():
    os.system("adb connect 127.0.0.1:62001")


def juqing(zhuxianjuqing,kaishi,loading,juqinghuifang,redu,next,win,yanchujiesu,xiayiguan,fanhui,xuanze,guanbi):

    img=take_screenshot()
    print("是否在主线剧情？")
    pos,val=image_to_position(img,zhuxianjuqing)
    if(pos and val>0.8):
        adb_click(pos)
        time.sleep(1)
    print("开始表演了吗？")
    img = take_screenshot()
    pos, val = image_to_position(img, kaishi)
    if(pos and val>0.8):
        adb_click(pos)
        time.sleep((0.5))

    img = take_screenshot()
    print("是否在加载画面？")
    tmp = image_to_position(img,loading )
    while (tmp[1] > 0.8):
        time.sleep(2)
        screen = take_screenshot()
        tmp = image_to_position(screen, loading)

    time.sleep(1)
    print("有剧情吗？")
    img = take_screenshot()
    pos, val = image_to_position(img, juqinghuifang)
    while(val>0.8):
        pos1, val1 = image_to_position(img, next)
        adb_click(pos1)
        time.sleep(0.6)
        pos_xz,val_xz=image_to_position(img,xuanze)
        if pos_xz and val_xz>0.8:
            adb_click(pos_xz)
        img = take_screenshot()
        pos, val = image_to_position(img, juqinghuifang)

    img = take_screenshot()
    print("是否在加载画面？")
    tmp = image_to_position(img, loading)
    while (tmp[1] > 0.8):
        time.sleep(2)
        screen = take_screenshot()
        tmp = image_to_position(screen, loading)

    print("战斗了吗？")
    img = take_screenshot()
    pos_r, val = image_to_position(img, redu)
    if(val>0.8):
        time.sleep(2)
        img = take_screenshot()
        print("战斗胜利了吗？")
        pos_win, val_w = image_to_position(img,win)
        while(val_w<0.8):
            img = take_screenshot()
            pos_win, val_w = image_to_position(img, win)
            time.sleep(1)
        adb_click((900, 450))
    time.sleep(1)

    img = take_screenshot()
    print("是否在加载画面？")
    tmp = image_to_position(img, loading)
    while (tmp[1] > 0.8):
        time.sleep(2)
        screen = take_screenshot()
        tmp = image_to_position(screen, loading)

    print("有剧情吗？")
    img = take_screenshot()
    pos, val = image_to_position(img, juqinghuifang)
    while(val>0.8):
        pos1, val1 = image_to_position(img, next)
        adb_click(pos1)
        time.sleep(0.6)
        pos_xz,val_xz=image_to_position(img,xuanze)
        if pos_xz and val_xz>0.8:
            adb_click(pos_xz)
        img = take_screenshot()
        pos, val = image_to_position(img, juqinghuifang)
    time.sleep(2)

    print("可以下一关吗？")
    img = take_screenshot()
    pos, val = image_to_position(img, yanchujiesu)
    if (pos and val > 0.8):
        pos, val = image_to_position(img, xiayiguan)
        if (pos and val > 0.8):
            adb_click(pos)
        else:
            pos,_=image_to_position(img,guanbi)
            adb_click(pos)
            time.sleep(2)
            print("有剧情吗？")
            img = take_screenshot()
            pos, val = image_to_position(img, juqinghuifang)
            while (val > 0.8):
                pos1, val1 = image_to_position(img, next)
                adb_click(pos1)
                time.sleep(0.6)
                pos_xz, val_xz = image_to_position(img, xuanze)
                if pos_xz and val_xz > 0.8:
                    adb_click(pos_xz)
                img = take_screenshot()
                pos, val = image_to_position(img, juqinghuifang)
            time.sleep(2)
            img = take_screenshot()
            pos, val = image_to_position(img, fanhui)
            adb_click(pos)
            time.sleep(2)

if __name__ == '__main__':
    adb_init()
    zhuxianjuqing = cv2.imread("zhuxianjuqing.png")
    kaishi=cv2.imread("kaishi.png")
    loading=cv2.imread('loading.png')
    juqinghuifang=cv2.imread("juqinghuifang.png")
    redu=cv2.imread("redu.png")
    next=cv2.imread("next.png")
    win= cv2.imread("win.png")
    yanchujiesu=cv2.imread("yanchujiesuan.png")
    xiayiguan=cv2.imread("xiayiguan.png")
    fanhui=cv2.imread("fanhui.png")
    xuanze=cv2.imread("xuanze.png")
    guanbi=cv2.imread("guanbi.png")
    while(True):
        juqing(zhuxianjuqing,kaishi,loading,juqinghuifang,redu,next,win,yanchujiesu,xiayiguan,fanhui,xuanze,guanbi)