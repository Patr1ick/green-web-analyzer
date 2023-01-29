<template>
    <header class="flex flex-col md:flex-row justify-between content-center px-8 py-4 bg-teal-800 dark:bg-gray-900">
        <RouterLink to="/">
            <h1 class="text-4xl text-gray-100 py-6 text-center">Website Analyzer</h1>
        </RouterLink>
        <div class="flex justify-between content-center flex-col sm:flex-row flex-wrap p-4 m-auto md:ml-auto md:mr-0">
            <TheThemeSwitch />
            <nav class="flex flex-wrap justify-between content-center mx-4">
                <RouterLink to="/request" :class="linkClass">
                    Request
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