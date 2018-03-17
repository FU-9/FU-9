nvm介绍
nvm（Node版本管理器），用它可以方便的在机器上安装并维护多个Node的版本；

在Ubuntu服务器中先安装nvm，在这里我通过wget方式进行安装
nvm github地址（https://github.com/creationix/nvm/blob/master/README.md）
执行以下命令进行安装nvm
```
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
```
安装完成之后可以通过`nvm ls-remote`来查看可以安装那些node版本
####可能遇到的问题
安装完后，如果是用xshell连远程主机的话，先重连一次，不然会发现提示找不到nvm命令
```
source ~/.bashrc
```
可能出现依旧提示找不到nvm命令，那么请使用source命令，如下

安装node
```
nvm install v8.9.0
```
通过`node -v`查看是否安装成功

nvm安装多个node版本
`nvm ls`查看已安装node的版本
使用`nvm use v8.9.0`切换版本
`nvm current`查看当前node版本
使用`nvm alias default <version>`来指定一个node版本
