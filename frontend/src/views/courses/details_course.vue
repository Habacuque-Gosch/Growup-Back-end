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

    import { useRouter, useRoute } from 'vue-router'
    import { getAPI } from '@/api/axios_api'
    import { ref, onMounted } from 'vue'

    // const courseRouter = useRouter()
    // const courseId = courseRouter.currentRoute.value.params.id
    const courseRoute = useRoute()
    const courseId = courseRoute.params.id

    console.log(courseId)

    const courseData = ref({})

    onMounted(()=> {
        getAPI.get(`courses/${courseId}?format=json`)
            .then(res => {

                courseData.value = res.data

                console.log('Courses API has received data')

            })

            .catch(err => {
                console.log('erro get courses API: ' + err)
            })
    })

</script>