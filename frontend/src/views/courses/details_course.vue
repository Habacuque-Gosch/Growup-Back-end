<template>

    <h1>Course Details</h1>

    <div v-if="courseData">

        <p>Id: {{ courseData.id }}</p>
        <p>Nome: {{ courseData.title }}</p>
        <p>Slug: {{ courseData.slug }}</p>

    </div>

    <div v-else>Curso não encontrado</div>

</template>

<script setup>

    import {useRoute} from 'vue-router'

    const courseRouter = useRoute()

    const courseId = courseRouter.params

    console.log(courseId['id'])

</script>

<script>

    import { getAPI } from '@/api/axios_api'

    export default {
        data() {
            return {
                courseData: [],
            }
        },
        mounted() {
            getAPI.get(`courses/1?format=json`)
            .then(res => {

                this.courseData = res.data

                console.log('Courses API has received data: '+ this.courseData)

            })

            .catch(err => {
                console.log('erro get courses API: ' + err)
            })
        }
    }

</script>
