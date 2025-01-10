<script setup>
  import { RouterView } from 'vue-router';
  import Index from './views/courses/index.vue'
  import Home from './views/user/home/index.vue'
</script>

<template>

  <main>

    <RouterView></RouterView>
    <RouterLink to="/">a</RouterLink>
    <br>
    <RouterLink to="/index">a</RouterLink>
    <br>
    <RouterLink to="/user/login">a</RouterLink>
    <br>
    <RouterLink to="/user/register">a</RouterLink>

  </main>

</template>


