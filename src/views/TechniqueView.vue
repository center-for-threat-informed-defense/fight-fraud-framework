<template>
    <div class="flex h-full">
        <div class="sidebar">
            <Accordion multiple :value="sidenavValue">
                <template v-for="tactic in tactics" :key="tactic.id">
                    <AccordionPanel :value="tactic.id">
                        <AccordionHeader> <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
                        </AccordionHeader>
                        <AccordionContent>list subtechniques here</AccordionContent>
                    </AccordionPanel>
                </template>
            </Accordion>

        </div>
        <div class="main-container">
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
        </div>

    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import json from "../data/matrix-data.json";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import MarkdownIt from 'markdown-it';
import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';

export default defineComponent({
    components: { BreadcrumbComponent, Accordion, AccordionContent, AccordionHeader, AccordionPanel },
    data() {
        return {
            matrixData: json,
            md: new MarkdownIt(),
            breadcrumbItems: [
                { label: "Techniques", route: "/techniques" },
                { label: `${this.$route.params.id}`, route: `/technique/${this.$route.params.id}` }
            ],
            sidenavValue: ['TA0003']

        };
    },
    computed: {
        techniqueId() {
            return this.$route.params.id;
        },
        technique() {
            return this.matrixData?.filter(i => i.id == this.techniqueId)[0]
        },
        tactics() {
            return this.matrixData.filter(i => i.tactic)
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

.main-container {
    @apply w-3/4 p-8 px-12 h-full
}

.sidebar {
    @apply w-1/4 block border-r-2 p-8 border-ctid-light-gray h-full
}


.sidebar h4 {
    @apply text-ctid-gray font-medium
}

.sidebar a {
    @apply text-ctid-blue hover:text-ctid-navy hover:underline
}
</style>
