import sqlite3 as lite
import requests


# 创建数据库
def create_datebase(db_path: str):
    conn = lite.connect(db_path)  # 创建或打开数据库
    with conn:
        cur = conn.cursor()  # 数据库游标
        cur.execute('drop table if exists apples')  # 删除已存在的数据表
        # 创建新的数据表apples
        ddl = 'CREATE TABLE apples (id  INTEGER NOT NULL UNIQUE, \
        name    TEXT NOT NULL,feature   TEXT,regular TEXT,cure  TEXT,\
        img_url TEXT,PRIMARY KEY(id AUTOINCREMENT));'
        cur.execute(ddl)
        # 创建索引
        ddl = 'create unique index apples_id_uindex on apples(id);'
        cur.execute(ddl)


# 写入数据库
def save_to_database(db_path: str, records: list):
    conn = lite.connect(db_path)  # 打开数据库
    with conn:
        cur = conn.cursor()
        for record in records:  # 遍历列表
            print(record)
            # 查询数据表
            name = record['name']
            sql = f"select count(name) from apples where name='{name}'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count <= 0:  # 数据条目是不存在的
                feature = record['feature']  # 症状
                regular = record['regular']  # 发病规律
                cure = record['cure']  # 防止措施
                img_url = record['img_url']  # 图片的url
                # 定义SQL语句，插入数据
                sql = f"insert into apples(name,feature,regular,cure,img_url) values ('{name}','{feature}','{regular}','{cure}','{img_url}')"
                cur.execute(sql)
        print('数据存储工作已经完成！')


# 根据数据库中的图片字段的url去下载图片
def download_image(db_path: str, img_path: str):
    records = []
    conn = lite.connect(db_path)
    with conn:
        cur = conn.cursor()
        sql = "select id,img_url from apples"  # 所有记录
        cur.execute(sql)
        records = cur.fetchall()  # 返回所有的列表数据
    print('\n 开始下载图片...')
    for record in records:  # 遍历所有的图片
        file = img_path + "\\" + str(record[0]) + ".jpg"  # 用id命名图片文件的
        img_data = requests.get(record[1])  # 获取当前图片的数据
        with open(file, 'wb') as f:
            f.write(img_data.content)  # 保存文件
    print('\n 已经完成所有图片的下载！')