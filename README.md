# Security_Camera
wifi安防摄像头  
#-----------------</p>
网络安防摄像头，当系统开启后，有人在摄像头下活动时会被拍照并存储到服务器下</p>
这应该是我大四最后一个课设实验了，大学完结撒花~~  
希望自己考研能考个好成绩!!!!!!</p>
#-----------------  

一.版本控制</p>
  1.Anaconda3 4.2   
  2.opencv3  
  3.imutils  
  4.requests  
</p>
二.兼容系统</p>
</p>
  1.linux端可部署在#树莓派#上，部署前确认树莓派wifi，摄像头模块完好，且树莓派已加入局域网中</p>
  2.服务器端（Windows/linux）需要上述所有计算工具</p>
</p>
三.运行方法</p>
</p>
  1.服务器部署好所有环境后，cd到目录下，python Flask_serving.py 即可</p>
  2.ssh/xshell 链接到树莓派，配置 树莓派 加入无线网络，cd到linux_program目录下 python test.py即可</p>
