<script setup>
    import Navbar from './components/partials/navbar.vue';
</script>

<template>

    <Navbar></Navbar>

    <main class="container mt-4" id="app">

        <!-- <RouterLink to="/">Início</RouterLink> -->
        <RouterView></RouterView>

    </main> 

</template>

<style>

</style>


