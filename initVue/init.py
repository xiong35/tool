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

os.mkdir('assets')
os.mkdir('components')
os.mkdir('components/common')
os.mkdir('components/content')
os.mkdir('network')
os.mkdir('routers')
os.mkdir('store')
os.mkdir('views')
os.mkdir('common')

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

os.system('cnpm install vue bootstrap-vue vue-router font-awesome axios vuex --save')

print("installed packages")

print('done!')