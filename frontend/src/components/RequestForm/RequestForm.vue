<template>
    <div class="flex justify-center items-center flex-col mt-8">
        <h1 class="text-2xl font-bold text-center text-gray-900 dark:text-gray-200">
            Request a report from a Website
        </h1>
        <form @submit.prevent="requestReport" class="flex flex-wrap justify-center content-center w-1/2 my-4">
            <input id="url" type="url" v-model="url"
                class="grow text-gray-900 text-center font-bold bg-gray-200 border-2 border-solid rounded-sm border-teal-600 h-14"
                placeholder="https://www.example.com" />
            <BasicButton type="submit" :disabled="isLoading" class="mr-0">
                Submit
            </BasicButton>
        </form>
        <BasicHint v-if="isLoading" type="information">
            Generating the request. This can take a while.
        </BasicHint>
        <BasicHint v-if="error" type="error">
            {{ errorMessage }}
        </BasicHint>
    </div>
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
                "https://backend.green-web-analyzer.eu/request",
                // "http://localhost:5000/request",
                {
                    method: "POST",
                    body: JSON.stringify({
                        url: this.url
                    }),
                    headers: {
                        "Content-Type": "application/json"
                    }
                }
            ).then(async (response) => {
                if (response.ok) {
                    return response.json()
                }
                const data = await response.json()
                throw new Error(data.description)
            }).then((data) => {
                this.$store.commit('invertIsLoading')
                this.$store.commit('setRequestResult', data)
                this.$router.push('/results')
            }).catch((err) => {
                this.$store.commit('invertIsLoading')
                this.errorMessage = err;
                this.error = true
            })
        }
    }
})
</script>