<template>
    <div class="w-full m-1 border rounded dark:border-opacity-20 border-gray-800 dark:border-gray-200">
        <button @click="collapseAccordion"
            class="w-full flex justify-between items-center p-4 border-b dark:border-opacity-20 border-gray-800 dark:border-gray-200">
            <CheckCircleIcon v-if="status" class="icon" :class="iconStyle" />
            <XCircleIcon v-else class="icon" :class="iconStyle" />
            <slot name="title">

            </slot>
            <PlusIcon v-if="collapsed" class="w-8 h-auto" />
            <MinusIcon v-else class="w-8 h-auto" />
        </button>
        <section v-if="!collapsed" class="text-gray-200 p-4">
            <slot name="description">

            </slot>
            <slot name="details">

            </slot>
        </section>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/solid'

export default defineComponent({
    props: {
        status: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            collapsed: true,
            iconStyle: {
                'w-8 h-auto': true,
                'text-emerald-600': this.status,
                'text-rose-900': !this.status
            }
        }
    },
    methods: {
        collapseAccordion() {
            this.collapsed = !this.collapsed;
        }
    }, components: {
        CheckCircleIcon, XCircleIcon
    }
})
</script>