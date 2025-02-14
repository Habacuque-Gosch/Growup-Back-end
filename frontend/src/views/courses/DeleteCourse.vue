<template>

    <h1>Delete Course</h1>
    <br>
    <p v-if="errorMessage" class="alert alert-danger" role="alert">{{ errorMessage }}</p>

</template>

<script setup>


import { useRouter, useRoute } from 'vue-router'
import { baseAPI } from '@/api/axios_api'
import { ref, onMounted } from 'vue'

const courseRoute = useRoute()
const router = useRouter()
const errorMessage = ref('')

const courseId = courseRoute.params.id
console.log(courseId)

onMounted(()=> {
    baseAPI.get(`courses/${courseId}/`)
        .then(response => {

            console.log('data: ', response.data.title)

            let config = {
                headers: {
                    Authorization: 'Token c2ef737289fabeae006a6b01c9ecb40aa088d046',
                }
            }
            baseAPI.delete(`courses/${courseId}/`, config)
            // console.log('requestss: ')
            router.push({ name: 'index'})

        })

        .catch(error => {
            console.log(`ERRO AO DELETAR O CURSO: ${error}`)
            errorMessage.value = `Curso inexistente`
        })
})

</script>