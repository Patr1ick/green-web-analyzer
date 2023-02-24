<template>
    <div :class="borderClass">
        <XCircleIcon v-if="type == 'error'" class="w-8 text-rose-900" />
        <ExclamationCircleIcon v-if="type == 'information'" class="w-8 text-blue-600" />
        <QuestionMarkCircleIcon v-if="type == 'question'" class="w-8 text-blue-600" />
        <CheckCircleIcon v-if="type == 'success'" class="w-8 text-emerald-600" />
        <p class="grow">
            <slot>
                {{ message }}
            </slot>
        </p>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { ExclamationCircleIcon, CheckCircleIcon, QuestionMarkCircleIcon, XCircleIcon } from '@heroicons/vue/24/solid'

export default defineComponent({
    components: {
        ExclamationCircleIcon,
        CheckCircleIcon,
        QuestionMarkCircleIcon,
        XCircleIcon
    },
    props: {
        message: {
            type: String,
            required: false,
        },
        type: {
            type: String,
            required: true,
            validator(value: string) {
                return ['success', 'information', 'error', 'question'].includes(value);
            }
        }
    },
    computed: {
        borderClass() {
            return {
                'flex justify-between items-center w-1/2 rounded border bg-opacity-25 p-4': true,
                'border-rose-900 bg-rose-900': this.type == "error",
                'border-emerald-600 bg-emerald-600': this.type == "success",
                'border-blue-600 bg-blue-600': this.type == "information" || this.type == "question",

            }
        }
    }
})
</script>
