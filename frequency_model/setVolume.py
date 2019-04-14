# coding=utf-8
import win32api

WM_APPCOMMAND = 0x319

APPCOMMAND_VOLUME_MAX = 0x0A
APPCOMMAND_VOLUME_MIN = 0x09


def setVolume(volume: int):
    # 按公式处理音量数值
    # l = int(APPCOMMAND_VOLUME_MAX) - int(APPCOMMAND_VOLUME_MIN)
    volume = volume / 100 
    mult = int(volume*0x10000)
    win32api.SendMessage(-1, WM_APPCOMMAND, 0x30292, APPCOMMAND_VOLUME_MAX * hex(mult))


if __name__ == "__main__":
    # 中等音量
    setVolume(15)
    # 静音
    # SetVolume(0)
