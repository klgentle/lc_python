#! python3
# Copies an entire foleder and its contents into a ZIP file
# whose filename increments

import zipfile, os
import shutil


def backupToZip(folder: str):

    # change path
    dirname = os.path.dirname(folder)
    os.chdir(dirname)
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    zipFilename = os.path.basename(folder) + ".zip"
    if os.path.exists(zipFilename):
        os.remove(zipFilename)

    # create the ZIP file
    print(f"Creating {zipFilename}..")
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # walk the entire folder tree and compress the files in each folder
    base_folder = os.path.basename(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        # backupZip.write(foldername)
        short_foldername = foldername[len(dirname) :]
        backupZip.write(foldername, short_foldername)  # 重命名(去掉文件名前面的绝对路径）

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = base_folder + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue  # skip backup ZIP files

            # backupZip.write(os.path.join(foldername, filename))
            short_filename = os.path.join(short_foldername, filename)
            backupZip.write(os.path.join(foldername, filename), short_filename)

    backupZip.close()
    print("Create zip done.")


if __name__ == "__main__":
    folder = "/mnt/e/yx_walk/report_develop/sky/20190505beta"
    backupToZip(folder)
