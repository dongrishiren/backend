import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login.vue'
import regist from '../components/regist.vue'
import index from '../components/index.vue'
import business_detail from '../components/business_detail.vue'

Vue.use(Router);

export default new Router({
  mode:"history",
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path:'/regist',
      name: 'regist',
      component: regist
    },
    {
      path:'/index/:username',
      name: 'index',
      component: index
    },
    {
      path:'/business_detail/:username',
      name: 'business_detail',
      component: business_detail
    },
  ]
})
