import os
import cv2
from PIL import Image
import time


def Change_into_BW(file):
    img = Image.open(file)
    Img = img.convert('L')
    # Img.save("test1.jpg")
    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 图片二值化
    photo = Img.point(table, '1')
    photo.save(file)
    return file

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

def adb_click(center, offset=(0, 0)):
    (x, y) = center
    x += offset[0]
    y += offset[1]
    os.system(f"adb shell input tap {x} {y}")

def adb_init():
    os.system("adb connect 127.0.0.1:62001")

def quit():
    print("俺要跑路！")
    pos_quit, _ = image_to_position(cv2.imread("tmp.png"), cv2.imread("quit.png"))
    adb_click(pos_quit)
    time.sleep(0.8)
    take_screenshot()
    print("下次再来！")
    pos, _ = image_to_position(cv2.imread("tmp.png"), cv2.imread("exit.png"))
    adb_click(pos)
    time.sleep(1)
    take_screenshot()
    print("确认！")
    pos, _ = image_to_position(cv2.imread("tmp.png"), cv2.imread("sure.png"))
    adb_click(pos)
    adb_click((100, 100))

def enterLoop(chufamaoxian,loading):

    take_screenshot()
    screen = cv2.imread('tmp.png')
    center = image_to_position(screen, chufamaoxian)
    if (center[1] > 0.8):
        print("出发冒险！")
        # print(image_to_position(screen,template))
        adb_click(center[0])
        time.sleep(1)
        take_screenshot()
        print("死境探索确认！")
        adb_click((1432, 645))
        take_screenshot()
        screen = cv2.imread('tmp.png')
        print("加载中")
        tmp = image_to_position(screen, loading)
        while (tmp[1] > 0.8):
            time.sleep(2)
            take_screenshot()
            screen = cv2.imread('tmp.png')
            tmp = image_to_position(screen, loading)
        print("确认阵容！")
        adb_click((1380, 830))
        time.sleep(0.5)
        print("就去死境散散步，嘿嘿！")
        adb_click((900, 605))
        time.sleep(2)
        take_screenshot()


def World_Tree(chufamaoxian,loading,kaishibiaoyan,qiyu,xiuxi,tuzishangdian,huode,baoxiang,zhanbu,shezhi,fangqizhandou,fangqi,xuanze
               ,sanxuan,jiesugoumai):
    enterLoop(chufamaoxian,loading)
    j=0
    try:
        while (1):
            take_screenshot()
            j+=1
            print("*"*100)
            print("第{}轮探索，遇到啥了呢？".format(j))
            # crop_screenshot("tmp.png", 295, 420, 970, 330, "check.png")
            check = cv2.imread("tmp.png")
            print("进入战斗了：")
            _,val_zhandou=image_to_position(check,kaishibiaoyan)
            print("奇遇：")
            pos_qiyu, val_qiyu = image_to_position(check, qiyu)
            print("休息：")
            pos_xiuxi, val_xiuxi = image_to_position(check, xiuxi)
            print("兔子商店：")
            pos_tuzi, val_tuzi = image_to_position(check, tuzishangdian)
            print("升级了：")
            pos_huode, val_huode = image_to_position(check,huode)
            print("宝箱：")
            pos_baoxiang, val_baoxiang = image_to_position(check, baoxiang)
            print("占卜：")
            pos_zb, val_zb = image_to_position(check, zhanbu)
            print("*"*100)
            if(_ and val_zhandou>0.8):
                print("退出战斗中")
                pos_shezhi,_=image_to_position(check,shezhi)
                adb_click(pos_shezhi)
                take_screenshot()
                pos_fangqizhandou,_=image_to_position(cv2.imread("tmp.png"),fangqizhandou)
                adb_click(pos_fangqizhandou)
                take_screenshot()
                screen = cv2.imread('tmp.png')
                print("加载中")
                tmp = image_to_position(screen, loading)
                while (tmp[1] > 0.8):
                    time.sleep(2)
                    take_screenshot()
                    screen = cv2.imread('tmp.png')
                    tmp = image_to_position(screen, loading)
                take_screenshot()
                time.sleep(2)
                take_screenshot()
                quit()
                break
            elif (pos_huode and val_huode > 0.8):
                print("处理升级中")
                adb_click(pos_huode)
                time.sleep(0.5)
            elif (pos_baoxiang and val_baoxiang> 0.8):
                print("宝箱选择中")
                adb_click(pos_baoxiang)
                time.sleep(0.8)
                while (1):
                    time.sleep(0.8)
                    take_screenshot()
                    pos_fangqi, val_fangqi = image_to_position(cv2.imread("tmp.png"), fangqi)
                    if (val_fangqi > 0.9):
                        adb_click(pos_fangqi)
                    else:
                        break
            elif (pos_xiuxi and val_xiuxi > 0.8):
                print("正在休息中")
                adb_click(pos_xiuxi)
                time.sleep(0.8)
                while (1):
                    time.sleep(0.8)
                    take_screenshot()
                    pos_xuanze, val_xuanze = image_to_position(cv2.imread("tmp.png"), xuanze)
                    if (val_xuanze > 0.9):
                        adb_click(pos_xuanze)
                    else:
                        break
            elif (pos_qiyu and val_qiyu > 0.8):
                print("完成奇遇中")
                adb_click(pos_qiyu)
                time.sleep(0.8)
                while (1):
                    time.sleep(0.8)
                    take_screenshot()
                    pos_xuanze, val_xuanze = image_to_position(cv2.imread("tmp.png"), xuanze)
                    pos_fangqi, val_fangqi= image_to_position(cv2.imread("tmp.png"), fangqi)
                    _,val_sanxuan=image_to_position(cv2.imread("tmp.png"),sanxuan)
                    if val_sanxuan>0.9:
                        adb_click((1240,555))
                    elif(val_fangqi>0.9):
                        adb_click(pos_fangqi)
                    elif (val_xuanze > 0.9):
                        adb_click(pos_xuanze)
                    else:
                        break
            elif (pos_tuzi and val_tuzi > 0.8):
                print("商店选购中")
                adb_click(pos_tuzi)
                time.sleep(0.8)
                while (1):
                    time.sleep(0.8)
                    take_screenshot()
                    pos_jiesu, val_jiesu = image_to_position(cv2.imread("tmp.png"),jiesugoumai)
                    if (val_jiesu > 0.9):
                        adb_click(pos_jiesu)
                    else:
                        break
            elif (pos_zb and val_zb > 0.8):
                print("正在占卜中")
                adb_click(pos_zb)
                time.sleep(0.8)
                while (1):
                    time.sleep(0.8)
                    take_screenshot()
                    pos_xuanze, val_xuanze = image_to_position(cv2.imread("tmp.png"), xuanze)
                    if (val_xuanze > 0.9):
                        adb_click(pos_xuanze)
                    else:
                        break
            else:
                print("进入战斗了吗？：")
                _, val_zhandou = image_to_position(check, kaishibiaoyan)
                if (_ and val_zhandou > 0.8):
                    print("退出战斗中")
                    pos_shezhi, _ = image_to_position(check, shezhi)
                    adb_click(pos_shezhi)
                    take_screenshot()
                    pos_fangqizhandou, _ = image_to_position(cv2.imread("tmp.png"), fangqizhandou)
                    adb_click(pos_fangqizhandou)
                    take_screenshot()
                    screen = cv2.imread('tmp.png')
                    print("加载中")
                    tmp = image_to_position(screen, loading)
                    while (tmp[1] > 0.8):
                        time.sleep(2)
                        take_screenshot()
                        screen = cv2.imread('tmp.png')
                        tmp = image_to_position(screen, loading)
                    take_screenshot()
                    time.sleep(2)
                    take_screenshot()
                print("退出副本中")
                quit()
                break
    except:
        try:
            while(1):
                take_screenshot()
                pos_fangqi, val_fangqi = image_to_position(cv2.imread("tmp.png"), fangqi)
                if (val_fangqi > 0.9):
                    adb_click(pos_fangqi)
                else:
                    break
        except:
            adb_click((10,10))
            time.sleep(2)
            quit()



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    adb_init()
    chufamaoxian=cv2.imread('chufamaoxian.png')
    loading=cv2.imread('loading.png')
    kaishibiaoyan=cv2.imread("kaishibiaoyan.png")
    qiyu=cv2.imread("qiyu.png")
    xiuxi=cv2.imread("xiuxi.png")
    tuzishangdian=cv2.imread("tuzishangdian.png")
    huode= cv2.imread("huodedaoju.png")
    baoxiang=cv2.imread("baoxiang.png")
    zhanbu=cv2.imread("zhanbu.png")
    shezhi=cv2.imread("shezhi.png")
    fangqizhandou=cv2.imread("fangqizhandou.png")
    fangqi=cv2.imread("fangqi.png")
    xuanze=cv2.imread("xuanze.png")
    sanxuan=cv2.imread("sanxuanze.png")
    jiesugoumai= cv2.imread("jiesugoumai.png")
    for i in range(150):
        print("-"*100)
        print("第{}次世界树副本探索中".format(i+1))
        print("-"*100)
        World_Tree(chufamaoxian,loading,kaishibiaoyan,qiyu,xiuxi,tuzishangdian,huode
                   ,baoxiang,zhanbu,shezhi,fangqizhandou,fangqi,xuanze
                    ,sanxuan,jiesugoumai)
        i+=1
        print("-"*45+"已完成！！！"+"-"*48)
        time.sleep(4)


    #crop_screenshot("tmp.png", 1060, 705, 85, 35, "baoxiang.png")  # 1270,750
    #crop_screenshot("tmp.png", 735, 705, 85, 35, "xiuxi.png")   # 820,740
    #crop_screenshot("tmp.png", 1480, 45, 80, 60, "quit.png")  # 530,740
    #crop_screenshot("tmp.png", 450, 705, 85, 35, "zhandou.png")  # 530,740
    #take_screenshot()
    #adb_click(image_to_position(cv2.imread("tmp.png"),cv2.imread("xuanze.png")))




# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
