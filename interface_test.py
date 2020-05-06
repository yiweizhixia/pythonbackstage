import pymysql


def getcontent():
    conn = pymysql.connect("120.26.131.95", 'root', '123456', 'first')
    cur = conn.cursor()
    sql = "select * from First_stu"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    para = []
    for i in data:
        text = {'id':i[0],'name':i[1]}
        print(text)
        para.append(text)


if __name__ == '__main__':
    getcontent()
