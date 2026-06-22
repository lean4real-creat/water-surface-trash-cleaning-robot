'''
实验名称：pyMotors多功能电机模块
版本：v1.0
日期：2021-6-21
作者：01Studio
说明：同时控制4路直流电机
平台：pyAI-K210
'''
from machine import I2C
from motor import Motors
import time

#构建I2C对象，根据自己开发板类型定义引脚
i2c1 = I2C(I2C.I2C0, mode=I2C.MODE_MASTER,scl=7, sda=6)

#构建4路直流电机对象
m=Motors(i2c1)

#直流电机对象使用用法，详情参看motor.py文件
#
#m.speed(index, value=0)
#index: 0~3表示4路直流电机
#value: 速度。-4095~4095，正负表示转向，绝对值越大速度越大


#前进
m.speed(0,4095) #直流电机0正转，速度0~4095,4095表示最快速度
m.speed(1,4095)
m.speed(2,4095)
m.speed(3,4095)

time.sleep(3)

#后退
m.speed(0,-4095) #直流电机0反转，速度0~-4095,-4095表示反转最快速度
m.speed(1,-4095)
m.speed(2,-4095)
m.speed(3,-4095)

time.sleep(3)

#制动停止
for i in range(4):
    m.brake(i)







