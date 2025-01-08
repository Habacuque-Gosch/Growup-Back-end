import { createRouter, createWebHistory } from 'vue-router'
import ListCourses from '../components/courses/index.vue'


const routes = [
    {
        path: '/',
        name: 'index',
        component: ListCourses,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router