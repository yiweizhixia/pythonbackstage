import pymysql

pymysql.version_info = (1, 4, 6, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()

pymysql.install_as_MySQLdb()

db = pymysql.connect("120.26.131.95", 'root', '123456', 'first')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print("Version is %s" % data)

db.close()