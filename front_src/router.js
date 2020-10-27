import Vue from 'vue'
import VueRouter from 'vue-router'

import loginView from './views/login_view/index.vue'
import homepageView from './views/homepage_view/index.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'homepage',
    component: homepageView
  },
  {
    path: '/login',
    name: 'login',
    component: loginView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
