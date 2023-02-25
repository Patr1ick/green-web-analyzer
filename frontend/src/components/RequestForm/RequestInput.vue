<template>
    <div class="grid grid-cols-12 justify-start items-center rounded border-2 border-emerald-600 m-2">
        <div class="bg-emerald-600 col-span-2 md:col-span-1">
            <MagnifyingGlassIcon class="p-2 w-12 h-full rounded-full text-white dark:text-gray-900" />
        </div>
        <input v-model="content" @input="handleInput" id="url" type="url"
            class="col-span-9 md:col-span-10 w-full h-full bg-transparent outline-none m-2 text-center"
            placeholder="https://www.example.com/" />
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