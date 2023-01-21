<template>
    <BasicCard class="flex justify-center content-center flex-col">
        <h1 class="text-2xl font-bold text-center text-gray-900 dark:text-gray-200">
            Request a report from a Website
        </h1>
        <form @submit.prevent="requestReport" class="flex justify-center content-center my-8">
            <input id="url" type="url" v-model="url"
                class="text-gray-900 text-center font-bold bg-gray-200 border-2 border-solid rounded-sm border-teal-600 w-96 h-14 my-auto"
                placeholder="https://www.example.com" />
            <BasicButton type="submit" :disabled="isLoading">
                Submit
            </BasicButton>
        </form>
        <ScaleLoader v-if="isLoading" color="rgb(13, 148, 136)" width="0.5em" />
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ScaleLoader from 'vue-spinner/src/ScaleLoader.vue'

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
                "http://localhost:5000/request",
                {
                    method: "POST",
                    body: JSON.stringify({
                        url: this.url
                    })
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
    },
    components: {
        ScaleLoader
    }
})
</script>