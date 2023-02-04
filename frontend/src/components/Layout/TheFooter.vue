<template>
    <footer class="flex flex-col justify-center items-center px-4 py-8 bottom-0 bg-teal-800 dark:bg-zinc-900">
        <p class="text-gray-200">&copy; 2023 Copyright Patrick Geiger</p>
        <nav class="flex justify-center mt-2">
            <RouterLink to="/privacy" class="text-gray-400 hover:underline px-2">Privacy Policy</RouterLink>
        </nav>
    </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>