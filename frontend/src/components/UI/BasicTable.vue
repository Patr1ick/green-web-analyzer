<template>
    <table>
        <tr>
            <th v-for="t in title" :key="t">{{ t }}</th>
        </tr>
        <tr v-for="d in data" :key="d[0]">
            <td v-for="key in arrayKeys" :key="key">
                <a v-if="key == 'url'" :href="d[key]">
                    {{ d[key] }}
                </a>
                <img v-else-if="key == 'img'" :src="d['url']" />
                <p v-else-if="bytes.includes(key)">
                    {{ convert(d[key]) }}
                </p>
                <p v-else>
                    {{ d[key] }}
                </p>
            </td>
        </tr>
    </table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import convertBytesToString from '../../utils/functions'

export default defineComponent({
    props: {
        data: {
            type: Array<any>,
            required: true
        },
        title: {
            type: Array<string>,
            required: true
        },
        arrayKeys: {
            type: Array<string>,
            required: true
        },
        bytes: {
            type: Array<string>,
            required: false,
            default() {
                return [];
            }
        }
    }, methods: {
        convert(bytes: number){
            return convertBytesToString(bytes);
        }
    }
})
</script>

<style scoped>
table {
    table-layout: fixed;
}

td,
th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

th {
    background-color: #dddddd;
}

img {
    width: 10em;
}
</style>