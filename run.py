from PIL import Image,  ImageTk # 导入图像处理函数库
import tkinter as tk           # 导入GUI界面函数库
import win32ui
import win32con
import os

file_type = 'Image File(*.bmp .jpg .png)|*.png;*.jpg;*.bmp|'

API_flag = win32con.OFN_OVERWRITEPROMPT | win32con.OFN_FILEMUSTEXIST


window = tk.Tk()
window.title('图像显示界面')
window.geometry('600x800')
global img_png           # 定义全局变量
global result_img
global path
global result_path


# 打开图像
def Open_Img():
    dlg = win32ui.CreateFileDialog(1, None, None, API_flag, file_type)  # 指定为打开文件窗口
    dlg.SetOFNInitialDir("D:")
    dlg.DoModal()
    global path
    path = dlg.GetPathName()
    print(path)
    global img_png
    Img = Image.open(path)
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack()


def Convert_Img():
    print("Save File\n")
    global path
    global result_path
    dlg = win32ui.CreateFileDialog(0, None, None, API_flag, file_type)  # 指定为保存文件窗口
    dlg.SetOFNInitialDir('D:')  # 默认打开的位置
    dlg.DoModal()
    result_path = dlg.GetPathName()  # 获取打开的路径
    print(result_path)
    cmd = "activate python36 && python test.py --photo_path {} --save_path {}".format(path, result_path)
    os.system(cmd)


btn_Open = tk.Button(window,
    text='选择图像',      # 显示在按钮上的文字
    width=15, height=2,
    command=Open_Img)     # 点击按钮式执行的命令
btn_Open.pack()    # 按钮位置
btn_Convert = tk.Button(window,
    text='转换',      # 显示在按钮上的文字
    width=15, height=2,
    command=Convert_Img)     # 点击按钮式执行的命令
btn_Convert.pack()    # 按钮位置


# 运行整体窗口
window.mainloop()
