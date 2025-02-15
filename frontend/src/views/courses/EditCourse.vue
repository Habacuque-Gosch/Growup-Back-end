<template>

    <h1>Editar Course</h1>
    <br>
    <p>aaa {{ courseData }}</p>
    <form @submit.prevent="editCourse" class="form-control row g-2 pt-4 pb-4">

        <label class="form-label">Titulo</label>
        <input type="text" placeholder="Titulo do curso" v-model="editCourseData.title" value="" required style="height: 60px; border-radius: 5px;">
        <br>
        <label class="form-label">Slug</label>
        <input type="text" placeholder="Slug do curso" v-model="editCourseData.slug" value="" required style="height: 60px; border-radius: 5px;">

        <label class="form-label">Creation</label>
        <input type="date" placeholder="Slug do curso" v-model="editCourseData.creation" value="" required style="height: 60px; border-radius: 5px;">

        <button class="btn btn-success mt-4">Salvar alterações</button>
        <br>
        <p v-if="errorMessage" class="alert alert-danger" role="alert">{{ errorMessage }}</p>

    </form>

</template>

<script>
import { ref } from 'vue';
import { baseAPI } from '@/api/axios_api'
import { useRouter, useRoute } from 'vue-router';

export default {
    setup(){

        const editCourseData = ref({title: '', slug: '', creation: ''})
        const errorMessage = ref('')
        const courseRoute = useRoute()
        const router = useRouter()
        const courseId = courseRoute.params.id
        
        var courseData = ''

        const editCourse = async () => {
            try {

                let config = {
                    headers: {
                        Authorization: 'Token c2ef737289fabeae006a6b01c9ecb40aa088d046',
                    }
                }
                await baseAPI.put(`courses/${courseId}/`, editCourseData.value, config)
                // console.log('requestss: ')
                router.push({ name: 'index'})

            }
            
            catch (error) {
                console.log(`ERRO AO EDITAR O CURSO: ${error}`)
                errorMessage.value = `Erro ao editar o curso`
            }
        }

        courseData = baseAPI.get(`courses/${courseId}/`)
        .then(course => {
            courseData = course.data
            console.log(courseData)
            // router.push({name: 'edit_course', params: {id: courseId}})
            return courseData
        })
        .catch(error => {
            errorMessage.value = 'Curso inexistente'
            console.log('error: ', error)
            router.push({name: 'index'})
        })

        return {
            editCourseData,
            errorMessage,
            editCourse,
            courseData
        }
    }
}

</script>