from PIL import Image


def resize_image(input_path, output_path):
    # 打开原始图片
    with Image.open(input_path) as img:
        # 使用LANCZOS重采样方法进行高质量拉伸
        resized_img = img.resize((2240, 1260), Image.Resampling.LANCZOS)
        # 保存结果
        resized_img.save(output_path)
        print(f"图片已成功拉伸并保存到 {output_path}")


# 使用示例
input_image = "C:/Users/Florian/Documents/medicine_in_use_picture/C2/1.png"  # 你的原始图片路径
output_image = "C:/Users/Florian/Documents/medicine_in_use_picture/C2_1_resized2.png"  # 输出图片路径
resize_image(input_image, output_image)


