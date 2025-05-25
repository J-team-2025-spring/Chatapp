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
      max_size=5,
      charset='utf8',
      cursorclass=pymysql.cursors.DictCursor
    )
    pool.init()
    return pool
  
