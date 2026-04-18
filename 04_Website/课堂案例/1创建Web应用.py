from flask import Flask
app=Flask(__name__)
#创建 flask 实例 app，其中__name__ 是内置变量，表示当前模块的名字

@app.route('/')   #路由
def index():      #视图函数
    return '这是我的第一个网页程序！'
    #return '<h1>这是登录页面</h1><a href="/robot">登录</a>'

@app.route('/robot')
def robot():
    return '<html><body><h1>你好！</h1><h2>开始聊天吧</h2></body></html>'

if __name__=='__main__':
    app.run()