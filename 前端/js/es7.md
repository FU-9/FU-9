#### 一堆废话，但还是要来一个开场白的
这篇文章是基于es6版本对es7新增以及修改的内容，做一次简要的总结，方便自己与看到这篇文章的有缘人来进行学习，方便我们快速开发
####  一、ES7新特性
es7在es6的基础上添加了三项内容：求幂运算符（**）、Array.prototype.includes()方法、函数作用域中严格模式的变更

##### Array.prototype.includes()方法
includes()的作用，是查找一个值在不在数组里，如果在呢他就返回true，不在呢就返回false。
```
['a','b','c'].includes('a')//true
['a','b','c'].includes('d')//false
```
includes方法接收两个参数：要搜索的值和搜索的开始索引。当第二个参数被传入时，该方法会从索引出开始往后搜索（默认索引为0）。若搜索的值在数组中找到的话返回true，反之false
```
['a','b','c','d'].includes('b',1)//true
['a','b','c','d'].includes('b',2)//false
```
有一个需要注意的点是，在判断+0与-0时，被认为是相同的
```
['+0','1'].includes(-0)//true
```
##### 求幂运算符（**）
基本用法
3**2    //9
效果同
Math.pow(3,2)   //9

##### 函数作用于严格模式下改动
在es6中仍然可以使用"use strict"指令来制定严格模式
es7中指出只有参数不包含解构或默认值的简单参数列表时才可以在函数中使用"use strict"
```
function func(arg1,arg2){
  "use strict"
  return arg1
}
//这里抛出语法错误
function func(arg1,arg2=arg1){
  "use strict"
  return arg1
}
```
