<template>
    <TheDisclaimer />
    <TheHeader />
    <main class="grow">
        <RouterView />
    </main>
    <TheFooter />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheDisclaimer from './components/Layout/TheDisclaimer.vue';
import TheFooter from './components/Layout/TheFooter.vue';
import TheHeader from './components/Layout/TheHeader.vue'

export default defineComponent({
    beforeCreate() {
        if (localStorage.theme === "dark" || (!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
            document.documentElement.classList.add("dark");
            localStorage.setItem("theme", "dark");
        }
        else {
            document.documentElement.classList.remove("dark");
            localStorage.setItem("theme", "light");
        }
    },
    components: { TheHeader, TheFooter, TheDisclaimer }
})
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
