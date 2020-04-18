import os

projectName = input("enter project name: ")

os.system(f'vue create {projectName}')

print('started project')

os.chdir(projectName)

os.remove('src/components/HelloWorld.vue')
os.remove('src/assets/logo.png')
os.remove('README.md')

with open('src/App.vue', 'w') as fw:
    fw.write(
'''<template>
  <div id="app">
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
</style>
''')

print('removed helloworld')

os.mkdir('src/assets/img')
os.mkdir('src/components/common')
os.mkdir('src/components/content')
os.mkdir('src/network')
os.mkdir('src/routers')
os.mkdir('src/store')
os.mkdir('src/views')
os.mkdir('src/common')

print("made dirs")

with open('vue.config.js','w') as fw:
    fw.write('''
const path = require("path");

function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  chainWebpack: config => {
    config.resolve.alias
      .set("@", resolve("./src"))
      .set("components", resolve("./src/components"))
      .set("assets", resolve("./src/assets"))
      .set("common", resolve("./src/common"))
      .set("network", resolve("./src/network"))
      .set("views", resolve("./src/views"));
  }
};''')

print("created vue config")

with open('src/main.js','w') as fw:
    fw.write('''import Vue from "vue";
import App from "./App.vue";
import router from "./routers";

import "font-awesome/css/font-awesome.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = true;

new Vue({
  render: h => h(App),
  router
}).$mount("#app");
''')

print("changed main.js")

with open('src/routers/index.js','w') as fw:
    fw.write('''import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

const someRoute = () => import("views/someRoute/someRoute");

const routes = [
  {
    path: "",
    redirect: "/home"
  },
  {
    path: "/home",
    component: someRoute
  },
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
''')

print("create main router")

os.system('cnpm install vue bootstrap-vue vue-router font-awesome axios vuex --save')

print("installed packages")

print('done!')