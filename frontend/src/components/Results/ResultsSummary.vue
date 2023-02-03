<template>
    <BasicCard>
        <div class="flex flex-col justify-center text-center dark:text-gray-200">
            <h1 class="text-2xl sm:text-4xl mb-4">
                <a :href="results?.url" target="_blank" class="hover:underline">
                    {{ results?.url }}
                </a>
            </h1>
            <p>Created on {{ new Date(results!.date).toLocaleString() }}</p>
            <h2 class="text-2xl mt-4">Metrics</h2>
            <table class="flex flex-wrap justify-center">
                <tr class="metrics-row">
                    <div class="metric">
                        <h3>Size in Bytes</h3>
                        <p>{{ convert(results?.metrics.size) }}</p>
                    </div>
                    <div class="metric">
                        <h3>Amount of outgoing Requests</h3>
                        <p>{{ results?.metrics.requests }}</p>
                    </div>
                </tr>
                <tr class="metrics-row">
                    <div class="metric">
                        <h3>Metric #3</h3>
                        <p>Value</p>
                    </div>
                    <div class="metric">
                        <h3>Metric #4</h3>
                        <p>Value</p>
                    </div>
                </tr>
            </table>
            <h2 class="text-2xl mt-4">Criterias</h2>
            <section class="w-full xl:w-3/4 2xl:w-4/5 m-auto">
                <CriteriaRequests :result="getCriteria(0)" />
                <CriteriaImageType :result="getCriteria(1)" />
                <CriteriaImageCompression :result="getCriteria(2)" />
            </section>
        </div>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import convertBytesToString from '../../utils/functions'
import CriteriaImageType from './Criterias/CriteriaImageType.vue';
import CriteriaRequests from './Criterias/CriteriaRequests.vue';
import CriteriaImageCompression from './Criterias/CriteriaImageCompression.vue'

import { CriteriaModel } from '../../models/result';

export default defineComponent({
    computed: {
        results() {
            return this.$store.state.requestResult;
        }
    },
    methods: {
        convert(bytes: number | undefined) {
            if (bytes != undefined) {
                return convertBytesToString(bytes);
            }
            else
                return bytes;
        },
        getCriteria(index: number): CriteriaModel {
            if (this.results !== undefined) {
                return this.results!.criteria[index]
            }
            const empty: CriteriaModel = {
                id: -1,
                accepted: false,
                details: null
            };
            return empty;
        }
    },
    components: { CriteriaRequests, CriteriaImageType, CriteriaImageCompression }
})
</script>


<style scoped>
.metric h3 {
    font-size: 12px;
    margin: 0em;
}

.metric p {
    margin: 0em;
    font-size: 28px;
}

.metrics-row {
    display: flex;
}

.metric {
    margin: 1em;
    display: flex;
    flex-direction: column;
}
</style>