import os
filename:str = input("请输入要导出manimgl场景定义Python文件的路径:")
if not filename.endswith(".py"):
    filename += ".py"
os.system(f"manimgl {filename} --write_all -w --uhd")