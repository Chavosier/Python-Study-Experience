from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')   #路由
def index():      #视图函数
    return '<h1>这是登录页面</h1><a href="/robot">登录</a>'

@app.route('/robot',methods=['GET','POST'])
def robot():
    if request.method == 'GET':
        return render_template('gossip.html', robot_msg='你好！开始聊天吧')
    elif request.method == 'POST':
        msg = request.form.get('msg')  # 获取表单msg框内的输入值
        if msg == '你好':
            msg = '你好呀！'
        else:
            msg = '听不懂'
        return render_template('gossip.html', robot_msg=msg)

if __name__=='__main__':
    app.run()