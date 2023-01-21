<template>
    <BasicCard class="main">
        <main>
            <h1>Green IT: Development of a tool for checking the data efficiency and economy of websites</h1>
            <p>
                Climate catastrophe is a current threat to the planet. The IT sector must also make its contribution to
                reducing greenhouse gas emissions. Even if this is primarily done by switching power generation to
                renewable
                energies, energy consumption can be reduced through optimization and data reduction. This tool should
                help
                to check certain typical criteria of websites, which can be improved.
            </p>
            <b>This project is a part of a student research project of the DHBW Stuttgart and the Mercedes-Benz Tech
                Innovation</b>
        </main>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style scoped>
.main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 1em;
    margin-bottom: 1em;
    padding: 4em;
}
</style>