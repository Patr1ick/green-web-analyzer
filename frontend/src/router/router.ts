import { createRouter, createWebHistory } from "vue-router"
import MainPage from '../view/MainPage.vue'
import ResultsPage from '../view/ResultsPage.vue'
import RequestPage from '../view/RequestPage.vue'
import SearchPage from '../view/SearchPage.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: MainPage
        },{
            path: '/request',
            component: RequestPage
        }, 
        {
            path: '/results',
            component: ResultsPage
        },
        {
            path: '/search',
            component: SearchPage
        }
    ]
});

export default router;