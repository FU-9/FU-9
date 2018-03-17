#### 一、MySQL介绍
MySQL是一个关系型数据库管理系统，由瑞典Mysql AB公司开发，目前数据Oracle旗下公司。MySQL是最流行的关系型数据库管理系统，在web应用方面MySQL是最好的RDBMS（关系数据库管理系统）软件应用之一
###### 1、MySQL是什么
```
# mysql就是一个基于socket编写的C/S架构的软件
# 客服端软件
    mysql自带：如mysql命令，mysqldump命令等
    python模块：如pymysql
    node模块：mysql
```
#### 二、下载安装
Ubuntu 版本：
[Ubuntu版本下载方式](https://github.com/FU-9/FU-9/blob/master/Ubuntu/Ubuntu16.4%20%E5%AE%89%E8%A3%85mysql.md)
Windows版本：
```
下载：mysql community server 5.7.16
http://dev.mysql.com/downloads/mysql/

#2、解压
如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64

#3、添加环境变量
【右键计算机】--》【属性】--》【高级系统设置】--》【高级】--》【环境变量】--》【在第二个内容框中找到 变量名为Path 的一行，双击】 --> 【将MySQL的bin目录路径追加到变值值中，用 ； 分割】

#4、初始化
mysqld --initialize-insecure

#5、启动MySQL服务
mysqld # 启动MySQL服务

#6、启动MySQL客户端并连接MySQL服务
mysql -u root -p # 连接MySQL服务器
复制代码

复制代码
上一步解决了一些问题，但不够彻底，因为在执行【mysqd】启动MySQL服务器时，当前终端会被hang住，那么做一下设置即可解决此问题：



注意：--install前，必须用mysql启动命令的绝对路径
# 制作MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --install

# 移除MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --remove



注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令：
# 启动MySQL服务
net start mysql

# 关闭MySQL服务
net stop mysql
```
#### 三、统一字符编码
```
#mysql5.5以上：修改方式有所改动
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

#2. 重启服务
#3. 查看修改结果：
\s
show variables like '%char%'
```
#### 四、初始sql语句
有了mysql这个数据库软件，就可以将程序猿从对数据的管理中解脱出来，专注于对程序逻辑的编写

mysql服务端软件即mysqld帮我们管理好文件夹以及文件，前提是作为使用者的我们，需要下载mysql的哭护短，或者其他模块来链接到mysqld，然后使用mysql软件规定的语法格式去提交自己命令，实现对文件夹或文件的管理。该语法即sql（Structured Query Language 即结构化查询语言）

###### sql语言分为3中类型：
+ 1、DDL语句 数据库定义语言：数据库、表、视图、索引、存储过程，例如：create drop alter
+ 2、DML语句 数据库操纵语言：插入数据insert、删除数据delete、更新数据update、查询数据select
+ 3、DCL语句 数据库控制语言：例如控制用户的访问权限grant、revoke

```
#1、操作文件夹
    增：create databases db1 charset utf8;
    查：show databases;
    改：alter databases db1 charset latin1;
    删：drop database db1;

#2、操作文件
    先切换到文件夹下 ：use db1;
      增：create table t1(id int,name char(20));
      删：drop table t1;
      改：alter table t1 modify name char(3);
      查：show tables

#3、操作文件中的内/记录
    增：insert into t1 values(1,'aaa'),(2,'bbb');
    查：select * from t1;
    改：updata t1 set name='ccc' where id=2;
    删：delete from t1 where id=1;
    清空表：
      delete from t1;#如果有自增id，新增的数据，仍然是删除前的最后一条为起始；
      truncate table t1; #数据量大，删除速度比上一条快，且直接从0开始
```
