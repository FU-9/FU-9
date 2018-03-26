#### 什么是vuex？
>vuex是一个专门为vue.js设计的集中式状态管理架构。状态？我把它理解为在data中的属性需要共享给其他vue组件使用的部分。就叫做状态。简单地说就是data中需要公用的属性。

#### 引入Vuex（前提是已经用Vue脚手架工具构建好项目）
1、利用npm包管理工具，进行安装vuex。在控制命令行输入下边的命令就可以了
```
npm isntall vuex --save
```
2、新建一个store的文件夹（不是必须的），并在文件夹下新建store.js文件，文件中引入我们的vue和vuex
```
import Vue from 'vue';
import Vuex from 'vuex';
```
3、使用我们的vuex，引入之后用Vue.use进行引用
```
Vue.use(Vuex)
```
4、在mian.js中引入新建的vuex文件
```
import storeConfig from './vuex/store';
```
5、在然后，在实例化Vue对象是加入store对象：
```
new Vue({
    el:"#app",
    router,
    store,
    template:"<App/>",
    components:{App}
  })
```
##### 初出茅庐 来个DEMO
1、现在我们store.js文件里增加一个常量对象。sotre.js文件就是我们在引入vuex时的那个
```
const state = {
  count:1
}
```
2、用export default封装代码，让外部可以引用。
```
export default new Vuex.Store({
    state
  })
```
3、新建一个vue的模板，位置在components问佳佳下，名字叫count.vue。在模板中我们引入我们刚新建的store.js文件，并在模板中用{{$store.state.count}}输出count的值
```
<template>
  <div>
    <h1>{{msg}}</h1>
    <h3>{{$store.state.count}}</h3>
  <div>
</template>
<script>
  import store form '@/vuex/store'
  export detault{
    data(){
      return {
        msg:"hello vuex"
      }
    },
    store
  }
</script>
```
4、在store.js文件中加入两个改变state的方法
```
const mutations = {
  add(state){
    state.count+=1
  },
  reduce(state){
    state.count-=1
  }
}
```
这里的mutations是固定的写法，意思是改变的，所以先不用着急，只知道我们要改变state的数值的方法，必须写在mutations里就可以了
5、在count.vue模板中加入两个按钮，并调用mutations中的方法
```
<div>
  <button @click="$store.commit('add')">+</button>
  <button @click="$store.commit('reduce')">-</button>
</div>
```
然后在store.js中定义的mutations放到到处的实例中
```
export default new Vuex.Store({
  state,mutations
  })
```
这样进行预览就可以实现对vuex中的count进行加减了
##### state访问状态对象
>const state,这个就是我们说的访问状态对象，它就是我们SPA（单页应用程序）中的共享值

学习状态对象赋值给内部对象，也就是把stroe.js中的值，赋值给我们模板里data中的值
###### 一、通过computed的计算属性直接赋值
computed属性可以在输出前，对data中的值进行改变，我们就利用这种特性把store.js中的state值赋值给我们模板中的data值。
```
computed:{
  count(){
    return this.$store.state.count;
  }
}
```
这里需要注意的是return this.$store.state.count这一句，一定要写this，要不你会找不到$store的。这种写法很好理解，但是写起来比较麻烦，那么来看第二种写法。
###### 二、通过mapState的对象来赋值
我们首先要用import引入mapState
```
import {mapState} from 'vuex'
```
然后在computed计算属性里写如下代码：
```
computed:mapState({
    count:state=>state.count
  })
```
###### 三、通过mapState的数组来赋值
```
computed:mapState(['count'])
```
这个算是最简单的写法了，在实际项目开发中也经常这样使用。
##### Mutations修改状态（$store.commit())
Vuex提供了commit方法来修改状态，我们粘贴出Demo示例代码内容，回顾一下，我们在button上修改的方法
```
<button @click="$store.commit('add')">+</button>
<button @click="$store.commit('reduce')">-</button>
```
store.js文件：
```
const mutations = {
  add(state){
    state.count+=1
  },
  reduce(state){
    state.count-=1
  }
}
```
传值：这只是一个最简单的修改状态的操作，在实际项目中我们常常需要在修改状态时传值，比如上边的例子，是我们每次只加1，而现在我们要通过所传的值进行相加。其实我们只需要在Mutations里再加上一个参数，在commit的时候传递就可以了。具体代码如下
store.js
```
const mutations = {
  add(state,n){
    state.count+=n
  },
  reduce(state){
    state.count-=1
  }
}
```
count.vue
```
<button @click="$store.commit('add',5)">+</button>
<button @click="$store.commit('reduce')">-</button>
```
##### 模板获取Mutations方法
实际开发中我们也不喜欢看到$store.commit()这样的方法出现，我们希望跟调用模板里的方法一样调用。
例如：@click="reduce"就和没引用vuex插件一样。要达到这种写法，只需要简单的两步就可以了
1、在模板count.vue里用import引入我们的mapMutations：
```
import {mapState,mapMutations} from 'vuex';
```
2、在模板的script里添加methods属性，并加入mapMutations
```
methods:mapMutations([
    'add','reduce'
  ])
```
通过上边两步，我们已经可以在末班中直接使用我们的reduce或者add方法了，就像下面这样
```
<button @click="reduce">-</button>
```

##### getters计算过滤操作
getter从表面是获得的意思，可以把他看做在获取数据之前进行的一种在编辑，相当于对数据的一个过滤和加工，可以看作store.js的计算属性
###### 基本用法
假如有这么一个需求，count在输出前，需要在原基础之上加上一个数字或拼成一段字符串，这时就可以使用这个getters属性了
```
const getters = {
  count:function(state){
    return state.count+=100;
  }
}
```
写好getters之后，我们还需要在Vuex.Store()里引入，由于之前我们已经引入了state和mutations，所以引入里有三个引入属性。代码如下：
```
export default new Vuex.Store({
  state,mutations,getters
  })
```
store.js就先可以告一段落了，我们需要到模板页对computed进行配置。在vue的构造器里边只能有一个computed属性，如果写多个，只有最后一个computed属性可用，所以要对上边写的computed属性进行一个改造。改造时我们使用ES6中的展开运算符'...'。
```
computed:{
  ...mapState(['count']),
  count(){
    return this.$store.getters.count;
  }
}
```
写完这些后，在每次count值发生变化的时候，都会进行加100的操作
###### 用mapGetters简化模板写法
我们都知道state和mutations都有map的引用方法把我们模板中的编码进行简化，我们的getters也是有的，代码如下。
老套路，先用import引入我们的mapGetters
```
import {mapState,mapMutations,mapGetters} from 'vuex';
```
在computed属性中加入mapGetters
```
...mapGetters(['count'])
```
##### module模块组
随着项目的复杂性增加，我们共享的状态越来越多，这时候我们就需要把我们状态的各种操作进行分组，分组后再进行按组编写。
###### 声明模块组
在vuex/store.js中声明模块组，我们还是用我们的const常量的方法声明模块组。代码如下：
```
const moduleA={
  state,mutations,getters,actions
}
```
声明好后，我们修改原来Vuex.Store里的值：
```
export default new Vuex.Store({
  modules:{a:"moduleA"}
  })
```
###### 在模板中使用
```
<h3>{{$store.state.a.count}}</h3>
```
简写方法同样适用
```
computed：{
  count(){
    return this.$store.state.a.count;
  }
}
```
