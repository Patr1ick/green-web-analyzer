<template>
    <RequestResults v-if="!isLoaded" />
    <BasicCard v-else>
        <main>
            <h1>No Results loaded. Search or request a report to show a report</h1>
            <div>
                <BasicButton @click="$router.push('/request')">
                    Request
                </BasicButton>
                <BasicButton @click="$router.push('/search')">
                    Search
                </BasicButton>
            </div>
        </main>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    computed: {
        isLoaded() {
            return this.$store.getters.isResultNull;
        }
    },
    components: {
        // RequestResults
    }
})
</script>

<style scoped>
main {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 90%;
    margin: auto;
}

div {
    margin: 1em;
}
</style>