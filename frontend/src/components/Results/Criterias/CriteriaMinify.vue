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
                    <table v-else>
                        <thead class="dark:bg-opacity-25 bg-gray-800">
                            <tr>
                                <th>URL</th>
                                <th class=" bg-red-800 bg-opacity-20">Size</th>
                                <th class=" bg-primary-dark-40 bg-opacity-20">Minified Size</th>
                                <th>Potential Savings</th>
                            </tr>
                        </thead>
                        <tr v-for="file in result.details[key].files">
                            <td class="break-all">
                                <a :href="file.url" target="_blank" class="hover:underline">
                                    {{ file.url }}
                                </a>
                            </td>
                            <td class="bg-red-800 bg-opacity-20">
                                {{ convert(file.size) }}
                            </td>
                            <td class="bg-primary-dark-40 bg-opacity-20">
                                {{ convert(file.minified_size) }}
                            </td>
                            <td>
                                - {{ convert(file.potential_saving) }}
                            </td>
                        </tr>
                        <tr>
                            <td>
                                Summary
                            </td>
                            <td class="bg-red-800 bg-opacity-50">
                                {{ convert(result.details[key].total_size) }}</td>
                            <td class="bg-primary-dark-40 bg-opacity-50">
                                {{ convert(result.details[key].total_minified_size) }}
                            </td>
                            <td>
                                - {{ convert(result.details[key].total_savings) }}</td>
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