<template>
    <header class="grid grid-cols-1 md:grid-cols-2 gap-4 justify-start items-center p-8 bg-zinc-900">
        <RouterLink to="/" class="w-full mx-auto grid grids-cols-1 md:grid-cols-2 justify-center md:w-1/3 md:ml-0 hover:no-underline">
            <img src="/green-web-analyzer.svg" class="w-12 m-auto" alt="Logo in the shape of a leaf" />
            <h1 class="w-full m-auto whitespace-nowrap text-lg lg:text-2xl text-gray-200">Green Web Analyzer</h1>
        </RouterLink>
        <nav class="grid grids-cols-1 md:grid-cols-4 justify-center w-full mx-auto xl:w-3/4 2xl:w-1/2 md:mr-0">
            <TheThemeSwitch />
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
    </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TheThemeSwitch from './TheThemeSwitch.vue';

export default defineComponent({
    computed: {
        resultsClasses() {
            return {
                "btn-nav": true,
                "border-primary-60": this.$router.currentRoute.value.path == '/results',
            }
        },
        aboutClasses() {
            return {
                "btn-nav": true,
                "border-primary-60": this.$router.currentRoute.value.path == '/about',
            }
        },
        searchClasses() {
            return {
                "btn-nav": true,
                "border-primary-60": this.$router.currentRoute.value.path == '/search',
            }
        }
    },
    components: {
        TheThemeSwitch
    }
})
</script>