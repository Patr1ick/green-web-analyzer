<template>
    <ResultsSummary v-if="!isLoaded" />
    <BasicCard v-else class="m-2 md:m-16">
        <main class="grid grid-cols-1 justify-center items-center w-3/4 m-auto">
            <h1 class="text-center text-lg">
                No report is loaded.
            </h1>
            <div class="grid grid-cols-2 gap-4">
                <BasicButton @click="$router.push('/')">
                    Request
                </BasicButton>
                <BasicButton @click="$router.push('/search')">
                    Search
                </BasicButton>
            </div>
        </main>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ResultsSummary from '../components/Results/ResultsSummary.vue';

export default defineComponent({
    computed: {
        isLoaded() {
            return this.$store.getters.isResultNull;
        }
    },
    components: {
        ResultsSummary
    }
})
</script>