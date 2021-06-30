import chardet
import codecs
import logging
import sys
import os
import encodings.idna

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def convert_file(filename, out_enc):
    # !!! does not backup the origin file
    content = ""
    with codecs.open(filename, "rb") as f:
        content = f.read()
    source_encoding = chardet.detect(content)["encoding"]
    if not source_encoding:
        logging.info("source_encoding??", filename)
        return
    if source_encoding != out_enc:
        logging.info("{0},{1}".format(source_encoding, filename))
        content = content.decode(source_encoding, "ignore")
        with codecs.open(filename, "w", encoding=out_enc) as f:
            f.write(content)


def convert_folder(dir, out_enc="GB2312"):
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(file)
            path = os.path.join(root, file)
            convert_file(path, out_enc)


if __name__ == "__main__":
    #dir="/mnt/e/cx_ods/ODS需求跟问题/"
    #usage: python3 change_files_encode.py dir_name gb2312 
    convert_folder(sys.argv[1], sys.argv[2])
