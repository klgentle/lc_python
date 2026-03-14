def fix_misencoded_text(misencoded_text, source_encoding='gbk', misencoded_as='windows-1252'):
    """
    修复因编码错误导致的乱码文本（强化版）
    """
    try:
        # 1. 将乱码文本按错误编码编码回字节
        bytes_data = misencoded_text.encode(misencoded_as, errors='ignore')

        # 2. 用正确的编码解码字节数据
        fixed_text = bytes_data.decode(source_encoding, errors='ignore')

        return fixed_text
    except Exception as e:
        print(f"解码失败: {e}")
        return misencoded_text


# 测试数据（您的题目）
misencoded_text = """
2章 药物商品的分类
题量: 4 满分: 100.0
1【单选题】为防止药婸对胃揔揕揘揙控制药婸在肠道内定位释放，揖制成包衣片揔片剂是：
A 揝溶揜
B揞散揜
C揟腾揜
D揠下揜
E揢释揜
"""

# 修复乱码
fixed_text = fix_misencoded_text(misencoded_text, source_encoding='gbk', misencoded_as='windows-1252')

# 确保输出编码兼容（如写入文件或调整终端编码）
print(fixed_text)

