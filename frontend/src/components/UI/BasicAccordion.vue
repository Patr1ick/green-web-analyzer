<template>
    <!-- <BasicCard> -->
    <div :class="style">
        <button @click="collapseAccordion" :class="style">
            <CheckCircleIcon v-if="applicable" class="icon" :class="style" />
            <XCircleIcon v-else class="icon" :class="style" />
            <slot name="title">

            </slot>
            <PlusIcon v-if="collapsed" class="icon" />
            <MinusIcon v-else class="icon" />
        </button>
        <section v-if="!collapsed">
            <slot name="description">

            </slot>
            <slot name="details">

            </slot>
        </section>
    </div>
    <!-- </BasicCard> -->
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { PlusIcon, MinusIcon, CheckCircleIcon, XCircleIcon } from '@heroicons/vue/24/outline'

export default defineComponent({
    props: {
        applicable: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            collapsed: true,
            style: {
                'border-emerald-600': this.applicable,
                'border-rose-600': !this.applicable
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

<style scoped>
.icon {
    width: 2em;
    height: auto;
}

.icon.red {
    color: #BD3808;
}

.icon.green {
    color: #1abc9c;
}

div {
    width: 100%;
    border-radius: 0.25em;
    border: 0.1em solid #1abc9c;
    margin: 0.5em;
}


section {
    padding: 1em;
}

button {
    width: 100%;
    color: #666666;
    background-color: transparent;
    border-radius: 0.125em;
    border: 0.1em solid;
    height: 5vh;
    cursor: pointer;

    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0em 1em;
}

button:hover.green {
    background-color: #1abc9c10;
}

button:hover.red {
    background-color: #bd380810;
}

.v-enter-active,
.v-leaver-active {
    transition: height 2s ease-in-out;
}
</style>