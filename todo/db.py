import sqlite3

#创立链接
#获取游标
#通过游标操作
#.......
#关闭游标
#commit
#关闭链接

class TodoDB:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

    def cursor(self):
        return self.conn.cursor()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def read_all(self):
        cursor = self.cursor()
        cursor = cursor.execute('select id, content from todo order by id desc')
        data = cursor.fetchall()
        cursor.close()
        return data

    def delete(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('delete from todo where id= ?', (todo_id, ))
        cursor.close()
        self.commit()
        return

    def read(self, todo_id):
        cursor = self.cursor()
        cursor = cursor.execute('select id,content from todo where id= ?', (todo_id, ))
        data = cursor.fetchone()
        cursor.close()
        return data

    def init_db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('create table todo (id integer primary key AUTOINCREMENT, content varchar(200))')
        cursor.close()
        conn.commit()
        conn.close()

    def create(self, text):
        cursor = self.cursor()
        cursor = cursor.execute('insert into todo(content) values (?)', (text, ))
        cursor.close()
        self.commit()


if __name__ == '__main__':
    db = TodoDB()
    result = db.read(15)
    print(result)

