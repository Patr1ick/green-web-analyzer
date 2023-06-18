<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Image Types
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table>
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th>URL</th>
                            <th>Preview</th>
                            <th>Type</th>
                            <th class="bg-red-800 bg-opacity-20">Size</th>
                            <th class="bg-primary-dark-40 bg-opacity-20">Size in Webp</th>
                            <th>Potential Savings</th>
                        </tr>
                    </thead>
                    <tr v-for="img in result.details.files">
                        <td class="break-all">
                            <a :href="img.url" target="_blank" class="hover:underline">
                                {{ img.url }}
                            </a>
                        </td>
                        <td >
                            <img :src="img.url" class="w-12 h-auto m-auto" />
                        </td>
                        <td >
                            {{ img.type }}
                        </td>
                        <td
                            class="bg-red-800 bg-opacity-20">
                            {{ convert(img.size) }}
                        </td>
                        <td
                            class="bg-primary-dark-40 bg-opacity-20">
                            {{ convert(img.size_webp) }}
                        </td>
                        <td >
                            - {{ convert(img.potential_saving) }}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3" class="px-2">
                            Summary ({{ result.details.files.length }} Images)
                        </td>
                        <td class="bg-red-800 bg-opacity-50">{{
                            convert(result.details.total_size) }}</td>
                        <td class="px-2 bg-primary-dark-40 bg-opacity-50"> {{
                            convert(result.details.total_size_webp)
                        }} </td>
                        <td class="px-2">
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