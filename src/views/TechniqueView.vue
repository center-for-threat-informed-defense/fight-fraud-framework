<template>
    <div class="flex h-full">
        <div class="sidebar">
            <Accordion multiple :value="sidenavValue">
                <template v-for="tactic in tactics" :key="tactic.id">
                    <AccordionPanel :value="tactic.id">
                        <AccordionHeader> <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
                        </AccordionHeader>
                        <AccordionContent>
                            <ul v-if="tactic.techniques">
                                <li v-for="technique of tactic.techniques" :key="technique">
                                    <router-link :to="'/technique/' + technique">{{ getTechniqueData(technique).name
                                    }}</router-link>
                                </li>
                            </ul>
                        </AccordionContent>
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

                <h2>Detection Source</h2>
                <p>put detection information here</p>

                <h2>Mitigation</h2>
                <p>put mitigation information here</p>

                <h2>Tactics</h2>
                <ul>
                    <li v-for="tactic in [parentTactic]" :key="tactic">
                        <router-link :to="'/tactic/' + tactic.id">{{ tactic.name
                            }}</router-link>
                    </li>
                </ul>

                <template v-if="technique.subtechniques?.length > 0">
                    <h2>Subtechniques</h2>
                    <ul>
                        <li v-for="subtechnique in technique.subtechniques" :key="subtechnique">
                            <router-link :to="'/technique/' + subtechnique">{{ getTechniqueData(subtechnique).name
                                }}</router-link>
                        </li>
                    </ul>
                </template>
                <h2>References</h2>
                <ul>
                    <li>
                        <a href="/">this is a link to a reference</a>

                    </li>
                </ul>
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
        };
    },
    computed: {
        breadcrumbItems() {
            return [this.technique.tactic ? { label: "Tactics", route: "/tactic" } : { label: "Techniques", route: "/technique" },
            { label: `${this.$route.params.id}`, route: `/technique/${this.$route.params.id}` }]
        },
        techniqueId() {
            return this.$route.params.id;
        },
        technique() {
            return this.matrixData?.filter(i => i.id == this.techniqueId)[0]
        },
        tactics() {
            return this.matrixData.filter(i => i.tactic)
        },
        parentTactic() {
            // until we have actual tactics assigned to each technique, currently this is always tactic TA0001
            return this.matrixData.filter(i => i.tactic)[0]

        },
        sidenavValue() {
            return [this.parentTactic.id]
        }
    },
    methods: {
        renderedHtml(data: string) {
            return this.md.render(data);
        },
        getTechniqueData(id: string) {
            return this.matrixData.filter(i => i.id === id)[0]
        }
    }
});
</script>

<style scoped>
.highlight {
    @apply text-ctid-blue font-medium
}

.main-container {
    @apply w-3/4 p-8 px-12 h-full border-l-2 border-ctid-light-gray
}

.sidebar {
    @apply w-1/4 block p-8 h-full flex-1
}


.sidebar h4 {
    @apply text-ctid-gray font-medium
}

a {
    @apply text-ctid-blue hover:text-ctid-navy hover:underline
}

ul {
    @apply ml-4
}

li {
    @apply my-1 leading-snug
}
</style>
