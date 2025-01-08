<script setup>
import Index from './components/courses/index.vue'
</script>

<template>
  <header>

    <div>
      <Index></Index>
    </div>
  </header>

</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>



<!-- 

<template>

    <div id="app">

        <h1>Courses t</h1>
        <router-view></router-view>

    </div>

</template>

<script>

export default {
    name: 'app',
}

</script> -->


