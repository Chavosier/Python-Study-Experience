from flask import Flask,render_template,request,redirect
import sqlite3
import aiml
k = aiml.Kernel()
k.learn("cn-startup.xml")
k.respond("load aiml cn")
k.respond("start")

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # 读取网站的所有用户名和密码
    conn = sqlite3.connect('robot.db')
    c = conn.cursor()  # 获取游标
    data = c.execute("select username,password from user")
    user = {}
    for row in data:
        user[row[0]] = row[1]
    conn.commit()
    conn.close()

    if request.method=='GET':
        return render_template('userlogin.html')
    if request.method=='POST':
        id=request.form.get('id')
        pwd=request.form.get('pwd')
        if id in user.keys():
            if pwd==user[id]:
                return redirect('/robot?'+'id='+id)
                #用render_template不能改变路由地址，因此使用redirect重新定向，并将xm用get方法传递给模板
            else:
                return render_template('userlogin.html',erromsg='密码错误！')
        else:
            return render_template('userlogin.html',erromsg='账号不存在！')

@app.route('/robot',methods=['GET','POST'])   #修改方式
def talk():
    if request.method=='GET':
        id=request.args.get('id')
        return render_template('gossip.html',id=id,robot_msg='开始聊天吧！')
    if request.method=='POST':
        msg=request.form.get('msg')   #获取gossip.html的表单中的输入内容msg
        if msg=='':
            return render_template('gossip.html', robot_msg='请不要保持沉默')
        else:
            return render_template('gossip.html',robot_msg=k.respond(msg))
            #gossip.html显示的机器人回答robot_msg，由aiml语料库产生对msg的回答

if __name__=='__main__':
    app.run()