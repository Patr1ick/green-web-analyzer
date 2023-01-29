<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Outgoing requests
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table class="w-full border-separate border-spacing-1">
                    <thead class="bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">Response</th>
                            <th class="border border-gray-600 px-2">Method</th>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Date</th>
                            <th class="border border-gray-600 px-2">Content-Type</th>
                            <th class="border border-gray-600 px-2">Size</th>
                        </tr>
                    </thead>
                    <tr v-for="request in result.details.requests">
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <CheckCircleIcon v-if="requestSuccess(request.response.status_code)"
                                class="w-8 md:w-10 h-auto m-auto text-emerald-600" />
                            <XCircleIcon v-if="!requestSuccess(request.response.status_code)"
                                class="w-10 h-auto m-auto text-rose-600" />
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ request.method }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <a :href="request.url" class="hover:underline text-clip">
                                {{ request.url }}
                            </a>
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ new Date(request.date).toLocaleString() }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ request.response.type }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ convert(request.size) }}
                        </td>
                    </tr>
                </table>
            </div>
        </template>
    </BasicAccordion>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import type { PropType } from 'vue'
import { CriteriaModel } from '../../../models/result';
import convertBytesToString from '../../../utils/functions'

import { CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/outline'

export default defineComponent({
    props: {
        result: {
            type: Object as PropType<CriteriaModel>,
            required: true,
        }
    },
    methods: {
        requestSuccess(status: number): boolean {
            return (status >= 200 && status < 400)
        },
        convert(bytes: number | undefined) {
            if (bytes != undefined) {
                return convertBytesToString(bytes);
            }
            else
                return bytes;
        }
    },
    components: {
        CheckCircleIcon, XCircleIcon
    }
})
</script>