import App from './App.vue'
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import router from './router.js'
import langEn from './lang/en'
import langZh from './lang/zh'

const messages = {
  en: langEn,
  zh: langZh
}
Vue.use(VueI18n)
const i18n = new VueI18n({
  locale: 'zh-CN',
  messages
})

Vue.config.productionTip = false

new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount('#app')
