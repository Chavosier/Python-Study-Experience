from curses import baudrate

from micrbit import *
import Obloq # 移动网络模块
# 温度传感器在pin0, 蜂鸣器在pin8
IP = '192.168.1.100'
PORT = '8080'
SSID = 'your_wifi_ssid'
PASSWORD = 'your_wifi_password'

uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=pin1, rx=pin2) # 初始化串口通信
while Obloq.connect_wifi(SSID, PASSWORD,10000)!=True:
    display.scroll('WiFi connection failed, retrying...')

display.scroll(Obloq.ifconfig()) # 显示IP地址
Obloq.httpset(IP, PORT) # 设置服务器地址和端口

while True:
    temp = round((pin0.read_analog()/1024)*3000/10.24,1) # 读取温度传感器数据并转换为摄氏度
    errno,resp = Obloq.get('add', 'id=1&val={}'.format(temp)) # 发送数据到服务器
    if errno == 200:
        display.scroll('Data sent successfully: {}'.format(temp))
        if resp == '1':
            pin8.write_digital(1)
        elif resp == '0':
            pin8.write_digital(0)
    else:
        display.scroll('Failed to send data, error code: {}'.format(errno))
    sleep(5000) # 每5秒发送一次数据