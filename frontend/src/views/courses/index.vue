
<template>

    <div v-if="apiData">

        <ul>
            <li v-for="course in apiData" :key="course.id">
                <p>Nome do curso: {{ course.title }}</p><p>Link: {{ course.slug }}</p>
            </li>
        </ul>

    </div>

    <div v-else>Nenhum curso encontrado</div>

</template>

<script>
import { getAPI } from '@/helpers/axios-api'


export default {
  data() {
    return {
      apiData: []
    }
  },
  mounted() {
    getAPI.get('courses/?format=json')
    .then(res => {

      this.apiData = res.data.results
      console.log('Courses API has received data: '+ this.apiData)

    })

    .catch(err => {
      console.log('erro get courses API: ' + err)
    })
  }
}
</script>