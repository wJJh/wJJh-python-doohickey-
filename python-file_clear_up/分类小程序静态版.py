import os
import shutil
import time


class moveFile():
    # 把需要的资源提前缓存 如当前目录的所有文件格式、名字、文件夹
    def __init__(self):
        self.Path = os.listdir(".")  # 遍历当前目录所有文件
        self.Dir = [i for i in self.Path if os.path.isdir(i)]  # 收集文件夹
        self.File = [i.split(".") for i in self.Path if os.path.isfile(i)]  # 文件
        self.Format = {i.split(".", -1)[-1] for i in self.Path if os.path.isfile(i)}  # 收集格式
        self.dirCreate1 = ['代码', '视频', '音乐', '文档', '图片', '压缩包']  # 简易模式所创建的文件夹
        moveFile.main(self)

    #    主函数 控制程序走向
    def main(self):
            moveFile.JudegAndCreate1(self)
            moveFile.moveFile(self)

    # 根据文件格式创建文件夹
    def JudegAndCreate1(self):
        for i in self.Format:
            if i in "exe":
                continue
            if i not in self.Dir:
                os.mkdir(str(i))

    # 根据简易模式创建文件夹
    def JudegAndCreate2(self):
        for i in self.dirCreate1:
            if i not in self.Dir:
                os.mkdir(str(i))

    # 文件格式移动文件方法
    def moveFile(self):
        for i in self.File:
            if i[0] in "分类小程序":
                continue
            elif i[1] in "exe":
                continue
            else:
                print("成功移动" + i[0] + "文件")
                shutil.move(i[0] + '.' + i[1], i[1])
        print("以成功归类完成")
        print("3秒后自动退出")
        time.sleep(3)
        exit()

    # 简易模式移动文件方法
    def easyFile(self):
        easyfile = {
            '代码': ['java', 'py', 'html', 'scala'],
            '视频': ['avi', 'wmv', 'mp4'],
            '文档': ['docx', 'dot', 'doc', 'wps', 'xlsx', 'csv', 'xls', 'pps', 'ppt', 'pptx', 'xml', 'txt'],
            '音乐': ['mp3', 'wma', 'mpeg', 'wav'],
            '图片': ['psd', 'jpg', 'png', 'gif', 'jpeg', 'pdf'],
            '压缩包': ['jar', 'zip', 'rar']
        }  # 让不同格式的文件直接归类
        for aa in self.File:
            for i in easyfile.values():
                if aa[0] in "分类小程序":
                    continue
                if aa[1] in i:
                    f = list(easyfile.keys())[list(easyfile.values()).index(i)]
                    print("成功移动" + aa[0] + "文件")
                    shutil.move(aa[0] + '.' + aa[1], f)
        print("以成功归类完成")
        exit()


if __name__ == '__main__':
    moveFile()
