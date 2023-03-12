<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Image Lazy Loading
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table class="w-full p-4 border-separate border-spacing-1">
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Preview</th>
                            <th class="border border-gray-600 px-2">Loaded</th>
                            <th class="border border-gray-600 px-2">Visible</th>
                        </tr>
                    </thead>
                    <tr v-for="img in result.details.files" class="text-gray-800 dark:text-gray-200">
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 break-all">
                            <a :href="img.url" target="_blank" class="hover:underline">
                                {{ img.url }}
                            </a>
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <img :src="img.url" class="w-12 h-auto m-auto" />
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <CheckCircleIcon v-if="img.is_loaded" class="w-8 h-auto text-emerald-600 m-auto" />
                            <XCircleIcon v-else class="w-8 h-auto text-rose-800 m-auto" />
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <CheckCircleIcon v-if="img.is_visible" class="w-8 h-auto text-emerald-600 m-auto" />
                            <XCircleIcon v-else class="w-8 h-auto text-rose-800 m-auto" />
                        </td>
                    </tr>
                </table>
            </div>
        </template>

    </BasicAccordion>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { CriteriaModel } from '../../../../models/result';
import { CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/solid'

export default defineComponent({
    props: {
        result: {
            type: Object as PropType<CriteriaModel>,
            required: true,
        }
    },
    components: {
        CheckCircleIcon, XCircleIcon
    },
})
</script>