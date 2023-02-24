<template>
    <header class="flex flex-col md:flex-row justify-between content-center px-8 py-4 bg-teal-800 dark:bg-zinc-900">
        <RouterLink to="/" class="flex flex-col md:flex-row items-center">
            <img src="green-web-analyzer.svg" class="m-4 w-12" />
            <h1 class="text-2xl text-gray-100 m-4 text-center hidden lg:block">Green Web Analyzer</h1>
        </RouterLink>
        <div class="flex justify-between content-center flex-col md:flex-row flex-wrap p-4 m-auto md:ml-auto md:mr-0">
            <TheThemeSwitch />
            <nav class="flex flex-wrap justify-between content-center mx-4">
                <RouterLink to="/about" :class="linkClass">
                    About
                </RouterLink>
                <RouterLink to="/results" :class="linkClass">
                    Results
                </RouterLink>
                <RouterLink to="/search" :class="linkClass">
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
    data() {
        return { linkClass: "p-4 no-underline text-gray-100 text-lg border-solid border-2 border-transparent rounded-sm hover:border-gray-100 w-full sm:w-auto text-center" }
    },
    components: {
        TheThemeSwitch
    }
})
</script>