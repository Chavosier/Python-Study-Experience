# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:43:34 2026

@author: Chavosier & Kimi
"""

'''
B. Base64编码转换

Description
某字符串的字节数为3的倍数，按如下规则处理：
（1）将字符串的字节分成3字节一组，顺序连接后得到24位二进制数
（2）将得到的24位二进制数按每6位一组分成4组，每组6位
（3）在每组前面补两个0，得到4个字节的二进制数
（4）将3步中得到的4个二进制数分别转换为十进制数
（5）将每个十进制数转换为1个Base64字符，对应的字符表为
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

Format
Input
一行字符串，字节数为3的倍数，字节数小于1000
Output
Base64编码的结果

Samples
This is an example
VGhpcyBpcyBhbiBleGFtcGxl

Limitation
1s, 1024KiB for each test case.
'''

l=input()
r=''
base64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for i in range(0,len(l),3):
    t=ord(l[i])
    t=(t<<8)+ord(l[i+1])
    t=(t<<8)+ord(l[i+2])
    tem=''
    for j in range(4):
        tem=base64[t%64]+tem
        t=t//64
    r+=tem
print(r)
