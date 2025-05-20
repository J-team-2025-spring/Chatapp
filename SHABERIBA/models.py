from flask import abort, flash
import pymysql 
from util.DB import DB

db_pool = DB.init_SHABERIBA_db_pool()

#ユーザークラス
class User:
  @classmethod
  def create(cls, uid, name, email, password):
    conn = db_pool.get_conn()
    try:
      with conn.cursor() as cur:
        sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s,%s,%s,%s);"
        cur.execute(sql,(uid, name, email, password, ))
        conn.commit()
    except pymysql.Error as e:
      flash(f'エラーが発生しています:{e}')
      abort(500) 
    finally:
      db_pool.release(conn)
  

  @classmethod
  def find_by_email(cls,email):
    conn = db_pool.get_conn()
    try:
          with conn.cursor() as cur:
             sql = "SELECT * FROM users WHERE email=%s;"
             cur.execute(sql,(email,))
             user = cur.fetchone()
          return user
    except pymysql.Error as e:
       print(f'エラーが発生しています:{e}')
       abort(500)
    finally:
       db_pool.release(conn)

