import sqlite3


class TodoDB:
    def read_all(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        # 执行一条SQL语句，创建user表:
        # insert into todo(content) values ('test1');
        cursor = cursor.execute('select content from todo')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [d[0] for d in data]
        return data

    def init_db(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('create table todo (id integer primary key AUTOINCREMENT, content varchar(200))')
        cursor.close()
        conn.commit()
        conn.close()

    def test(self):
        pass


if __name__ == '__main__':
    db = TodoDB()
    db.read_all()

    # select * from todo;