<script setup>
    import { RouterView } from 'vue-router';
    import Navbar from './components/partials/navbar.vue';
</script>

<template>

    <Navbar></Navbar>

    <main class="container mt-4">

        <RouterLink to="/">Início</RouterLink>
        <RouterView></RouterView>

    </main>

</template>


