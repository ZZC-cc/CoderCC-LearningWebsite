// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import setting  from "./setting";
import axios  from "axios";

axios.defaults.withCredentials = false
Vue.prototype.$axios = axios; // 把对象挂载vue中
Vue.config.productionTip = false

Vue.prototype.$setting = setting;

// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/static/css/reset.css'

// 调用插件
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
