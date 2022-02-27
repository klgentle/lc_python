"""
file sample:
万历十五年 (黄仁宇)
- 您在位置 #135-135的标注 | 添加于 2016年9月23日星期五 上午5:59:19

嫡母隆庆的皇后陈氏
==========
万历十五年 (黄仁宇)
- 您在位置 #145-145的标注 | 添加于 2016年9月23日星期五 上午6:01:40

后来居上，实在是本末颠倒。
==========
"""

import os.path
import re

# from pprint import pprint

# my_clippings_file = r"D:\文本\kindle电子书\My Clippings-test.txt"
my_clippings_file = r"D:\文本\kindle电子书\My Clippings.txt"
target_note_path = r"D:\文本\kindle电子书\notes"


def read_and_split_notes():
    with open(my_clippings_file, "r", encoding='utf-8-sig') as note_file:
        all_notes = note_file.read()
        return all_notes.split("==========\n")


def move_notes_according_to_book_name():
    all_notes_list = read_and_split_notes()
    # 去掉最后一个无效的 Note
    if not all_notes_list[-1]:
        all_notes_list.pop()
    book_note_dict = {}
    for note in all_notes_list:
        note_line_list = note.split("\n")
        book_name = note_line_list[0].replace("\ufeff", "")
        book_name = re.sub(r'[,. -!?:/]', '_', book_name)
        page_info = note_line_list[1].split(" | ")[0].replace("- 您在位置 ", "").replace("的标注", "")
        note_content_with_page = " ".join([page_info, note_line_list[3]])
        if book_name in book_note_dict.keys():
            book_note_dict[book_name].append(note_content_with_page)
        else:
            book_note_dict[book_name] = [note_content_with_page]

    # pprint(book_note_dict)
    return book_note_dict


def write_note_to_files():
    for book_name, content in move_notes_according_to_book_name().items():
        if not os.path.exists(target_note_path):
            os.makedirs(target_note_path)
        # print(f"Book name:{book_name}")
        try:
            with open(os.path.join(target_note_path, book_name[0:60] + '.txt'), "a", encoding="utf-8") as note_file:
                note_file.write("\n".join(content))
        except OSError:
            print(f"Error found with content:", '\n'.join(content))
    print("Write complete. Please check note files.")


if __name__ == "__main__":
    write_note_to_files()
