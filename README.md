# Security_Camera
wifi安防摄像头</p>
#-----------------</p>
网络安防摄像头，当系统开启后，有人在摄像头下活动时会被拍照并存储到服务器下</p>
这应该是我大四最后一个课设实验了，大学完结撒花~~  </p>
希望自己考研能考个好成绩!!!!!!</p>
#-----------------  

一.依赖</p>
  1.Anaconda3 4.2</p>
  2.opencv3  </p>
  3.imutils  </p>
  4.requests  </p>
</p>
二.部署</p>
</p>
  1.服务器部署好所有环境后，cd到目录下，python Flask_serving.py 即可</p>
  2.ssh/xshell 链接到树莓派，配置 树莓派 加入无线网络，cd到linux_program目录下 python test.py即可</p>
  
  
#-------------更新用--------------</p>
加入了转发接口  
url = http://your_ip:port/download/time  
json 数据格式:  
{  
  nb_image:n  
  1:image1  
  2:image2  
  ...  
}  
