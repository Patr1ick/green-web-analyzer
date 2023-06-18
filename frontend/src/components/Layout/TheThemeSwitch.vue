<template>
    <button @click="switchTheme" class="btn-nav flex justify-center">
        <SunIcon v-if="!darkTheme" class="text-white w-8 h-8" />
        <MoonIcon v-if="darkTheme" class="text-white w-8 h-8" />
    </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { SunIcon, MoonIcon } from '@heroicons/vue/24/outline'

export default defineComponent({
    data() {
        return {
            theme: localStorage.getItem('theme')
        }
    },
    watch: {
        theme(newValue: string) {
            localStorage.setItem('theme', newValue)
            if (newValue == 'light') {
                document.documentElement.classList.remove('dark')
            } else {
                document.documentElement.classList.add('dark')
            }
        }
    },
    computed: {
        darkTheme() {
            return this.theme == 'dark'
        }
    },
    methods: {
        switchTheme() {
            if (this.theme == 'light') {
                this.theme = 'dark'
            } else this.theme = 'light'
        }
    },
    components: {
        SunIcon, MoonIcon
    }
})
</script>