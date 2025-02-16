<script setup>
    import Navbar from './components/partials/navbar.vue';
    import Notifications from './components/partials/notifications.vue';
</script>

<template>
    <Navbar></Navbar>
    <Notifications></Notifications>
    <main class="container mt-4" id="app">

        <!-- <RouterLink to="/">Início</RouterLink> -->
        <RouterView></RouterView>

    </main> 

</template>

<style>

</style>


