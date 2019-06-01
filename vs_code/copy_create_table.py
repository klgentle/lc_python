" add drop table in the head "
import os

path = "/mnt/e/yx_walk/report_develop/sky/TABLE"
path2 = "/mnt/e/yx_walk/report_develop/sky/TABLE2"

for folderName, subfolders, filenames in os.walk(path):
    for file_name in filenames:
        #print(f"file_name:{file_name}")
        file_name2 = os.path.join(path2, file_name)
        # if file_name != 'cbs_fh00_aa_account_det000.sql':
        #    continue
        #print(f"file_name2:{file_name2}")
        f2 = open(file_name2, "w")
        with open(os.path.join(path, file_name), encoding="utf-8-sig") as f:
            head = f"drop table ODSUSER_DM.{file_name.split('.')[0].upper()}; \n"
            f2.write(head)
            for data in f.readlines():
                f2.write(data)
        f2.close()

print("Done")
