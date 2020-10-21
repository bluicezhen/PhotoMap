<template>
  <div id="app">
    <button @click="upload">dsdd</button>
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
