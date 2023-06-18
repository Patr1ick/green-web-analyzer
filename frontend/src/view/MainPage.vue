<template>
    <main class="flex justify-end content-center flex-col m-2 md:m-16">
        <BasicCard class="text-center dark:text-gray-200 w-full lg:3/5 m-auto">
            <h1 class="text-4xl mb-4 font-bold">
                Green Web Analyzer
            </h1>
            <p class="w-4/5 m-auto text-center dark:text-gray-200">
                This website is a tool that allows you to check a website for certain criterias. With the background of
                Green IT, websites are to be checked with regard to data minimisation and efficiency.
            </p>
            <RequestForm />
        </BasicCard>


    </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import RequestForm from '../components/RequestForm/RequestForm.vue';

export default defineComponent({ components: { RequestForm } })
</script>