<template>
    <BasicCard class="m-4 md:m-16">
        <div class="flex flex-col justify-center text-center">
            <h1 class="text-xl sm:text-4xl">
                <a :href="results?.url" target="_blank" class="hover:underline text-gray-600 dark:text-gray-200">
                    {{ results?.url }}
                </a>
            </h1>
            <p class="text-center">Created on {{ new Date(results!.date).toLocaleString() }}</p>
            <h2>Metrics</h2>
            <div class="metrics">
                <div>
                    <h3 class="text-xs mb-0">Size</h3>
                    <p class="text-center text-2xl">{{ convert(results?.metrics.size) }}</p>
                </div>
                <div>
                    <h3 class="text-xs mb-0">Estimated CO2 emissions</h3>
                    <p class="text-center text-2xl">{{ getEmissions(results!.metrics.size, results?.metrics.green.green) }}g
                    </p>
                </div>
                <div>
                    <h3 class="text-xs mb-0">Outgoing Requests</h3>
                    <p class="text-center text-2xl">{{ results?.metrics.requests }}</p>
                </div>
                <div>
                    <h3 class="text-xs mb-0">Potential Savings</h3>
                    <p class="text-center text-2xl">{{ convert(results?.metrics.potential_savings) }}</p>
                </div>
            </div>
            <BasicAccordion :status="results?.metrics.green.green" class="md:w-1/2 2xl:w-1/3 mt-8 md:mx-auto">
                <template #title>
                    {{ results?.metrics.green.green ? `This website is using green energy.` : `This website is not
                    using green energy`}}
                </template>
                <template #details v-if="results?.metrics.green.green">
                    <p v-if="results?.metrics.green.hosted_by !== ''" class="text-xs text-center">
                        Hosted by {{ results?.metrics.green.hosted_by }}
                    </p>
                    <div v-if="results?.metrics.green.details && results?.metrics.green.details.length !== 0" class="mt-4">
                        <h4 class="text-lg"> More Information</h4>
                        <div v-for="doc in results?.metrics.green.details" class="text-xs">
                            <a :href="doc.link" target="_blank" class="hover:underline">{{ doc.title }}</a>
                        </div>
                    </div>
                </template>
                <template #details v-else>
                    <p class="text-xs">
                        It appears that this website does not use a hosting service that uses green energy.  Please note that this information may be incorrect. There are several possible reasons for a mistakes. You can find out more about the methodology <RouterLink to="/about#methodology">here</RouterLink>.
                    </p>
                </template>
            </BasicAccordion>
            
            <h2>Criterias</h2>
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
        CriteriaRequests,
        CriteriaImageType,
        CriteriaImageCompression,
        CriteriaRedirects,
        CriteriaMinify,
        CriteriaImageLazyLoad,
        CriteriaMassivePayloads,
        CheckCircleIcon,
        XCircleIcon
    }
})
</script>
