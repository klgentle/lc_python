import os
import sys


class RenameFileAndContent(object):
    def __init__(self, from_pattern, to_pattern, file_path):
        self.__from_pattern = from_pattern
        self.__to_pattern = to_pattern
        self.__file_path = file_path

    def getNewFilename(self, filename: str) -> str:
        return filename.replace(self.__from_pattern, self.__to_pattern)

    def renameFile(self, filename: str):
        newFilename = self.getNewFilename(filename)
        os.rename(filename, newFilename)

    def renameContent(self, filename: str):
        content = ""
        with open(filename, "r") as fr:
            content = fr.read()

        with open(filename, "w") as fw:
            fw.write(content.replace(self.__from_pattern, self.__to_pattern))

    def renameAllFile(self):
        for filename in os.listdir(self.__file_path):
            oldFileNameAndPath = os.path.join(self.__file_path, filename)
            self.renameFile(oldFileNameAndPath)
            newFilename = self.getNewFilename(oldFileNameAndPath)
            #self.renameContent(newFilename)


if __name__ == "__main__":
    # from_pattern = "MAC510_D"
    # to_pattern = "CIF360E"
    # file_path = "/mnt/c/Users/pactera/Downloads/Documents"
    # print(sys.argv)
    o = RenameFileAndContent(sys.argv[1], sys.argv[2], sys.argv[3])
    o.renameAllFile()
