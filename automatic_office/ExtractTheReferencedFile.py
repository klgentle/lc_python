import os
import shutil
import sys 
import logging
import yaml

#logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

class ExtractTheReferencedFile(object):

    def __init__(self, versionDate):
        self.versionDate = versionDate
        self.getPath()
        self.fileList = []

    def getPath(self):
        logging.debug(os.getcwd())
        with open(os.path.join("bin", "config.yaml"), "r") as config:
            cfg = yaml.safe_load(config)
            logging.debug(cfg)
            self.systemName = cfg.get('systemName')
            self.inputDir = cfg.get('inputDir').format(self.versionDate)
            self.outputDir = cfg.get('outputDir').format(self.systemName,self.versionDate)
            self.sourceDir = cfg.get('sourceDir')

    def isPathExists(self):
        if not os.path.exists(self.sourceDir):
            logging.error("sourceDir not exists")
            return False 

        if not os.path.exists(self.inputDir):
            logging.error("inputDir[%s] not exists" % self.inputDir)
            return False 

        if not os.path.exists(self.outputDir):
            logging.info("outputDir[%s] not exists" % self.outputDir)
            os.makedirs(self.outputDir, exist_ok=True)
            logging.info("outputDir 已创建!")

        return True

    def referencedLineFormat(self, line):
        line = line.strip('\n')
        line = line.strip()
        line = line.strip(';')
        return line.replace('@..\\..\\', '')
        


    def getListFiles(self):
        for folderName, subfolders, filenames in os.walk(self.inputDir):
            for filename in filenames:
                logging.debug(filename)
                if filename.endswith(".ktr"):
                    continue
                with open(os.path.join(self.inputDir,filename), "r", encoding='gbk', errors='ignore') as f:
                    for line in f.readlines(): 
                        if line[0] == "@":
                            self.fileList.append(self.referencedLineFormat(line))
        logging.debug(self.fileList)

    def copyFile(self, fromDir, toDir):
        if not os.path.exists(toDir):
            os.makedirs(toDir, exist_ok=True)

        try:
            shutil.copy(fromDir, toDir)
        except FileNotFoundError:
            logging.error("[%s] not find" % fromDir)

    def copyAllFiles(self):
        if self.isPathExists():
            self.getListFiles()
        for filename in self.fileList:
            logging.debug(filename)
            file_and_dir_list = filename.split("\\")
            target_path = os.path.join(self.outputDir, "\\".join(file_and_dir_list[:-1]))
            from_path = os.path.join(self.sourceDir, filename)
            self.copyFile(from_path, target_path)
        logging.info("python 取文件完成")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请输入versionDate")
        sys.exit(1)
    if len(sys.argv[1]) != 11:
        print("versionDate格式不符", sys.argv[1])
        sys.exit(1)
    versionDate = sys.argv[1]
    o = ExtractTheReferencedFile(versionDate)
    o.copyAllFiles()
