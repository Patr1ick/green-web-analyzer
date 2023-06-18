<template>
    <BasicAccordion :status="result.accepted">
        <template #title>
            <p class="text-gray-900 dark:text-gray-200">
                Criteria {{ result.id }}: Image Lazy Loading
            </p>
        </template>
        <template #details>
            <div class="overflow-x-auto">
                <table>
                    <thead class="dark:bg-opacity-25 bg-gray-800">
                        <tr>
                            <th>URL</th>
                            <th>Preview</th>
                            <th>Loaded</th>
                            <th>Visible</th>
                        </tr>
                    </thead>
                    <tr v-for="img in result.details.files">
                        <td class="break-all">
                            <a :href="img.url" target="_blank" class="hover:underline">
                                {{ img.url }}
                            </a>
                        </td>
                        <td>
                            <img :src="img.url" class="w-12 h-auto m-auto" />
                        </td>
                        <td>
                            <CheckCircleIcon v-if="img.is_loaded" class="w-8 h-auto text-primary m-auto" />
                            <XCircleIcon v-else class="w-8 h-auto text-rose-800 m-auto" />
                        </td>
                        <td>
                            <CheckCircleIcon v-if="img.is_visible" class="w-8 h-auto text-primary m-auto" />
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