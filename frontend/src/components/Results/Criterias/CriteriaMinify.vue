<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Minify files
            </p>
        </template>
        <template #details>
            <section class="overflow-x-auto">
                <div v-for="key in ['html', 'css', 'js']" :key="key">
                    <h2 class="font-bold"><span class="uppercase">{{ key }}</span> files</h2>
                    {{ }}
                    <p v-if="result.details[key].files.length == 0">
                        Either all files are minified or there are no files of this data type.
                    </p>
                    <table v-else class="w-full p-4 border-separate border-spacing-1 ">
                        <thead class="dark:bg-opacity-25 bg-gray-800">
                            <tr>
                                <th class="border border-gray-600 px-2">URL</th>
                                <th class="border border-gray-600 px-2">Actual Size</th>
                                <th class="border border-gray-600 px-2">Minified Size</th>
                            </tr>
                        </thead>
                        <tr v-for="file in result.details[key].files" class="text-gray-800 dark:text-gray-200">
                            <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25 break-all">
                                <a :href="file.url" target="_blank" class="hover:underline">
                                    {{ file.url }}
                                </a>
                            </td>
                            <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                                {{ convert(file.size) }}
                            </td>
                            <td class="border border-gray-700 dark:border-gray-100 dark:border-opacity-25">
                                {{ convert(file.minified_size) }}
                            </td>
                        </tr>
                        <tr class="dark:bg-opacity-25 bg-gray-800">
                            <td class="border border-gray-600 px-2">
                                Summary
                            </td>
                            <td class="border border-gray-600 px-2">{{ convert(result.details[key].total_size) }}</td>
                            <td class="border border-gray-600 px-2">
                                {{ convert(result.details[key].total_minified_size) }} (Saved {{
                                    convert(result.details[key].total_savings) }})
                            </td>
                        </tr>
                    </table>
                </div>
            </section>
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