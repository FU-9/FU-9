1、active-class是那个组件的属性？嵌套路由怎么定义？
```
答：vue-router模块的router-link的组件
```
2、怎么定义vue-router的动态路由？怎么获取传过来的动态参数？
```
答：在router目录下的index.js文件中，对path属性加上/:id。使用router对象的params.id来获取
```
3、vue-router有哪几种导航钩子？
```
答：三种
    1、一种是全局导航钩子：router.beforeEach(to,from,next),作用：跳转前进行判断拦截
    2、组件内的钩子
    3、单独路由独享组件
```
4、v-model是什么？怎么使用？vue中标签怎么绑定事件？
```
答：可以实现双向绑定，指令（v-class、v-for、v-if、v-show、v-on）。
vue的model层的属性。绑定事件：<div @click="doLog()"/>
```
5、vuex是什么？怎么使用？哪种功能场景使用它？
[vuex详细使用方法]()
```
答：vue框架中的状态管理。在main.js引入store，注入。
新建了一个目录store，。。。export。
场景有：单页应用中，组件之间的状态。音乐播放、登录状态。。。
```
6、mvvm框架是什么？它和其它框架（jquery）的区别是什么？那些场景适合？
```
答：一个model+view+viewmodel框架，数据模型model，viewmodel链接model与view
区别：vue数据驱动，通过数据来显示视图层而不是节点操作。
场景：数据操作比较多的场景，更加便捷
```
7、vue-router是什么？它有那些组件？
[vue-router详细使用方法]()
```
答：vue用来写路由的一个插件。router-link、router-view
```
8、vue的双向数据绑定原理是什么？
```
答：vue.js是采用数据劫持结合发布者-订阅者模式的方式，通过object.defineProperty()来劫持各个属性的setter，geeter,在数据变动时发布消息给订阅者，触发相应的监听回调
具体步骤：
1、需要observe的数据对象进行递归遍历，包括子属性对象的属性，都加上setter和getter这样的话，给这个对象的某个值赋值，就会触发setter，那么就能监听到了数据变化
2、compile解析模板指令，将模板中的变量替换成数据，然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者，一旦数据有变动，收到通知，更新视图
3、watcher订阅者是observer和compile之间通信的桥梁，主要做的事情是：
3.1、在自身实例化时往属性订阅器(dep)里面添加自己
3.2、自身必须要有一个update方法
3.3、待属性变动dep.notice()通知时，能调用自身的update()方法，并触发compile中绑定的回调，则功成身退。
4、MVVM作为数据绑定的入口，整合observer、compile和watcher三者，通过observer来监听自己的model数据变化，通过compile来接卸变异模板指令，最终利用watcher搭起observer和compile之间的通信桥梁，达到数据变化-> 视图更新；视图交互变化->数据model变更的双向绑定效果
```
9、请详细说下你对vue生命周期的理解？
```
答：总共年份为8个阶段：创建前/后、载入前/后、更新前/后、销毁前/后
创建前/后：在beforeCreated阶段，vue实例的挂在元素$el和数据对象data都为undefined，还未初始化。在created阶段，vue实例的数据对象data有了，$el还没有。
载入前/后：在beforeMount阶段，vue实例的$el和data都初始化了,但还是挂载之前为虚拟的dom节点，data.message还未替换。在mounted阶段，vue实例挂载完成，data.message成功渲染
更新前/后：当data变化时，会触发beforeUpdate和updated方法。
销毁前/后：在执行destroy方法后，对data的改变不会再触发周期函数，说明此时vue实例已经解除了事件监听以及和dom的绑定，但是dom结构依然存在
```
10、vue常用指令 及 用法
```
v-if：判断是否隐藏；v-for：数据循环出来；v-bind:class：绑定一个属性；v-model：实现双向绑定
```
11、vuex得属性
```
 State、 Getter、Mutation 、Action、 Module
```
12、vuex的mutation特性
```
一、Action 类似于 mutation，不同在于：
二、Action 提交的是 mutation，而不是直接变更状态。
三、Action 可以包含任意异步操作
```
13、用vue进行开发的优点
```
低耦合。视图（View）可以独立于Model变化和修改，一个ViewModel可以绑定到不同的"View"上，当View变化的时候Model可以不变，当Model变化的时候View也可以不变。
可重用性。你可以把一些视图逻辑放在一个ViewModel里面，让很多view重用这段视图逻辑。
独立开发。开发人员可以专注于业务逻辑和数据的开发（ViewModel），设计人员可以专注于页面设计，使用Expression Blend可以很容易设计界面并生成xml代码。
可测试。界面素来是比较难于测试的，而现在测试可以针对ViewModel来写
```
