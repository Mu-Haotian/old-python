import os
import argparse
import threading

from utility import url_handle, db_handle


# 主逻辑函数
def main(database: str, input_url: str):
    print(f'存储数据的数据库是：{database}')
    print(f'网页地址列表文件是：{input_url}')
    all_records = []  # 所有数据
    urls = url_handle.read_url(input_url)  # 读取url列表    ####问题所在
    for url in urls:  # 遍历列表
        print('读取url：' + url)
        html = url_handle.get_page(url)  # 抓取页面
        records = url_handle.extract_page(html)  # 解析页面
        all_records.extend(records)  # 扩展数据集
    db_path = os.path.join(os.getcwd(), database)  # 数据库路径
    db_handle.create_datebase(db_path=db_path)  # 创建数据库
    db_handle.save_to_database(db_path=db_path, records=all_records)  # 写入数据库
    # 下载图片
    directory = 'images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    img_path = os.path.join(os.getcwd(), directory)  # 图片存放路径
    download_image = threading.Thread(target=db_handle.download_image, args=(db_path, img_path))
    download_image.start()


if __name__ == '__main__':
    # 定义命令参数行
    parse = argparse.ArgumentParser()
    parse.add_argument('-db', '--database', help='SQLite数据库名称')
    parse.add_argument('-i', '--input', help='包含url的文件名称')
    # 读取命令参数
    args = parse.parse_args()
    database_file = args.database
    input_file = args.input
    # 调用主函数
    main(database=database_file, input_url=input_file)