<template>
    <div class="flex justify-center items-center flex-col">
        <h2 class="text-gray-900 dark:text-gray-200">
            Request a report from a Website
        </h2>
        <form @submit.prevent="requestReport" class="grid grid-cols-1 items-center w-full lg:w-fit lg:grid-cols-12 gap-4 my-4">
            <RequestInput v-model="url" :disabled="isLoading" class="lg:col-span-10" />
            <BasicButton type="submit" :disabled="isLoading" class="lg:col-span-2">
                <MagnifyingGlassIcon class="p-2 h-12" />
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
import { LinkIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/solid'


export default defineComponent({
    components: {
        RequestInput,
        LinkIcon,
        MagnifyingGlassIcon
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
                "https://backend.green-web-analyzer.eu/requests",
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
                if (!response.ok) {
                    this.error = true
                }
                return response.json()
            }).then((data) => {
                this.$store.commit('invertIsLoading');
                if (this.error){
                    this.errorMessage = `${data.name}: ${data.description}`;
                }else{
                    this.$store.commit('setRequestResult', data)
                    this.$router.push('/results')
                }
            }).catch((error) => {
                this.$store.commit('invertIsLoading');
                this.error = true;
                this.errorMessage = error;
            })
        }
    }
})
</script>
