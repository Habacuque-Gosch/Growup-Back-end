import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/user/home/index.vue'
import Login from '../views/user/login/login.vue'
import Register from '../views/user/register/register.vue'




const routes = [

    // ROUTERS USERS
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

    // {
    //     path: '/category',
    //     name: 'category',
    //     component: Category,
    //     children: [
    //         {
    //            path: 'subcategory',
    //            name: 'subCategory',
    //            component: ChildComponent,
    //         },
    //         // other nested routes
    //     ]
    // },

    // ROUTERS COURSES
    {
        path: '/index',
        name: 'index',
        component: () => import('../views/courses/Index.vue'),
    },
    {
        path: '/course/details/:id/',
        name: 'course_details',
        component: () => import('../views/courses/DetailsCourse.vue'),
    },
    {
        path: '/course/add-course/',
        name: 'add_course',
        component: () => import('../views/courses/AddCourse.vue')
    },
    {
        path: '/course/edit-course/:id/',
        name: 'edit_course',
        component: () => import('../views/courses/EditCourse.vue'),
    },
    {
        path: '/course/delete-course/:id/',
        name: 'delete_course',
        component: () => import('../views/courses/DeleteCourse.vue')
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router