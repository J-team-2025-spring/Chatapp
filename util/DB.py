import os
import pymysql
from pymysqlpool.pool import Pool

class DB:
  @classmethod
  def init_SHABERIBA_db_pool(cls):
    pool = Pool(
      host=os.getenv('DB_HOST'),
      user=os.getenv('DB_USER'),
      passwd=os.getenv('DB_PASSWORD'),
      db=os.getenv('DB_DATABASE'),
      maxconnection=5,
      charset='utf8',
      cusorclass=pymysql.cursors.Dictcusor
    )
    pool.init()
    return pool