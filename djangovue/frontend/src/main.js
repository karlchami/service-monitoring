// All global imports go here
import 'babel-polyfill'
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store'
import Vuex from 'vuex'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.devtools = true
Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(Vuetify)

/* eslint-disable no-new */
new Vue({
  vuetify: new Vuetify({
    icons: {
      iconfont: 'md'
    }
  }),
  store,
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
