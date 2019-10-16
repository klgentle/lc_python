import os
import time


def list_file(path: str, file_name: str, path2: str):
    to_file = open(file_name, "w")
    date_str = time.strftime("%Y%m%d", time.localtime())
    to_path = f"D:\jdong\\beta\\{date_str}beta\\{path2}"
    for f in os.listdir(path):
        s = f"@@{to_path}\{f};\n"
        to_file.write(s)

    to_file.write("commit;\n")
    to_file.close()
    #print("list file done!")

def list_file_temp(list_file: str):
    file_list = []
    with open(list_file,"r") as file:
        file_list = file.read().strip().split('\n')
    
    to_file = open("list_pro.sql", "w")
    to_file.write(f"set define off\nspool.log\n\n")
    for proc_name in file_list:

        file_name = proc_name+'.sql'
        name_without_type = proc_name
        s = f"prompt\nprompt {name_without_type}\n@@{file_name}\nprompt\nprompt ==============================\nprompt\n"
        to_file.write(s)

    to_file.write("\nspool off\ncommit;\n")
    to_file.close()

if __name__ == "__main__":
    path = "/mnt/e/walker/乌海银行/baowen"
    list_file = "12(1).sql"
    list_file_temp(list_file)
