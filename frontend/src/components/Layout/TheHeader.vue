<template>
    <header class="flex flex-col md:flex-row justify-between content-center px-8 py-4 bg-zinc-900">
        <RouterLink to="/" class="flex flex-col md:flex-row items-center hover:no-underline">
            <img src="/green-web-analyzer.svg" class="m-2 w-12" />
            <h1 class="text-gray-200 m-2 text-center hidden lg:block">Green Web Analyzer</h1>
        </RouterLink>
        <div class="flex justify-between content-center flex-col md:flex-row flex-wrap p-4 m-auto md:ml-auto md:mr-0">
            <TheThemeSwitch />
            <nav class="flex flex-wrap justify-between content-center mx-4">
                <RouterLink to="/about" :class="aboutClasses">
                    About
                </RouterLink>
                <RouterLink to="/results" :class="resultsClasses">
                    Results
                </RouterLink>
                <RouterLink to="/search" :class="searchClasses">
                    Search
                </RouterLink>
            </nav>
        </div>
    </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TheThemeSwitch from './TheThemeSwitch.vue';

export default defineComponent({
    computed: {
        resultsClasses() {
            return {
                "btn-nav sm:w-auto": true,
                "border-emerald-800": this.$router.currentRoute.value.path == '/results',
            }
        },
        aboutClasses() {
            return {
                "btn-nav sm:w-auto": true,
                "border-emerald-800": this.$router.currentRoute.value.path == '/about',
            }
        },
        searchClasses() {
            return {
                "btn-nav sm:w-auto": true,
                "border-emerald-800": this.$router.currentRoute.value.path == '/search',
            }
        }
    },
    components: {
        TheThemeSwitch
    }
})
</script>