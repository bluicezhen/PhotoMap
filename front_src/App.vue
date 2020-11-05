<template>
  <div id="app">
    <input type="file" id="input-upload">
    <router-view :key="$route.path"></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  methods: {
    upload () {
      alert('aaaaa')
    }
  }
}
</script>

<style lang="scss">
body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#input-upload {
  display: none;
}
</style>
