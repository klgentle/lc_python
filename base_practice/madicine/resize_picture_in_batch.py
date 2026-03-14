import os
from PIL import Image


def resize_image(input_path, output_path):
    # 打开原始图片
    with Image.open(input_path) as img:
        # 使用LANCZOS重采样方法进行高质量拉伸
        resized_img = img.resize((2240, 1260), Image.Resampling.LANCZOS)
        # 保存结果
        resized_img.save(output_path)
        print(f"图片已成功拉伸并保存到 {output_path}")


def scan_png_files(root_dir='.'):
    """
    扫描目录及子目录中的所有PPT文件
    :param root_dir: 要扫描的根目录，默认为当前目录
    """
    print(f"开始扫描目录: {os.path.abspath(root_dir)}")
    print("-" * 60)

    for root, dirs, files in os.walk(root_dir):
        new_path = root + "_resize"
        os.mkdir(new_path)
        for file in files:
            resize_image(os.path.join(root, file), os.path.join(new_path, file))
            # print(f"test root:{root}, dirs: ${dirs}, files: ${file}")



if __name__ == "__main__":
    # 使用当前目录
    scan_png_files('C:/Users/Florian/Documents/medicine_in_use_picture')
    # 如果要指定其他目录，可以这样使用：
    # scan_ppt_files('/path/to/your/directory')
    # 使用示例
    # input_image = "C:/Users/Florian/Documents/medicine_in_use_picture/C2/1.png"  # 你的原始图片路径
    # output_image = "C:/Users/Florian/Documents/medicine_in_use_picture/C2_1_resized2.png"  # 输出图片路径
    # resize_image(input_image, output_image)
