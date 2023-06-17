<template>
    <input v-model="content" @input="handleInput" id="url" type="url"
        class="col-span-full h-full bg-transparent outline-none p-4 text-center rounded border-2 border-primary disabled:btn"
        placeholder="https://www.example.com/" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';


export default defineComponent({
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