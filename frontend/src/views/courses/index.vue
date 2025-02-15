
<template>

    <h1>Bem vindo(a)</h1>
    <div>
        <form action="" class=" input-group mb-3 d-flex flex-row bd-highlight mb-3" method="POST">

            <input type="text" name="palavra" id="palavra" class="form-control" placeholder="Pesquise pelo título, categoria ou descrição de um post" aria-label="Recipient's username" aria-describedby="button-addon2" required>
            <button class="btn btn-outline-secondary" id="button-addon2">Buscar </button>

        </form>
    </div>
    <hr>

    <h2>Cursos</h2>

    <div v-if="apiData">

        <div class="card" v-for="course in apiData" :key="course.id">
            <div class="card-body">
                <RouterLink :to="{name: 'course_details', params: {id: course.id}}">Nome do curso: {{ course.title }}</RouterLink>
                <p>Link: {{ course.slug }}</p>
                <RouterLink :to="{name: 'course_details', params: {id: course.id}}" class="btn btn-success"><i class="bi bi-eye"></i>Ver curso</RouterLink>
                <RouterLink :to="{name: 'edit_course', params: {id: course.id}}" class="btn btn-primary"><i class="bi bi-pencil"></i>Editar curso</RouterLink>
                <RouterLink :to="{name: 'delete_course', params: {id: course.id}}" class="btn btn-danger"><i class="bi bi-trash"></i>Deletar curso</RouterLink>
                <RouterLink :to="{name: 'course_details', params: {id: course.id}}" class="btn btn-primary"><i class="bi bi-bookmark"></i>Salvar curso</RouterLink>
            </div>
        </div>

    </div>

    <div v-else>Nenhum curso encontrado</div>

</template>

<script>
    import { baseAPI } from '@/api/axios_api'

    export default {
        data() {
            return {
                apiData: [],
            }
        },
        mounted() {
            baseAPI.get('courses/?format=json')
            .then(res => {
                this.apiData = res.data.results
            })
            .catch(err => {
                console.log('erro get courses API: ' + err)
            })
        }
    }
</script>