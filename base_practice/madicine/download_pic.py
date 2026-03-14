import requests
import os


def download_image(url, save_path=None):
    """
    下载指定URL的图片并保存到本地

    参数:
        url (str): 图片的URL
        save_path (str): 保存路径(可选)，如果不指定则保存到当前目录
    """
    try:
        # 发送HTTP GET请求
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 确定保存路径
        if save_path is None:
            # 如果没有指定保存路径，使用URL中的文件名
            filename = url.split('/')[-1]
            save_path = os.path.join(os.getcwd(), filename)
        else:
            # 确保保存路径的目录存在
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 写入文件
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"图片已成功下载到: {save_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"下载图片时出错: {e}")
        return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False


def get_count_of_pic(url):
    count = url.split("thumb/")[1].replace('.png', '')
    return int(count)


def download_image_in_bath(url, save_path, chapter, section):
    # url = https://s3.cldisk.com/sv-w9/doc/9d/a1/44/373dc73acb2b92fc037ea08e5a7aecd1/thumb/80.png
    count = get_count_of_pic(url)
    print(f"test: count: {count}")
    new_url = url.split("thumb/")[0] + 'thumb/'
    print(f"test: new_url: {new_url}")
    for i in range(1, count+1):
        image_url = f"{new_url}/{i}.png"
        file_path = f"{save_path}/{chapter}/{chapter}-{section}-{i}.png"
        # 检查文件是否已存在，避免搞错了覆盖已下载的文件
        if os.path.exists(file_path):
            print(f"{file_path} already exists, please check chapter and section name!")
            exit(1)
        download_image(image_url, file_path)
    print("All Done.")


# C8,1 to 58
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/fe/6c/d4/18d60ad24ad3e3dd6c2e9b5ddbed2390/thumb"
# C9, 1 to 89
# url = "https://s3.cldisk.com/sv-w7/doc/11/c7/87/a53280dd86919c31c17309710f6608fd/thumb"
# C10 1, 1 to 23
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/35/3c/41/d687995d26b127af3861e2b953fcd915/thumb"
# C10 2, 1 to 31
# url = "https://s3.cldisk.com/sv-w7/doc/ac/42/e0/ba19bad64b4544da56a37091b5b520bc/thumb"
# C10 3, 1 to 23
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/e5/30/83/871845e978ba2706a66a7e912a6f46b1/thumb"
# C10 4, 1 to 20
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/50/c6/56/493ac699f487758780658b416187bba2/thumb"
# C11 1 to 61
# url = "https://s3.ananas.chaoxing.com/sv-w9/doc/00/a0/74/891a55c00e540465ea1e30ad07898411/thumb"
# C12 S1 1 to 31
# url = "https://s3.cldisk.com/sv-w8/doc/05/23/22/d0f6cbe1968e5702daf673f60e9ac482/thumb"
# C12 S2_1 1 to 14
# url = "https://s3.cldisk.com/sv-w7/doc/c8/50/7e/1b44c98e04a007430a62119fca88a978/thumb"
# C12 S2_2 1 to 28
# url = "https://s3.cldisk.com/sv-w9/doc/d3/7d/87/088d5d03b9b85f3ec3de8ea5572e6e08/thumb"
# C12 S3_1, 1 to 25
# url = "https://s3.cldisk.com/sv-w9/doc/a7/b7/dd/d0c69a3ef7c41380826dc141ebb56e46/thumb"
# C12 S3_2, 1 to 45
# url = "https://s3.cldisk.com/sv-w8/doc/f3/56/f7/14479e52b9437ae5a69e0f175c9fbc46/thumb"
# C12 S4, 1 to 26
# url = "https://s3.cldisk.com/sv-w7/doc/d1/ce/8d/4262f25cafa0d781c63ba45d00a4339a/thumb"
# C12 S5, 1 to 26
# url = "https://s3.cldisk.com/sv-w9/doc/28/dd/7b/cf878b50e05aac3ca4eece65326203f3/thumb"
# C12 S6, 1 to 12
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/b7/47/73/c039f6ee357de1a6cf756cfa1fb247ad/thumb"
# C13 S1_1, 1 to 36
# url = "https://s3.cldisk.com/sv-w8/doc/b6/4f/e2/fc036d192b664de8fd0f3b8c25018d42/thumb"
# C13 S1_2, 1 to 41
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/45/b5/a9/b2c01799119f5f95d3f1cd63b029b82f/thumb"
# C13 S2_1, 1 to 13
# url = "https://s3.cldisk.com/sv-w8/doc/d4/48/d8/b3deb314974d7fcf214abb2d230b9f09/thumb"
# C13 S2_2, 1 to 42
# url = "https://s3.cldisk.com/sv-w9/doc/8f/fc/62/85ce0f643240a955373a4a91ca73b83e/thumb"
# C13 S3_1, 1 to 19
# url = "https://s3.cldisk.com/sv-w9/doc/a3/c7/af/f94e1a829e9829793a7a83f9e7a11b46/thumb"
# C13 S3_2, 1 to 41
# url = "https://s3.cldisk.com/sv-w9/doc/72/ce/4d/8f192c2dd0fc599ae565b3760cab750b/thumb"
# C13 S4_1, 1 to 17
# url = "https://s3.cldisk.com/sv-w8/doc/1a/e5/64/4e15dd9ec34c63b1e939aadb8abb5a51/thumb"
# C13 S4_2, 1 to 13
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/4f/b4/2e/e3f9926e18f8b6b8a9f0d973b7dc49ca/thumb"
# C14 S1, 1 to 74
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/9a/63/96/59e0fc11c9d5466f4de9eeece3c6505e/thumb"
# C14 S2, 1 to 51
# url = "https://s3.cldisk.com/sv-w7/doc/7e/cb/eb/f8f9da0ce017e29492c0b3768785a068/thumb"
# C14 S3, 1 to 45
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/1b/fb/2c/9c31a888b088700a493522519517a321/thumb"
# C14 S4, 1 to 81
# url = "https://s3.cldisk.com/sv-w9/doc/9d/a1/44/373dc73acb2b92fc037ea08e5a7aecd1/thumb/80.png"
# c14 S5
# url = "https://s3.cldisk.com/sv-w9/doc/68/93/0e/7e2a4c7bee3bcd9ccd8a92d27086819b/thumb/37.png"
# C14 S6
# url = "https://s3.cldisk.com/sv-w8/doc/17/ad/eb/016318ecf054ad0f352c4f65f0f2740b/thumb/62.png"
# C15 S1
# url = "https://s3.cldisk.com/sv-w9/doc/4d/06/83/63ab5a5d93f99f824d793c3f263895b4/thumb/47.png"
# C15 S2
# url = "https://s3.cldisk.com/sv-w7/doc/95/b7/54/33fee916f341d24a5fe7200ce85708f8/thumb/33.png"
# C15 S3
# url = "https://s3.cldisk.com/sv-s1/doc/66/84/66/ac12a4f0a22aebf80f0784d015856ae8/thumb/53.png"
# C16 S1
# url = "https://s3.cldisk.com/sv-s2/doc/2f/d4/23/5b2ac3be59b78a0a0318cd7f3a598a9d/thumb/61.png"
# C16 S2
# url = "https://s3.cldisk.com/sv-w6/doc/6f/55/fa/e16718be752a8051a080dcad8776f206/thumb/9.png"
# C16 S3
# url = "https://s3.cldisk.com/sv-w5/doc/97/98/9b/aa14ed12c68a447b077071b3352af381/thumb/49.png"
# C16 S4_1
# url = "https://s3.ananas.chaoxing.com/sv-w9/doc/cd/df/9e/d449bac4f4dfc2eca9d491d83b5c8d53/thumb/107.png"
# C16 S4_2
# url = "https://s3.ananas.chaoxing.com/sv-w9/doc/d9/c3/ee/e699bdac730ccb2594cb65338e78982c/thumb/39.png"
# C16 S5
# url = "https://s3.ananas.chaoxing.com/sv-w9/doc/3b/1d/50/3112fa2ac4e4cd9901a834ce2bd96a59/thumb/29.png"
# C16 S6
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/2b/58/97/c23eeaa9479d77faff53ed29c25ab880/thumb/42.png"
# C16 S7
# url = "https://s3.cldisk.com/sv-w9/doc/60/8e/12/260955dcea441704946c0b82c5d7292b/thumb/25.png"
# C17 T1
# url = "https://s3.cldisk.com/sv-w7/doc/ae/b8/3a/7058424b20e800ea7a6bac805e6d6515/thumb/36.png"
# C17 T2
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/ef/12/0d/f60e7e2d916733f626ab546422e3aacb/thumb/27.png"
# C17 T3
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/08/3e/ad/27fc31c44e85425ef12c9adc2fd7e1df/thumb/11.png"
# C18
# T1
# url = "https://s3.cldisk.com/sv-w8/doc/d7/87/d8/45284887ed9756a365619c3f8631c447/thumb/47.png"
# T2
# url = "https://s3.cldisk.com/sv-w8/doc/a3/6c/77/b05d0412eca27aa01573a594cb50fc9d/thumb/27.png"
# T3
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/cf/ad/50/302708183ae5f2b03616ecb439ee2e07/thumb/46.png"
# T4
# url = "https://s3.cldisk.com/sv-w7/doc/72/95/5d/464403172c5b75f26655e3fb897b3e29/thumb/27.png"
# T5
# url = "https://s3.cldisk.com/sv-w5/doc/52/19/08/c475ba9742b0c99660c91c553e698d63/thumb/30.png"
# C19
# S1
# url = "https://s3.cldisk.com/sv-w8/doc/37/b9/f6/2b01c57b6381cdaa29a89640d0b1de72/thumb/48.png"
# S2
# url = "https://s3.cldisk.com/sv-w8/doc/70/b9/7e/07cc35b46e5868abe8bf9cebcc518518/thumb/58.png"
# S3
# url = "https://s3.ananas.chaoxing.com/sv-w8/doc/43/fc/ea/9d22f8c932c1852fdf839d3abd5bc09f/thumb/21.png"
# S4
# url = "https://s3.cldisk.com/sv-w9/doc/c2/66/1b/d6a4aa75607ffb529d870bb45239cd17/thumb/35.png"
# S5
# url = "https://s3.cldisk.com/sv-w9/doc/9d/05/2e/e137f07b64230e90e522986e11108501/thumb/34.png"
# C20
# url = "https://s3.cldisk.com/sv-w9/doc/3e/4b/0f/27e083184b79b386608758b7ccc68e11/thumb/70.png"
# C21
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/cf/f2/86/0a3a1eb08537da38cba65a99e0e644e5/thumb/57.png"
# C22
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/89/ab/ce/d2d08354278384a788e7750812fd5130/thumb/88.png"
# C23
# url = "https://s3.ananas.chaoxing.com/sv-w7/doc/1d/4b/0d/0265e8a930abe9f5709e1d82ee9ca4ab/thumb/62.png"
# C26
# url = "https://s3.cldisk.com/sv-w7/doc/7e/86/70/c807b3aef2348f4dbc2a9947d93eea23/thumb/50.png"
# C28
# url = "https://s3.cldisk.com/sv-w7/doc/ba/66/40/e9dbddf0db8f94eaa5472c5d745f3c11/thumb/34.png"
# C29
# url = 'https://s3.cldisk.com/sv-w7/doc/f8/5e/95/f4ddc700bae717c809a51bf8f713b96b/thumb/36.png'
# C30
url = "https://s3.cldisk.com/sv-w9/doc/5f/d8/18/8a22f1d50209336b6b8cbe08c8e11bd2/thumb/46.png"

chapter = "C30"
section = "S1"
path = f"C:/Users/Florian/Documents/medicine_in_use_picture"
download_image_in_bath(url, path, chapter, section)
