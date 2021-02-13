<template>
  <div class="app-container">
    <nav class="tabbar">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import 'assets/app.css';
</style>
