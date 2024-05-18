### 使用说明（仅在UR10机器人下测试通过）：
1. 先建立环境 conda create --name myur python=3.9
2. conda activate myur
3. 安装 pip install ur-rtde
4. 打开UR机器人或者UR模拟器，确认能够从笔记本ping通UR的ip
5. 运行URRealtime.py（机器人关节的初始值是设置在这个py文件中的）
6. 然后打开sendUDP.gh 和3dm文件
7. 然后拖动gh文件中的slider就可以看到实时控制效果了