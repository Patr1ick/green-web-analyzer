<template>
    <BasicCard class="m-2 md:m-16">
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
                        <h3>Size</h3>
                        <p>{{ convert(results?.metrics.size) }}</p>
                    </div>
                    <div class="metric">
                        <h3>Estimated CO2 emissions</h3>
                        <p>{{ getEmissions(results!.metrics.size, results?.metrics.green.green) }}g</p>
                    </div>
                </tr>
                <tr class="metrics-row">
                    <div class="metric">
                        <h3>Outgoing Requests</h3>
                        <p>{{ results?.metrics.requests }}</p>
                    </div>
                    <div class="metric">
                        <h3>Potential Savings</h3>
                        <p>{{ convert(results?.metrics.potential_savings) }}</p>
                    </div>
                </tr>
            </table>
            <section
                class="my-4 w-1/2 mx-auto grid justify-center border rounded p-4 border-gray-800 dark:border-gray-200 dark:border-opacity-20">
                <div v-if="results?.metrics.green.green" class="flex justify-center items-center gap-4 text-lg">
                    <CheckCircleIcon class="w-8 h-auto text-emerald-600" />
                    This website is using green enery.
                </div>
                <div v-else class="flex justify-center items-center gap-4 text-lg">
                    <XCircleIcon class="w-8 h-auto text-rose-800" />
                    This website is not using green enery.
                </div>
                <p v-if="results?.metrics.green.hosted_by !== ''" class="text-xs">
                    (Hosted on {{ results?.metrics.green.hosted_by }})
                </p>
                <div v-if="results?.metrics.green.details && results?.metrics.green.details.length !== 0" class="mt-4">
                    <h4 class="text-lg"> More Information</h4>
                    <div v-for="doc in results?.metrics.green.details" class="text-xs">
                        <a :href="doc.link" target="_blank" class="hover:underline">{{ doc.title }}</a>
                    </div>
                </div>
            </section>
            <h2 class="text-2xl mt-4">Criterias</h2>
            <section class="w-full xl:w-3/4 2xl:w-4/5 m-auto">
                <CriteriaRequests :result="getCriteria(0)" />
                <CriteriaMassivePayloads :result="getCriteria(1)" />
                <CriteriaRedirects :result="getCriteria(2)" />
                <CriteriaImageType :result="getCriteria(3)" />
                <CriteriaImageCompression :result="getCriteria(4)" />
                <CriteriaImageLazyLoad :result="getCriteria(5)" />
                <CriteriaMinify :result="getCriteria(6)" />
            </section>
        </div>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import convertBytesToString from '../../utils/functions'
import CriteriaImageType from './Criterias/Images/CriteriaImageType.vue';
import CriteriaRequests from './Criterias/CriteriaRequests.vue';
import CriteriaImageCompression from './Criterias/Images/CriteriaImageCompression.vue'
import { CriteriaModel } from '../../models/result';
import CriteriaRedirects from './Criterias/CriteriaRedirects.vue';
import CriteriaMinify from './Criterias/CriteriaMinify.vue';
import CriteriaImageLazyLoad from './Criterias/Images/CriteriaImageLazyLoad.vue';
import CriteriaMassivePayloads from './Criterias/CriteriaMassivePayloads.vue';
import { CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/solid'

import { co2 } from '@tgwf/co2'

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
        },
        getEmissions(bytes: number, green_hosting: boolean): number {

            const model = new co2()

            return Math.round(model.perByte(bytes, green_hosting) * 1000) / 1000
        }
    },
    components: {
        CriteriaRequests, CriteriaImageType, CriteriaImageCompression, CriteriaRedirects, CriteriaMinify, CriteriaImageLazyLoad, CriteriaMassivePayloads, CheckCircleIcon, XCircleIcon
    }
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