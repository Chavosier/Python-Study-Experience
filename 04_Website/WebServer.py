'''
picked from 必修2 P145-146
'''
# coding = UTF-8
import json
import sqlite3
import datetime
from flask import Flask, render_template, request
DATABASE='data/data.db'
app=Flask(__name__)
@app.route("/")
def hello():
    '''
    显示数据
    '''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sensorlog WHERE sensorid=1") # 查询传感器1的所有记录
    data = cursor.fetchall()
    cursor.close()
    db.close()
    temp=data[-1][2] # 取最后一条记录的第3列（温度值）
    return render_template("views.html", data=data,temp=temp)
# adding data
@app.route("/add", methods=["POST", "GET"])
def add_data():
    '''
    添加数据
    '''
    if request.method == "POST":
        jsonvalue = json.loads(request.data)
        sensorid = jsonvalue["id"]
        sensorvalue = jsonvalue["val"]
    elif request.method == "GET":
        sensorid = request.args.get("id")
        sensorvalue = request.args.get("val")
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("INSERT INTO sensorlog (sensorid, sensorvalue, time) VALUES (%d, %f, '%s')", (sensorid, sensorvalue, nowtime))
    db.commit()
    cursor.execute("SELECT * FROM sensorlog WHERE sensorid= %d" % sensorid) # 查询传感器数据
    rv= cursor.fetchall()
    cursor.close()
    db.close()
    maxrv=rv[0][2]
    minrv=rv[0][3]
    if sensorvalue > maxrv or sensorvalue < minrv: # 蜂鸣器输入判定
        return "0"
    else:
        return "1"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)