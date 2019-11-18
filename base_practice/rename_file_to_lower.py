import os

# import sh


def filename_to_lower(file_dir=os.getcwd()):
    # can't rename filename to filename.lower with os.rename()
    for filename in os.listdir(file_dir):
        if filename.startswith("P_"):
            old_src = os.path.join(file_dir, filename)
            tmp_src = os.path.join(file_dir, filename.lower() + " ")
            dst_name = os.path.join(file_dir, filename.lower())
            # add blank
            os.rename(old_src, tmp_src)
            # delete blank
            os.rename(tmp_src, dst_name)


if __name__ == "__main__":
    filename_to_lower()
