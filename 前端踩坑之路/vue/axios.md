#### 什么是axios？
axios是基于http客户端的promise，面向浏览器和nodejs

#### 特点
+ 浏览器端发起XMLHttpRequests请求
+ node端发起http请求
+ 支持Promise API
+ 监听请求和返回
+ 转换请求和返回
+ 取消请求
+ 自动转化json数据
+ 客户端支持抵御

#### 安装
使用npm
```
npm i axios
```
使用bower
```
bower install axios
```
使用cdn
```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```
#### 示例
发起一个`GET`请求
```
//发起一个user请求，参数为给定的ID
axios.get('/user?ID=4399')
.then(function(response){
  console.log(response);
  })
.catch(function(error){
  console.log(error);
  })
//上边的请求也可选择下面的方式来写
axios.get('/user',{
    params:{
      ID:4399
    }
  })
.then(function(response){
    console.log(response);
  })
.catch(function(error){
  console.log(error)
  })
```
发起一个`POST`请求
```
axios.post('/user',{
    firstName:"frient",
    lastName:"Flintstone"
  })
.then(function(response){
  console.log(response)
  })
.catch(function(error){
  console.log(error)
  })
```
发起一个多重并发请求
```
function getUserAccount(){
  return axios.get('user/4399')
}
function getUserPermissions(){
  return axios.get('/user/4399/permissions')
}
axios.all([getUserAccount(),getUserPermissions()])
.then(function(acc,pers){
    //两个请求现在都完成
  })
```
#### axios API
`axios`能够在进行请求时进行一些设置。
axios(config)
```
//发起post请求
axios({
    methods:'post',
    url:'/user/4399',
    data:{
      firstName:"Fred",
      lastName:"Flintstone"
    }
  });

```
##### 请求方法的重命名
为了方便，axios提供了所有请求方法的重命名
axios.request(config)
axios.get(url[,config])
axios.delete(url[,config])
axios.head(url[,config])
axios.post(url[,data[,config]])
axios.put(url[,data[,config]])
axios.patch(url[,data[,config]])
##### 注意
当使用重命名方法时`url`、`methods`，以及`data`不需要在config里配置
