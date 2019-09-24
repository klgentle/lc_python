from subprocess import call
import shutil


# Convert using Libre Office
def convert_file(output_dir, input_file):
    call('libreoffice --headless --convert-to pdf --outdir %s %s ' %
         (output_dir, input_file), shell=True)


if __name__ == "__main__":
    input_file = r'E:\yx_walk\report_develop\uat修复\201908\pcl021_requirement.docx'
    output_dir = r"E:\yx_walk\report_develop\uat修复\201908"
    convert_file(output_dir, input_file)
