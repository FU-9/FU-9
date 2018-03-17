查看服务器中是否已安装mysql
```
sudo netstat -tap | grep mysql
```
如未安装则执行一下命令进行安装
 ```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
```
然后通过下面的命令查看是否安装成功
```
sudo netstat -tap | grep mysql
```
出现如下信息则安装成功![image](https://github.com/FU-9/FU-9/blob/master/img/8038576-dee455ba8b6dc130.png)
现在设置mysql允许远程访问
编辑命令
```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```
把bind-address = 127.0.0.1注释或改为bind-address = 0.0.0.0
![image](https://github.com/FU-9/FU-9/blob/master/img/8038576-287bc3db3d6d925e.png)
编辑完成之后保存退出（esc+:wq+enter）

然后通过`mysql -u 用户名 -p 密码`例：`mysql -uroot -pfufufu`*`-u -p 后不加空格` 进入mysql服务，分别执行以下授权命令：
```
grant all on *.* to root@'%' identified by '你的密码' with grant option;

flush privileges;

exit;
```
退出mysql服务，重启mysql：
```
service mysql restart
```
现在就可以在其他设备通过navicat工具远程链接Ubuntu下的mysql服务了。
