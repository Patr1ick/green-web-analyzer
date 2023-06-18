<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Outgoing requests
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table>
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th>Response</th>
                            <th>Method</th>
                            <th>URL</th>
                            <th>Date</th>
                            <th>Content-Type</th>
                            <th>Size</th>
                        </tr>
                    </thead>
                    <tr v-for="request in result.details.requests" class="text-gray-800 dark:text-gray-200">
                        <td>
                            <CheckCircleIcon v-if="requestSuccess(request)"
                                class="w-8 md:w-10 h-auto m-auto text-emerald-600" />
                            <XCircleIcon v-if="!requestSuccess(request)" class="w-10 h-auto m-auto text-rose-600" />
                        </td>
                        <td>
                            {{ request.method }}
                        </td>
                        <td
                            class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 text-left pl-4 max-w-sm">
                            <a :href="request.url" class="hover:underline break-all ">
                                {{ request.url }}
                            </a>
                        </td>
                        <td>
                            {{ new Date(request.date).toLocaleString() }}
                        </td>
                        <td>
                            <div v-if="hasResponse(request)">
                                {{ request.response.type }}
                            </div>
                            <div v-else>
                                No Response
                            </div>
                        </td>
                        <td>
                            <div v-if="!hasResponse(request)">
                                No Response
                            </div>
                            <div v-else-if="isRedirect(request)">
                                Redirect
                            </div>
                            <div v-else>
                                {{ convert(request.size) }}
                            </div>
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
import { CriteriaModel, RequestModel } from '../../../models/result';
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
        isRedirect(request: RequestModel) {
            if (request.response) {
                return (request.response.status_code === 301)
            }
            return false
        }
    },
    components: {
        CheckCircleIcon, XCircleIcon
    }
})
</script>