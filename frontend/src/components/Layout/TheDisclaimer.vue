<template>
    <header v-if="showDisclaimer" class="flex justify-between items-center bg-rose-900 px-4">
        <span class="p-4 text-2xl text-center text-gray-200 font-bold">
            This page is still under development!
        </span>
        <XMarkIcon @click="hideDisclaimer" class="text-gray-200 w-10 h-auto m-4 hover:cursor-pointer" />
    </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { XMarkIcon } from '@heroicons/vue/24/outline';
import { mapState } from 'vuex';


export default defineComponent({
    computed: {
        ...mapState(['showDisclaimer'])
    },
    methods: {
        hideDisclaimer() {
            this.$store.commit('setShowDisclaimer', false);
        }
    },
    components: {
        XMarkIcon
    }
})

</script>