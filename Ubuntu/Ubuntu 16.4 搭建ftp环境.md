在linux种ftp的全名叫vsftpd,我们需要利用相关命令开启安装ftp服务器，然后再在vsftpd.conf中进行相关配置
(1)、首先用命令检查是否安装了vsftpd
```
vsftpd -v
```
如果未安装执行下面命令安装
```
sudo apt-get install vsftpd
```
(2)、新建一个文件夹用于FTP的工作目录
```
mkdir /home/ftp
```
(3)、新建ftp用户并设置密码以及工作目录
```
sudo useradd -d /home/ftp -s /bin/bash username
```
为新增的用户设置密码
```
passwd ftpname
```
(4)、修改vsftpd配置文件
        配置文件在/etc目录下
```
vi /etc/vsftpd.conf
```
```
// 允许匿名用户登录
anonymous_enable=YES

// 允许本地用户登录
local_enable=YES

// 开启全局上传
write_enable=YES

// 允许匿名用户上传文件
anon_upload_enable=YES  

// 充许匿名用户新建文件夹
anon_mkdir_write_enable=YES
```
(5)、启动vsftpd
```
 service vsftpd start
```
(6)、在资源管理器，或者浏览器中ftp服务器
输入账号，密码登录即可 
