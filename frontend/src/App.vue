<template>
    <TheHeader />
    <main class="grow">
        <RouterView />
    </main>
    <TheFooter />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import TheDisclaimer from "./components/Layout/TheDisclaimer.vue";
import TheFooter from "./components/Layout/TheFooter.vue";
import TheHeader from "./components/Layout/TheHeader.vue";

export default defineComponent({
    beforeCreate() {
        if (
            localStorage.theme === "dark" ||
            (!("theme" in localStorage) &&
                window.matchMedia("(prefers-color-scheme: dark)").matches)
        ) {
            document.documentElement.classList.add("dark");
            localStorage.setItem("theme", "dark");
        } else {
            document.documentElement.classList.remove("dark");
            localStorage.setItem("theme", "light");
        }
    },
    components: { TheHeader, TheFooter, TheDisclaimer },
});
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
    body {
        @apply bg-gray-200 text-gray-800 dark:bg-zinc-800 dark:text-gray-300;
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
        @apply cursor-pointer text-primary-dark-40;
    }

    a:hover {
        @apply underline;
    }

    /*  */
    footer {
        @apply flex flex-col justify-center items-center px-4 py-8 bottom-0 bg-zinc-900 text-gray-200;
    }

    table {
        @apply w-full border-separate border-spacing-1 p-4;
    }

    tr {
        @apply text-gray-600 dark:text-gray-200;
    }

    th {
        @apply border border-gray-600 px-2 text-gray-200;
    }

    td {
        @apply border border-gray-700 dark:border-gray-100 dark:border-opacity-25 px-2;
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

    .btn:disabled:hover {
        @apply bg-primary-dark-40 cursor-not-allowed;
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

    .metrics {
        @apply grid grid-cols-2 lg:grid-cols-4 gap-4 w-full md:w-1/2 mx-auto mb-4;
    }
}
</style>
