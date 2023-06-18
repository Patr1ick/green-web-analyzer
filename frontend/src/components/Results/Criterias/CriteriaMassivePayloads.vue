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
                <table>
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th>URL</th>
                            <th>Type</th>
                            <th>Size</th>
                        </tr>
                    </thead>
                    <tr v-for="request in result.details.requests">
                        <td class="text-left pl-4 max-w-sm">
                            <a :href="request.url" class="hover:underline break-all ">
                                {{ request.url }}
                            </a>
                        </td>
                        <td>
                            {{ request.response.type }}
                        </td>
                        <td>
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