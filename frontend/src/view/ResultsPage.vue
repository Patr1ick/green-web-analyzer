<template>
    <ResultsSummary v-if="!isLoaded" />
    <BasicCard v-else class="m-2 md:m-16">
        <main class="flex justify-center items-center flex-col w-3/4 m-auto">
            <h1 class="text-gray-900 dark:text-gray-200 text-lg">
                No results loaded. Please request or search for a report.
            </h1>
            <div class="m-4">
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