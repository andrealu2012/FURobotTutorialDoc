import rtde_control
import rtde_receive
import re
import time
import numpy as np
import sys
import math
import ast
import socket

def parse_string_to_tuple(bArray):
    # 使用split()方法将字符串按逗号分割成列表
    string=bArray.decode()
    values = string.split(',')
    
    # 将列表中的字符串转换为整数
    values = [float(x) for x in values]
    
    # 返回元组
    return tuple(values)

def execute_commands(rtde_c,rtde_r,velocity=0.2,acceleration=0.2,dt=1.0/500,lookahead_time=0.2,gain=300,realv=0.2):
    radc=57.295779513082320876798154814105
    print("开始执行命令...")
    try:
        initJntPos=(1.142021, -1.187156, 1.757504, -0.568966, -0.428247, -1.572337)

        print(f"初始角度：{round(initJntPos[0]*radc,3)} ,{round(initJntPos[1]*radc,3)} ,{round(initJntPos[2]*radc,3)} ,{round(initJntPos[3]*radc,3)} ,{round(initJntPos[4]*radc,3)} ,{round(initJntPos[5]*radc,3)}")
        rtde_c.moveJ(initJntPos, velocity, acceleration)
        time.sleep(0.1)  # 等待移动完成

        while True:
            #actual_q=rtde_r.getActualQ()
            #print(f"Actual Joint: {actual_q[0]*radc} ,{actual_q[1]*radc} ,{actual_q[2]*radc} ,{actual_q[3]*radc} ,{actual_q[4]*radc} ,{actual_q[5]*radc}")
            #actual_c=rtde_r.getActualCurrent()
            #print(f"Actual Current: {round(actual_c[0],3)} ,{round(actual_c[1],3)} ,{round(actual_c[2],3)} ,{round(actual_c[3],3)} ,{round(actual_c[4],3)} ,{round(actual_c[5],3)}")
            try:
                # 尝试接收数据
                data, addr = sock.recvfrom(1024)  # 缓冲区大小为1024字节
                #print(f"Received message: {data} from {addr}")
                
                currentJntPos=parse_string_to_tuple(data)
                #print(f"Current Joint:{currentJntPos}")
                
                rtde_c.servoJ(currentJntPos, velocity, acceleration, dt, lookahead_time, gain)

            except BlockingIOError:
                # 如果没有数据可读，会引发BlockingIOError
                pass

    except KeyboardInterrupt:
        pass
        #print("用户中断程序") 
    except Exception as e:
        print(f"\n发生错误: {str(e)}")
    finally:
        print("断开与机器人的连接...")
        
        sock.close()
        rtde_c.stopScript()  # 停止脚本
        rtde_c.disconnect()
        print("连接已断开。")
        
if __name__ == '__main__':
    #HACK：机器人的IP地址
    ROBOT_IP = "192.168.56.101"

    #HACK：这里设置基本打印参数！
    velocity = 0.2
    acceleration = 0.2
    dt = 1.0/500  # 2ms
    lookahead_time = 0.2
    gain = 300
    radius = 0.01
    realv = 0.5 #HACK：这里设置实际速度mm/时间段

    # 创建 RTDE 控制和接收对象
    rtde_c = rtde_control.RTDEControlInterface(ROBOT_IP)
    rtde_r = rtde_receive.RTDEReceiveInterface(ROBOT_IP)

    # 创建一个UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定到特定的地址和端口
    udp_ip = "127.0.0.1"  # 监听所有可用的网络接口
    udp_port = 12345  # 可以根据需要选择一个端口
    sock.bind((udp_ip, udp_port))
    sock.setblocking(False)
    print(f"Listening for UDP messages on {udp_ip}:{udp_port}")

    # 执行解析出的命令
    execute_commands(rtde_c,rtde_r,velocity,acceleration,dt,lookahead_time,gain,realv)