
<template>
  <div>
    <p>Courses</p>

    <p>{{ courses }}</p>

    <ul>
      <li v-for="course in courses" :key="course.id">
        <p>{{ course.title }} - {{ course.slug }}</p>
      </li>
    </ul>

  </div>
</template>

<script>

  import axios from 'axios'

  export default {
    data() {
      return {
        courses: []
      }

    },
    mounted() {
      axios.get('http://127.0.0.1:8000/api/v1/courses/?format=json')
        .then((response) => {
          this.courses = response.data
          console.log('data queryset app:' + this.courses)
        }).catch((err) =>{
          console.log('Erro app: ' + err)
        })
    }
  }

</script>



<!-- TEMPLATE
<template>
  <div>
    <p>cursos</p>

    <ul>
      <li v-for="course in courses" :key="course.id">
        <p>{{ course.title }} - {{ course.slug }}</p>
        <p>{{ courses }}</p>
      </li>
    </ul>

  </div>
</template>
<script>


  import { ref, onMouted } from 'vue'
  import axios from 'axios'
  // import { useRouter } from 'vue-router'

  export default {
    setup() {

      const courses = ref([])
      
      const ListAllCourses = async () => {

        try {

          const response = await axios.get('http://127.0.0.1:8000/api/v1/courses/?format=json')
          courses.value = response.data
          console.log('data queryset app:' + courses)

        } catch(error) {
          console.log('Erro app: ' + error)
        }
          
      }

      // onMouted(ListAllCourses)
      return courses

    }
  }

</script> -->