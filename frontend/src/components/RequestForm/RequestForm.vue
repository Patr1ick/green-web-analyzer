<template>
    <div class="flex justify-center items-center flex-col mt-8">
        <h1 class="text-2xl font-bold text-center text-gray-900 dark:text-gray-200">
            Request a report from a Website
        </h1>
        <form @submit.prevent="requestReport" class="flex flex-wrap justify-center content-center my-4">
            <RequestInput v-model="url" />
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
        <BasicHint v-if="error" type="information" class="my-2">
            <span v-if="error" class="flex flex-col gap-1 justify-items-center">
                <p>
                    If the error still occurs, please create an issue at
                </p>
                <a href="https://github.com/Patr1ick/green-web-analyzer/issues/new/choose" target="_blank"
                    class="flex gap-1 justify-center">
                    GitHub
                    <LinkIcon class="w-4 text-gray-200" />
                </a>
            </span>
        </BasicHint>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import RequestInput from './RequestInput.vue'
import { LinkIcon } from '@heroicons/vue/24/solid'


export default defineComponent({
    components: {
        RequestInput,
        LinkIcon
    },
    data() {
        return {
            url: "",
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
