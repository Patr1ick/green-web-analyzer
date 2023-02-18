<template>
    <div :class="divStyle">
        <button @click="collapseAccordion" :class="buttonStyle">
            <CheckCircleIcon v-if="status" class="icon" :class="iconStyle" />
            <XCircleIcon v-else class="icon" :class="iconStyle" />
            <slot name="title">

            </slot>
            <PlusIcon v-if="collapsed" :class="iconStyle" />
            <MinusIcon v-else :class="iconStyle" />
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

import { PlusIcon, MinusIcon, CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/solid'

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
            divStyle: {
                'w-full m-2 border rounded': true,
                'border-emerald-600 text-emerald-600': this.status,
                'border-rose-900 text-rose-900': !this.status
            },
            buttonStyle: {
                'w-full flex justify-between items-center p-4 border rounded': true,
                'border-emerald-600 text-emerald-600': this.status,
                'border-rose-900 text-rose-900': !this.status
            },
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
        PlusIcon, MinusIcon, CheckCircleIcon, XCircleIcon
    }
})
</script>