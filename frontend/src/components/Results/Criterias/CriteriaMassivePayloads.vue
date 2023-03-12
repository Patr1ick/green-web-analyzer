<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Avoid massive payloads
            </p>
        </template>
        <template #details>
            <div v-if="result.details.requests.length === 0">
                There are no massive payloads above 500 KB.
            </div>
            <div v-else class="overflow-x-auto">
                <table class="w-full border-separate border-spacing-1">
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Type</th>
                            <th class="border border-gray-600 px-2">Size</th>
                        </tr>
                    </thead>
                    <tr v-for="request in result.details.requests" class="text-gray-800 dark:text-gray-200">
                        <td
                            class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 text-left pl-4 max-w-sm">
                            <a :href="request.url" class="hover:underline break-all ">
                                {{ request.url }}
                            </a>
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
import { defineComponent, PropType } from 'vue'
import { CriteriaModel, RequestModel } from '../../../models/result';
import convertBytesToString from '../../../utils/functions';

export default defineComponent({
    props: {
        result: {
            type: Object as PropType<CriteriaModel>,
            required: true,
        }
    },
    methods: {
        convert(bytes: number | undefined) {
            if (bytes != undefined) {
                return convertBytesToString(bytes);
            }
            else
                return bytes;
        }
    },
})
</script>