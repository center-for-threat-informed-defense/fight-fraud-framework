<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1><span class="highlight">{{ technique.id }}</span> {{ technique.name }} <a v-if="technique.isAttack"
                :href="'https://attack.mitre.org/techniques/' + technique.id + '/'" class="attack-indicator"
                target="_blank">&</a></h1>
        <h2>Description</h2>
        <div class="markdown-html" v-html="renderedHtml(technique.description)"></div>
        <template v-if="technique.subtechniques?.length > 0">
            <h2>Subtechniques</h2>
            <ul>
                <li v-for="subtechnique in technique.subtechniques" :key="subtechnique">{{ subtechnique }}</li>
            </ul>
        </template>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import json from "../data/matrix-data.json";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import MarkdownIt from 'markdown-it';

export default defineComponent({
    components: { BreadcrumbComponent },
    data() {
        return {
            matrixData: json,
            md: new MarkdownIt(),
            breadcrumbItems: [
                { label: "Techniques", route: "/techniques" },
                { label: `${this.$route.params.id}`, route: `/technique/${this.$route.params.id}` }
            ],

        };
    },
    computed: {
        techniqueId() {
            return this.$route.params.id;
        },
        technique() {
            return this.matrixData?.filter(i => i.id == this.techniqueId)[0]
        }
    },
    methods: {
        renderedHtml(data: string) {
            return this.md.render(data);
        }
    }
});
</script>

<style scoped>
.highlight {
    @apply text-ctid-blue font-medium
}
</style>
