import os
from pprint import pprint

PATH = "/mnt/d/code_test/lc_python/leet_code/top_interview_questions"
# PATH = "D\\code_test\\lc_python\\leet_code\\top_interview_questions"


def open_file(file_name: str) -> list:
    file_name_list = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            id, problem_name, difficulty = line.strip().split("\t")
            id = id.zfill(4)
            difficulty = difficulty + "_Case"
            problem_name = problem_name.strip()
            file_name_list.append([id, problem_name, difficulty])
    return file_name_list


def make_path_of_all():
    for folder_name in ("Easy_Case", "Medium_Case", "Hard_Case"):
        new_path = os.path.join(PATH, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)


def create_folder_and_file_from_list(file_name_list):
    for file_and_folder in file_name_list:
        file_name = file_and_folder[0] + "_" + file_and_folder[1] + ".py"
        folder_name = file_and_folder[2]
        new_file = os.path.join(PATH, folder_name, file_name)
        f = open(new_file, "w")
        f.close()


if __name__ == "__main__":
    make_path_of_all()
    file_name = os.path.join(PATH, "list.txt")
    file_list = open_file(file_name)
    create_folder_and_file_from_list(file_list)
    print("Done!")
