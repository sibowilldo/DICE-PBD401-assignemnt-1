import { createRouter, createWebHistory } from "vue-router";
import { authGuard } from "@auth0/auth0-vue";

const Auth0Callback = () => import("@/Pages/Errors/Auth0Callback.vue");
const CreateVacancy = () => import('@/Pages/Vacancy/CreateVacancy.vue')
const Vacancies = () => import('@/Pages/Vacancies.vue')
const Homepage = () => import('@/Pages/HomePage.vue')
const ProfilePage = () => import('@/Pages/Profile.vue')
const LoginPage = () => import('@/Pages/Auth/Login.vue')
const NotFoundPage = () => import('@/Pages/Errors/404.vue')

const routes = [
    {
        path: '/',
        name: 'home',
        component: Homepage,
    },
    {
        path: '/profile',
        name: 'profile',
        component: ProfilePage,
        beforeEnter: authGuard,
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage,
    },
    {
        path: '/vacancies',
        name: 'vacancies',
        component: Vacancies,
        beforeEnter: authGuard,
    },
    {
        path: '/vacancies/create',
        name: 'vacancies-create',
        component: CreateVacancy,
        beforeEnter: authGuard,
    },
    {
        path: '/callback',
        name: 'callback',
        component: Auth0Callback,
    },
    {
        path: "/:catchAll(.*)",
        name: "Not Found",
        component: NotFoundPage,
    },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router;