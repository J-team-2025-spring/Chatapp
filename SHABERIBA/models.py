# abort→flaskの機能 サーバーエラー（500）を返す
from flask import abort
# pymysql→MySQLに接続してSQLを打てるようにするためのライブラリ
import pymysql
# utilフォルダのDBファイルをインポート
from util.DB import DB


# 初期起動時にコネクションプールを作成し接続を確立
# DBクラス（DB.py)の関数呼び出し、DB接続プールを初期化
db_pool = DB.init_db_pool()


# ユーザークラス
class User:
   @classmethod
   #新規ユーザー登録
   def create(cls, uid, name, email, password):
       # get_conn()で接続を取得
       conn = db_pool.get_conn()
       #try→とりあえず実行
       try:
           #カーソルを自動管理
           with conn.cursor() as cur:
               #SQL文を書く、%s→プレースホルダー
               sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
               #プレースホルダに引数を渡して実行（SQLインジェクション対策）
               cur.execute(sql, (uid, name, email, password,))
               #DBに反映
               conn.commit()
        #except→もしエラーがおきたらこれを処理
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           #500エラーを返す
           abort(500)
        #finally→エラーがあってもなくても最後にこれをやる
       finally:
           #releaseで接続を返却
           db_pool.release(conn)


   @classmethod
   #メールアドレスでユーザー検索
   def find_by_email(cls, email):
       conn = db_pool.get_conn()
       try:
               with conn.cursor() as cur:
                   sql = "SELECT * FROM users WHERE email=%s;"
                   cur.execute(sql, (email,))
                   #1件だけ値を取得
                   user = cur.fetchone()
               return user
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


# チャンネルクラス
class Channel:
   #新規チャンネル作成
   @classmethod
   def create(cls, uid, new_channel_name, new_channel_description):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               #テーブルに追加
               sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
               cur.execute(sql, (uid, new_channel_name, new_channel_description,))
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   #全チャンネル取得
   def get_all(cls):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "SELECT * FROM channels;"
               cur.execute(sql)
               #値を全件取得
               channels = cur.fetchall()
               return channels
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   #チャンネルIDで特定のチャンネルを検索
   def find_by_cid(cls, cid):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "SELECT * FROM channels WHERE id=%s;"
               cur.execute(sql, (cid,))
               channel = cur.fetchone()
               return channel
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   #チャンネル名で検索
   def find_by_name(cls, channel_name):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "SELECT * FROM channels WHERE name=%s;"
               cur.execute(sql, (channel_name,))
               channel = cur.fetchone()
               return channel
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   #チャンネル情報の更新
   def update(cls, uid, new_channel_name, new_channel_description, cid):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
               cur.execute(sql, (uid, new_channel_name, new_channel_description, cid,))
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   def delete(cls, cid):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "DELETE FROM channels WHERE id=%s;"
               cur.execute(sql, (cid,))
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


# メッセージクラス
class Message:
   @classmethod
   #新規メッセージ作成
   def create(cls, uid, cid, message):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
               cur.execute(sql, (uid, cid, message,))
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   #特定チャンネルの全メッセージ取得
   def get_all(cls, cid):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = """
                   SELECT id, u.uid, user_name, message 
                   FROM messages AS m 
                   INNER JOIN users AS u ON m.uid = u.uid 
                   WHERE cid = %s 
                   ORDER BY id ASC;
               """
               cur.execute(sql, (cid,))
               messages = cur.fetchall()
               return messages
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)


   @classmethod
   def delete(cls, message_id):
       conn = db_pool.get_conn()
       try:
           with conn.cursor() as cur:
               sql = "DELETE FROM messages WHERE id=%s;"
               cur.execute(sql, (message_id,))
               conn.commit()
       except pymysql.Error as e:
           print(f'エラーが発生しています：{e}')
           abort(500)
       finally:
           db_pool.release(conn)