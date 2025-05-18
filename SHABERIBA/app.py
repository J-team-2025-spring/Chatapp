from flask import Flask, request, redirect, render_template, session, flash, abort, url_for
from datetime import timedelta
import hashlib
import uuid
import re
import os

from models import User




# 定数定義
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SESSION_DAYS = 30

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', uuid.uuid4().hex)
app.permanent_session_lifetime = timedelta(days=SESSION_DAYS)







# ホーム画面（仮）
@app.route('/', methods=['GET'])
def hello():
    return render_template('base.html')


# ルートページのリダイレクト処理
@app.route('/', methods=['GET'])
def index():
    uid = session.get('uid')
    if uid is None:
        return redirect(url_for('login_view'))
    return redirect(url_for('channels_view'))



# サインアップ画面
@app.route('/signup', methods =['GET'])
def signup_view():
    return render_template('signup-test.html')

@app.route('/signup', methods =['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    passwordConfirmation = request.form.get('password-confirmation')

    if name == '' or email == '' or password == '' or passwordConfirmation == '':
        flash('空欄があります')
    elif password != passwordConfirmation:
        flash('パスワードが一致していません')
    elif re.match(EMAIL_PATTERN,email) is None:
        flash('メールアドレスの形式が間違っています')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password.encode('utf-8')).hefxdigest()
        

    
        User.create(uid, name, email, password)
        # registered_user = a

        # if registered_user != None:
        #     flash('登録済みです')
        return redirect(url_for('login_view'))




# ログイン画面
@app.route('/login', methods=['GET'])
def login_view():
    return ("ログイン画面です。")





# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return ("ログアウト画面です")



# チャンネル一覧画面
@app.route('/channels', methods=['GET'])
def channels_view():
    uid = session.get('uid')
    if uid is None:
        return ("UIDなし")
    else:
        # channels = Channel.get.all()
        # channels.reverse()
        return("チャンネル一覧画面です。")




@app.errorhandler(404)
def page_not_found(error):
    return ("エラー404")

@app.errorhandler(500)
def internal_server_error(error):
    return ("エラー500")



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)