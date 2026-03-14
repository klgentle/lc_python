from PIL import Image
import os


def resize_images_in_folder(input_folder, output_folder, new_size=(800, 600)):
    """
    批量修改文件夹中所有图片的分辨率

    参数:
        input_folder (str): 输入文件夹路径
        output_folder (str): 输出文件夹路径
        new_size (tuple): 新分辨率(width, height)
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        try:
            # 打开图片文件
            with Image.open(input_path) as img:
                # 调整分辨率
                resized_img = img.resize(new_size, Image.LANCZOS)

                # 构建输出路径
                output_path = os.path.join(output_folder, filename)

                # 保存图片（保持原始格式）
                resized_img.save(output_path)
                print(f"已处理: {filename} -> {new_size}")

        except Exception as e:
            print(f"无法处理 {filename}: {e}")


# 使用示例
input_dir = "C:/Users/Florian/Documents/medicine_in_use_picture/C1"  # 替换为你的输入文件夹路径
output_dir = "C:/Users/Florian/Documents/medicine_in_use_picture/C1_resize"  # 替换为你的输出文件夹路径
# target_size = (1024, 768)  # 设置目标分辨率
target_size = (1280, 1024)

resize_images_in_folder(input_dir, output_dir, target_size)