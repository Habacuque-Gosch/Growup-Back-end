<template>

    <h1>Editar curso</h1>
    <br>
    <form @submit.prevent="editCourse" class="form-control row g-2 pt-4 pb-4">

        <label class="form-label">Titulo</label>
        <input type="text" placeholder="Titulo do curso" v-model="editCourseData.title" required style="height: 60px; border-radius: 5px;">
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
import { ref } from 'vue'
import { baseAPI } from '@/api/axios_api'
import { useRouter, useRoute } from 'vue-router';


export default {
    setup(){

        const editCourseData = ref({title: '', slug: '', creation: ''})
        const errorMessage = ref('')
        const courseRoute = useRoute()
        const router = useRouter()
        const courseId = courseRoute.params.id
        const DataCourseEdit = {
            id: '',
            title: '',
            slug: ''
        }

        const courseData = baseAPI.get(`v2/courses/${courseId}/`)
        .then(course => {
            DataCourseEdit.id = course.data.id
            DataCourseEdit.title = course.data.title
            DataCourseEdit.slug = course.data.slug
            return {DataCourseEdit}
        })
        .catch(error => {
            errorMessage.value = 'Curso inexistente'
            console.log('error: ', error)
            router.push({name: 'index'})
        })

        const editCourse = async () => {
            try {

                if(editCourseData.value.slug.toString() == DataCourseEdit.slug.toString()){
                    console.log(editCourseData.value.slug, DataCourseEdit.slug)
                    errorMessage.value = 'Esse slug já está atribuído a outro curso'
                } else {

                    let config = {
                        headers: {
                            Authorization: 'Token c2ef737289fabeae006a6b01c9ecb40aa088d046',
                        }
                    }
                    await baseAPI.put(`v2/courses/${courseId}/`, editCourseData.value, config)
                    // console.log('requestss: ')
                    router.push({ name: 'index'})
                }
            }
            
            catch (error) {
                console.log(`ERRO AO EDITAR O CURSO: ${error}`)
                errorMessage.value = `Erro ao editar o curso`
            }
        }
        
        return {
            editCourseData,
            errorMessage,
            editCourse,
            DataCourseEdit
        }
    }
}

</script>