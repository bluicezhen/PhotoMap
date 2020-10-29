import App from './App.vue'
import ElementUI from 'element-ui'
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import backend from './tools/backend'
import router from './router.js'
import langEn from './lang/en'
import langZh from './lang/zh'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.use(VueI18n)

const messages = {
  en: langEn,
  zh: langZh
}
const i18n = new VueI18n({
  locale: navigator.language,
  messages
})

Vue.config.productionTip = false
Vue.prototype.$backend = backend

new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount('#app')
