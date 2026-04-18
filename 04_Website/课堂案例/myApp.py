#1、导入Flask框架模块
from flask import Flask,render_template,request
import aiml

k=aiml.Kernel()   #创建一个聊天机器人k
k.learn('cn-startup.xml')  #读取语料库
k.respond('load aiml cn')
k.respond('start')

#2、由Flask类创建一个应用实例app
app=Flask(__name__)    #__name__是系统变量，该变量指本py文件的文件名

#3、编写路由和视图函数，建立URL到程序代码的关联
@app.route('/')
def index():
    return '我的第一个网页程序！'

@app.route('/robot',methods=['GET','POST'])
def robot():
    if request.method=='GET':
       return render_template('gossip.html',robot_msg='你好！开始聊天吧')
    elif request.method=='POST':
        msg=request.form.get('msg')
        if msg=='':
            msg='不要保持沉默~'
        else:
            msg=k.respond(msg)
        return render_template('gossip.html', robot_msg=msg)

#4、启动Web应用
if __name__=='__main__':  #只有执行当前脚本才能启动web服务器
    app.run()    #run方法会启动web服务器，服务器进入轮询状态，等待用户访问并处理用户请求