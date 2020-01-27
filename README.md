# 2019ロボットシステム学 課題 2 
# システムの概要  
入力した文字列の中の特定の単語の表示を規制するパッケージ
入力した文字列をrostopicとしてパブリッシュし，別ノードでサブスクライブして特定の単語を「＊＊＊」に変換  

## 手法  
### インストール手順
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Takeshi-Kojima/My_ROS.git
$ cd ../
$ catkin_make
```    
## 実行  
3つの端末を用いて，下記の各コマンドを実行する．
端末１  
`$ roscore`  
端末２  
`$ rosrun My_ROS pub_message.py`  
端末３  
`$ rosrun My_ROS sub_message.py`
## YouTube
https://youtu.be/WZDkQj4yW0M

## 一緒に課題を行った人
小関隆司　https://github.com/KosekiTakashi  
木村慧士　https://github.com/kimurasatoshi  
吉村一希　https://github.com/kazuki0702  

## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
