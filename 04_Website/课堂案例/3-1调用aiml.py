from flask import Flask,render_template,request
import aiml

k = aiml.Kernel()
k.learn("cn-startup.xml")
k.respond("load aiml cn")
k.respond("start")

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>这是登录页面</h1><a href="/robot">登录</a>'

@app.route('/robot',methods=['GET','POST'])   #修改方式
def talk():
    if request.method=='GET':
        return render_template('gossip.html',robot_msg='开始聊天吧！')
    if request.method=='POST':
        msg=request.form.get('msg')   #获取gossip.html的表单中的输入内容msg
        if msg=='':
            return render_template('gossip.html', robot_msg='请不要保持沉默')
        else:
            return render_template('gossip.html',robot_msg=k.respond(msg))
            #gossip.html显示的机器人回答robot_msg，由aiml语料库产生对msg的回答

if __name__=='__main__':
    app.run()