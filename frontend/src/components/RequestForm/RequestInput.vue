<template>
    <div class="grid grid-cols-12 justify-start items-center rounded border-2 border-primary">
        <input v-model="content" @input="handleInput" id="url" type="url"
            class="col-span-full h-12 bg-transparent outline-none m-2 text-center" placeholder="https://www.example.com/" />
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