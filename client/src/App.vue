<template>
  <div id="app">
    <div>
      <h1>{{ bannerMsg }}</h1>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: () => ({ bannerMsg: 'Welcome to Swarm AF' })
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1 {
  font-weight: normal;
}
</style>
