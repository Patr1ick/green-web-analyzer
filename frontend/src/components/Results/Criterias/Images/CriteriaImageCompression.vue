<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Image Compression
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table class="w-full p-4 border-separate border-spacing-1">
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Preview</th>
                            <th class="border border-gray-600 px-2">Type</th>
                            <th class="border border-gray-600 px-2 bg-red-800 bg-opacity-20">Size</th>
                            <th class="border border-gray-600 px-2 bg-emerald-800 bg-opacity-20">Compressed Size</th>
                            <th class="border border-gray-600 px-2">Potential Savings</th>
                        </tr>
                    </thead>
                    <tr v-for="img in result?.details.files" class="text-gray-800 dark:text-gray-200">
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 break-all">
                            <a :href="img.url" target="_blank" class="hover:underline">
                                {{ img.url }}
                            </a>
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            <img :src="img.url" class="w-12 h-auto m-auto" />
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ img.type }}
                        </td>
                        <td
                            class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 bg-red-800 bg-opacity-20">
                            {{ convert(img.size) }}
                        </td>
                        <td
                            class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 bg-emerald-800 bg-opacity-20">
                            {{ convert(img.size_compressed) }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            - {{ convert(img.potential_saving) }}
                        </td>
                    </tr>
                    <tr class="dark:bg-opacity-25 bg-gray-800">
                        <td colspan="3" class="border border-gray-600 px-2">
                            Summary ({{ result.details.files.length }} Images)
                        </td>
                        <td class="border border-gray-600 px-2 bg-red-800 bg-opacity-20">{{
                            convert(result.details.total_size) }}</td>
                        <td class="border border-gray-600 px-2 bg-emerald-800 bg-opacity-20">
                            {{ convert(result.details.total_size_compressed) }}
                        </td>
                        <td class="border border-gray-600 px-2">
                            - {{ convert(result.details.total_savings) }}
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
import convertBytesToString from '../../../../utils/functions'

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
    }
})
</script>