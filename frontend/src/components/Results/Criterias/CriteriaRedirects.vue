<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Redirects
            </p>
        </template>
        <template #details>
            <div v-if="result.details.redirects.length === 0">
                Looks good! There are no redirects.
            </div>
            <div v-else class="overflow-x-auto">
                <table>
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th>From</th>
                            <th>To</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tr v-for="request in result.details.redirects" class="text-gray-800 dark:text-gray-200">
                        <td class="text-left pl-4 max-w-sm">
                            <a :href="request.from" class="hover:underline break-all ">
                                {{ request.from }}
                            </a>
                        </td>
                        <td class="text-left pl-4 max-w-sm">
                            <a :href="request.to" class="hover:underline break-all ">
                                {{ request.to }}
                            </a>
                        </td>
                        <td>
                            {{ new Date(request.date).toLocaleString() }}
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
        requestSuccess(request: RequestModel): boolean {
            if (request.response) {
                return (request.response.status_code >= 200 && request.response.status_code < 400)
            }
            return false
        },
        convert(bytes: number | undefined) {
            if (bytes != undefined) {
                return convertBytesToString(bytes);
            }
            else
                return bytes;
        },
        hasResponse(request: RequestModel) {
            return request.response !== null
        },
    },
})
</script>