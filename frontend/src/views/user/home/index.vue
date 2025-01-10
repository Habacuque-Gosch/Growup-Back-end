<script setup>
    import Index from '@/views/courses/index.vue';

</script>

<template>

    <main>

        <h1>Bem vindo(a)</h1>
        <div>
            <form action="" class=" input-group mb-3 d-flex flex-row bd-highlight mb-3" method="POST">

                <input type="text" name="palavra" id="palavra" class="form-control" placeholder="Pesquise pelo título, categoria ou descrição de um post" aria-label="Recipient's username" aria-describedby="button-addon2" required>
                <button class="btn btn-outline-secondary" id="button-addon2">Buscar </button>

            </form>
        </div>
        <hr>

    </main>

    <h2>Cursos</h2>

    <index></index>

</template>












