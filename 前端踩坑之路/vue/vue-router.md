#### Vue-Router
vue-router是官方提供给我们基于vue实现单页应用进行路由跳转处理的一套解决方案
#### 安装
```
npm install vue-router --save
```
#### 详细方法
用Vue.js+vue-router创建单页应用，是非常简单的。使用Vue.js时，我们就已经把组件组合成一个应用了，当你要把vue-router加进来，只需要配置组件和路由映射，然后告诉vue-router在哪里渲染它们。
`组件 -> 路由 -> 渲染位置`
```
//app.vue
<template>
  <div id="app">
    <router-link to="/foo"></router-link>
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App'
}
</script>
//mian.js
import Vue from 'vue'
import App from './App'
import router from './router'
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
//router/index.js
import Vue from 'vue'
import Router from 'vue-router'
import {indexPage,contentPage,listPage} from '@/page'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: indexPage
    },{
      path: '/content',
      name: 'Content',
      component: contentPage
    },{
      path: '/list',
      name: 'List',
      component: listPage
    }
  ]
})
```
#### 动态路由匹配
我们经常需要把某种模式匹配到的所有路由，全部映射到同个组件，例如：我们有一个User组件，对于所有ID个不相同的用户，都要使用这个组件来渲染。那么，我们可以在vue-router的路由路径中使用动态路径参数来达到这个效果。
```
const User = {
  template:"<div>User</div>"
}

const router = new VueRouter({
    router:[
      {path:"/user/:id",component:User}
    ]
  })
```
一个路由中可以设置多段路径参数，对应的值都会设置到route.params。除了route.params外，route对象还提供了其他有用的信息，例如route.query,router.hash等。当使用路由参数是，组件实例会被复用，这就意味着组件的生命周期钩子不会再被调用。如果想对相应，可以简单的watch
```
const User = {
  template:"...",
  watch:{
    '$route'(to,from){

    }
  }
}

```
##### 嵌套路由
```
const router = new VueRouter({
    router:[
      {
        path:'/user/:id',
        component:user,
        children:[
          {
            path:'profile',
            component:UserProfile
          },
          {
            path:'posts',
            component:UserPosts
          }
        ]
      }
    ]
  })
```
要注意，以/开头的嵌套路径会被当作根路径。这让你充分的使用嵌套组件而无须设置嵌套的路径。
#### 编程式导航
除了使用创建a标签来定义导航链接，我们还可以借助router的实例方法，通过编写代码来实现。
###### router.push()
这种方法会向history栈中添加记录
```
//字符串
router.push('home')
//对象
router.push({path:'home'})
//命名的路由
router.push({name:'user',params:{userId:123}})
//带查询参数，编程/register?plan=private
router.push({path:'register'},query:{plan:'private'})
```
###### router.go()
这个方法的参数是一个整数，意思实在history记录中向前后者后台多少步，类似window.history.go(n)

#### 命名路由
主要是为了通过一个名称来表示一个路由显得更方便一些
```
const router = new VueRouter({
    routes:[
      {
        path:"/user/:userId",
        name:"user",
        component:User
      }
    ]
  })
```
#### 命名视图
如果想同时展示多个视图
```
<router-view class="view one"></router-view>
<router-view class="view one" name="a tow"></router-view>
<router-view class="view one" name="b three"></router-view>

const router = new VueRouter({
    routes:[
      {
        path:'/',
        components:{
          default:Foo,
          a:Bar,
          b:Baz
        }
      }
    ]
  })
```
#### 重定向
```
const router = new VueRouter({
    routes:[
      {
        path:"/a",
        redirect:"/b"
      }
    ]
  })
```
重定向的目标也可以是一个命名的路由
```
const router = new VueRouter({
    routes:[
      {
        path:"/a",redirect:{name:'foo'}
      }
    ]
  })
```
甚至是一个方法
```
const router = new VueRouter({
    routes:[
      {
        path:'/a',
        redirect:to=>{
            //方法接收目标路由作为参数
            //return重定向的 字符串路径/路径对象
        }
      }
    ]
  })
```

#### 别名
/a的别名是/b，意味着，当用户访问/b时，URL会保持为/b,但是路由匹配则为/a，就像用户直接访问/a一样。
```
const router = new VueRouter({
    routes:[
      {path:'/a',component:A,alias:'/b'}
    ]
  })
```
#### HTML5 History模式
使用history模式时，URL就是正常的url
```
const router = new VueRouter({
    mode:"history",
    routes:[...]
  })
```
#### 导航钩子
正如其名，vue-router提供的导航钩子主要用来拦截导航，让他完成跳转或取消。有多种方式可以在路由导航发生时执行钩子：全聚德，，当个路由独享的，或者组件级的。
全局钩子
```
const router = new VueRouter({...})
router.beforeEach((to,from,next)=>{
  //...
  })
每个钩子方法接收三个参数：
to：即将要进入的目标路由对象
from：当前导航正要离开的路由
next:Function:一定要调用该方法来resolve这个钩子。执行效果以来next方法的调用函数
    next():进行管道中的下一个钩子。如果全部钩子执行完了，则导航的状态就是confirmed（确认的）
    next(false)：终端当前的导航。如果浏览器的URL改变了（可能是用户手动或者浏览器后退按钮），那么URL低至会重置到from路由对应的地址。
    next('/')或者next({path:"/"}):跳转到一个不同的地址。当前的导航被中断，然后进行一个新的导航。
确保要调用next方法，否则钩子不会被resolved
```
某个路由独享的钩子
```
const router = new VueRouter({
    routes:[
      {
        path:"/foo",
        component:Foo,
        beforeEach:(to,from,next)=>{
          //...
        }
      }
    ]
  })
```
组件内的钩子
```
const Foo = {
  template: `...`,
  beforeRouteEnter (to, from, next) {
    // 在渲染该组件的对应路由被 confirm 前调用
    // 不！能！获取组件实例 `this`
    // 因为当钩子执行前，组件实例还没被创建
  },
  beforeRouteUpdate (to, from, next) {
    // 在当前路由改变，但是改组件被复用时调用
    // 举例来说，对于一个带有动态参数的路径 /foo/:id，在 /foo/1 和 /foo/2 之间跳转的时候，
    // 由于会渲染同样的 Foo 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。
    // 可以访问组件实例 `this`
  },
  beforeRouteLeave (to, from, next) {
    // 导航离开该组件的对应路由时调用
    // 可以访问组件实例 `this`
  }
}
```
#### 数据获取
有时候，进入某个路由后，需要从服务器获取数据。例如，在渲染用户信息时，你需要从服务器获取用户的数据，我们可以通过两种方式来实现：
1.导航完成之后获取：先完成导航，然后在接下来的组件生命周期钩子中获取数据，在数据获取期间显示加载中的指示。
2.导航完成之前获取：导航完成前，在路由的enter钩子中获取数据，在数据获取成功后执行导航。
###### 导航完成后获取数据
当你使用这种方式时，我们会马上导航和渲染组件，然后在组件的created钩子中获取数据。这让我们有机会再数据获取期间展示一个loading状态，还可以在不同视图间展示不同的loading状态。
```
<template>
  <div class="post">
    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="post" class="content">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>  

export default {
    data() {
        return {
            loading: false,
            post: null,
            error: null
        }
    },
    created() {
        // 组件创建完后获取数据，
        // 此时data已经被observed了
        this.fetchData()
    },
    watch: {
        // 如果路由有变化，会再次执行该方法
        '$route': 'fetchData'
    },
    methods: {
        this.error = this.post =null
        this.loading =true
        // replace getPost with your data fetching util/API wrapper
        getPost(this.$route.params.id, (err ,post) => {
            this.loading = false
            if(err) {
                this.error = err.toString()
            } else {
                this.post = post
            }
        })
    }
}
```
###### 在导航完成前获取数据
```
export default {
  data () {
    return {
      post: null,
      error: null
    }
  },
  beforeRouteEnter (to, from, next) {
    getPost(to.params.id, (err, post) =>
      if (err) {
        // display some global error message
        next(false)
      } else {
        next(vm => {
          vm.post = post
        })
      }
    })
  },
  // 路由改变前，组件就已经渲染完了
  // 逻辑稍稍不同
  watch: {
    $route () {
      this.post = null
      getPost(this.$route.params.id, (err, post) => {
        if (err) {
          this.error = err.toString()
        } else {
          this.post = post
        }
      })
    }
  }
}
```
