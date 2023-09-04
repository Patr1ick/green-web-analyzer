<template>
    <div :class="borderClass">
        <div class="col-span-1 p-2">
            <XCircleIcon v-if="type == 'error'" class=" w-10 text-rose-900" />
            <ExclamationCircleIcon v-if="type == 'information'" class="w-10 text-blue-600" />
            <QuestionMarkCircleIcon v-if="type == 'question'" class="w-10 text-blue-600" />
            <CheckCircleIcon v-if="type == 'success'" class="w-10 text-emerald-600" />
        </div>
        <div class="col-span-11 p-2">
            <slot>
                {{ message }}
            </slot>
        </div>
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
                'grid grid-cols-12 justify-items-center items-center w-full w-full h-fit rounded border bg-opacity-25 p-2 text-center': true,
                'border-rose-900 bg-rose-900': this.type == "error",
                'border-emerald-600 bg-emerald-600': this.type == "success",
                'border-blue-600 bg-blue-600': this.type == "information" || this.type == "question",

            }
        }
    }
})
</script>
