# 2019ロボットシステム学 課題 2 
# システムの概要  
入力された数字をフィートとして認識しメートルに変換する  
フィートで入力された数字をパブリッシュして、それをサブスクライブしてメートルに変換するパッケージ  
## 手法  
### インストール手順
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Takeshi-Kojima/My_ROS.git
$ cd ../
$ catkin_make
```    
## 実行  
端末１  
`$ roscore`  
端末２  
`$ rosrun My_ROS pub_feet.py`  
端末３  
`$ rosrun My_ROS sub_feet.py`
## YouTube
https://www.youtube.com/watch?v=4cbgXBJuzwM&feature=share

## LICENSE  
This repository is licensed under the GPLv3 license, see LICENSE.
