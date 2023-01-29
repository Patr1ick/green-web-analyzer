<template>
    <BasicCard class="flex justify-center content-center flex-col">
        <h1 class="text-2xl font-bold text-center text-gray-900 dark:text-gray-200">
            Request a report from a Website
        </h1>
        <form @submit.prevent="requestReport" class="flex flex-wrap justify-center content-center my-8">
            <input id="url" type="url" v-model="url"
                class="text-gray-900 text-center font-bold bg-gray-200 border-2 border-solid rounded-sm border-teal-600 w-96 h-14 m-4"
                placeholder="https://www.example.com" />
            <BasicButton type="submit" :disabled="isLoading">
                Submit
            </BasicButton>
        </form>
        <p v-if="isLoading" class="text-center text-gray-800 dark:text-gray-200">Loading...</p>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            url: "https://www.wikipedia.org",
            error: false,
            errorMessage: ""
        }
    },
    computed: {
        isLoading() {
            return this.$store.state.isLoading;
        }
    },
    methods: {
        requestReport() {
            this.$store.commit('invertIsLoading')
            this.error = false;
            fetch(
                "http://backend.green-web-analyzer.eu/request",
                {
                    method: "POST",
                    body: JSON.stringify({
                        url: this.url
                    }),
                    headers: {
                        "Content-Type": "application/json"
                    }
                }
            ).then((response) => {
                this.$store.commit('invertIsLoading')
                if (response.ok) {
                    return response.json()
                }
                this.error = true;
                throw new Error(response.statusText)
            }).then((data) => {
                this.$store.commit('setRequestResult', data)
                this.$router.push('/results')
            }).catch((error) => {
                this.errorMessage = error.message;
                console.log(this.errorMessage)
            })
        }
    }
})
</script>