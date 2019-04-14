# todo a clock
import time
import os
import sys


def sleepClock(m: str):
    """input a number of minute, time up play a song"""
    file = r"D:\\music\\music_good\\澤野弘之-Aliez_end.mp3"
    m = float(m)
    if m < 0 or m > 60:
        print("请输入分钟数:0<m<60")
    time.sleep(m * 60)
    os.system(file)  # use windows to play music


if __name__ == "__main__":
    #print(sys.argv)
    sleepClock(sys.argv[1])
