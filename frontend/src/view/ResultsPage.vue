<template>
    <ResultsSummary v-if="!isLoaded" />
    <BasicCard v-else>
        <main class="flex justify-center items-center flex-col w-3/4 m-auto">
            <h1 class="text-gray-900 dark:text-gray-200">No Results loaded. Search or request a report to show a report
            </h1>
            <div class="m-4">
                <BasicButton @click="$router.push('/request')">
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