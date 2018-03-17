## <br>常用命令
ls    显示文件或目录 <br>
    -l 列出文件详细信息（list）<br>
    -a 列出当前目录下所有文件及目录，包括以.开头的隐含文件<br>

mkdir    创建目录<br>
    -p 创建目录， 若无父目录，则创建p（parent）

cd         切换目录<br>
touch    创建空文件<br>
echo     创建带有内容的文件<br>
cat        查看文件内容<br>
cp         拷贝<br>
mv        移动或重命名<br>
rm　     删除文件<br>
    -r       递归删除，可删除子目录及文件<br>
    -f       强制删除<br>
find       在文件系统中搜索某文件<br>
wc         统计文本中行数 字数 字符数<br>
grep      在文本文件中查找某个字符串<br>
rmdir      删除空目录<br>
tree        树形结构显示目录，需要安装tree包<br>
pwd        显示当前目录<br>
ln            创建链接文件<br>
more less 分页显示文本文件内容<br>
head tail  显示文件头 尾 内容<br>

## 系统管理命令
stat          显示指定文件的详细信息，比ls更详细<br>
who         显示在线登录用户<br>
whoami   显示当前操作用户<br>
hostname 显示主机名<br>
uname     显示系统信息<br>
top            动态显示当前耗费资源最多进程信息<br>
ps             显示顺吉娜进程状态 ps -aux<br>
du             查看目录大小 du -h /home 带有单位显示的目录信息<br>
df              查看磁盘大小 df -h 带有单位的显示磁盘信息<br>
ifconfig      查看网络情况<br>
ping           测试网络联通<br>
netstat       显示网络状态信息<br>
man           查看命令用法，命令不会用了，找男人 如：man ls<br>
clear          清屏<br>
alias            对命令重命名alias showmeit="ps -aux"，另外解除使用 unaliax showmeit<br><br>
kill               杀死进程，可以先用ps或top查看进程的id，然后在用kill命令杀死进程

## 打包压缩相关命令
gzip：<br>
bzip:<br>
tar:        打包压缩<br>
    -c      归档文件<br>
    -x      压缩文件<br>
    -z      gzip压缩文件<br>
    -j       bzip2压缩文件<br>
    -v      显示压缩或解压缩过程<br>
    -f       使用档名<br>

## 关机／重启机器<br>
shutdown<br>
      -r        关机重启<br>
      -h        关机不重启<br>
      now     立刻关机<br>
halt            关机<br>
reboot        重启<br>

## Linux管道
将一个命令的标准输出作为另一个命令的标准输入。也就是把几个命令组合起来使用，后一个命令除以前一个命令的结果
例：<br>grep -r "close" /ho：me/*  |  more
在home目录下所有文件中查找，包括close的文件，并分页输出

## Vim使用
vim三种模式：命令模式 插入模式 编辑模式。 <br>
使用ESC或i或：来切换模式
命令模式下：<br>
:q      退出<br>
:q!     强制退出<br>
:wq    保存并退出<br>
:set number 显示行号<br>
:set nonumber 隐藏行号<br>
/apache   在文档中查找apache 按n 跳到下一个，shift+n上一个<br>
yyp      复制光标所在行，并粘贴<br>
h左移一个字符 j下一行 k上一行 l右移一个字符<br>
