<template>
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

@layer base {

    body {
        @apply bg-gray-200 text-gray-800;
    }

    /* Headings */
    h1 {
        @apply text-4xl mb-4 font-bold;
    }

    h2 {
        @apply text-2xl mb-4 mt-8 font-bold;
    }

    h3 {
        @apply text-lg mb-2 mt-4 font-bold;
    }

    p {
        @apply text-justify;
    }

    /* Links */
    a {
        @apply cursor-pointer;
    }

    a:hover {
        @apply underline;
    }

    /*  */
    footer {
        @apply flex flex-col justify-center items-center px-4 py-8 bottom-0 bg-zinc-900 text-gray-200;
    }
}

@layer components {
    .card {
        @apply p-4 rounded shadow-2xl;
    }

    .card-white {
        @apply bg-gray-100;
    }

    .card-dark {
        @apply bg-zinc-900;
    }

    /* Buttons */
    .btn {
        @apply border-2 border-primary rounded inline-block p-2;
    }

    .btn:hover {
        @apply bg-primary text-gray-200;
    }

    .btn:active {
        @apply border-primary;
    }

    .btn:disabled {
        @apply border-primary-dark-40 opacity-50;
    }

    .btn-nav {
        @apply p-4 border-transparent border-solid border-2 rounded-sm text-gray-100 text-lg text-center;
    }

    .btn-nav:hover {
        @apply no-underline border-primary;
    }

    .btn-nav:active {
        @apply border-primary-dark-40;
    }
}
</style>
