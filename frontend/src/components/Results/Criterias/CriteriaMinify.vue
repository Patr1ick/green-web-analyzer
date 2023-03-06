<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Minify JS
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <h2 class="font-bold">JavaScript files</h2>
                <p v-if="result.details.files.js.length === 0">
                    All files are minified.
                </p>
                <table v-else class="w-full p-4 border-separate border-spacing-1 ">
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Actual Size</th>
                            <th class="border border-gray-600 px-2">Minified Size</th>
                        </tr>
                    </thead>
                    <tr v-for="file in result.details.files.js" class="text-gray-800 dark:text-gray-200">
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 break-all">
                            <a :href="file.url" target="_blank" class="hover:underline">
                                {{ file.url }}
                            </a>
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ convert(file.actual_size) }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ convert(file.minified_size) }}
                        </td>
                    </tr>
                    <tr class="dark:bg-opacity-25 bg-gray-800">
                        <td class="border border-gray-600 px-2">
                            Summary
                        </td>
                        <td class="border border-gray-600 px-2">{{ convert(result.details.actual_size_js) }}</td>
                        <td class="border border-gray-600 px-2">
                            ??? (Saving {{ convert(result.details.potential_savings_js) }})
                        </td>
                    </tr>
                </table>
                <h2 class="font-bold">CSS files</h2>
                <table class="w-full p-4 border-separate border-spacing-1 ">
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th class="border border-gray-600 px-2">URL</th>
                            <th class="border border-gray-600 px-2">Actual Size</th>
                            <th class="border border-gray-600 px-2">Minified Size</th>
                        </tr>
                    </thead>
                    <tr v-for="file in result.details.files.css" class="text-gray-800 dark:text-gray-200">
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 break-all">
                            <a :href="file.url" target="_blank" class="hover:underline">
                                {{ file.url }}
                            </a>
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ convert(file.actual_size) }}
                        </td>
                        <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                            {{ convert(file.minified_size) }}
                        </td>
                    </tr>
                    <tr class="dark:bg-opacity-25 bg-gray-800">
                        <td class="border border-gray-600 px-2">
                            Summary
                        </td>
                        <td class="border border-gray-600 px-2">{{ convert(result.details.actual_size_css) }}</td>
                        <td class="border border-gray-600 px-2">
                            ??? (Saving {{ convert(result.details.potential_savings_css) }})
                        </td>
                    </tr>
                </table>
            </div>
        </template>
    </BasicAccordion>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { CriteriaModel } from '../../../models/result';
import convertBytesToString from '../../../utils/functions'

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