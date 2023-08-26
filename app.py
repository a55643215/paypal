from flask import Flask,request,abort
from line_bot_api import *
from events.basic import *


import os

app = Flask(__name__)#admin: !QAZ2wsx資料庫的帳號和密碼
#讓程式自己去判斷如果是測試端就會使用APP_SETTINGS



if __name__ == '__main__':
    app.run()