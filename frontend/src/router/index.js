import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import Home from '../components/user/home/index.vue'
import Login from '../components/user/login/login.vue'
import Register from '../components/user/register/register.vue'
import ListCourses from '../components/user/courses/index.vue'



const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
    },
    {
        path: '/user/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/user/register',
        name: 'register',
        component: Register,
    },
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