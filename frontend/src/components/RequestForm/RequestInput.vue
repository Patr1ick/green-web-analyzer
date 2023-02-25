<template>
    <div class="flex justify-start items-center rounded border-2 border-emerald-600 m-2">
        <div class="bg-emerald-600">
            <MagnifyingGlassIcon class="p-2 w-12 h-full rounded-full text-white dark:text-gray-900" />
        </div>
        <input v-model="content" @input="handleInput" id="url" type="url"
            class="w-80 h-full bg-transparent outline-none m-2" placeholder="https://www.example.com/" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { MagnifyingGlassIcon } from '@heroicons/vue/24/solid'


export default defineComponent({
    components: {
        MagnifyingGlassIcon
    },
    props: {
        modelValue: {
            type: String,
        }
    },
    data() {
        return {
            content: "",
        }
    },
    methods: {
        handleInput() {
            this.$emit('update:modelValue', this.content)
        }
    }
})

</script>