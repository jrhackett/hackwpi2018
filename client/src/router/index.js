import Vue from 'vue'
import Router from 'vue-router'
import Banner from '@/components/Banner'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Banner',
      component: Banner
    }
  ]
})
