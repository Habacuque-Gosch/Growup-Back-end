import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import ListCourses from '../components/courses/index.vue'


const routes = [
    {
        path: '/index',
        name: 'index',
        component: ListCourses,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router