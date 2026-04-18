from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')   #路由
def index():      #视图函数
    return '<h1>这是登录页面</h1><a href="/robot">登录</a>'

@app.route('/r')
def robot():
    #1.hello.html文件，要放在同目录下的templates文件夹下
    #return render_template('hello.htm')

    #2.通过get方法传输数据，引入request,修改return为以下语句，测试时网址加？id=张三
    #id=request.args.get('id')
    #return "你好!"+id

    #3.继续使用get方法，将URL的参数id传入hello.html中{{ id }}显示
    id = request.args.get('id')
    return render_template('hello.html',id=id)

if __name__=='__main__':
    app.run()