import Vue from 'vue'
import Banner from '@/components/Banner'

describe('Banner.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Banner)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.hello h1').textContent)
      .toEqual('Welcome to Swarm AF')
  })
})
