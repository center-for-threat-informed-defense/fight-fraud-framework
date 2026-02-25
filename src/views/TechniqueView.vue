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
        <div class="main">
            <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
            <h1> {{ technique.name }} <a v-if="technique.isAttack"
                    :href="'https://attack.mitre.org/techniques/' + technique.id + '/'" class="attack-indicator"
                    target="_blank">&</a></h1>
            <h2>Description</h2>
            <div class="markdown-html" v-html="renderedHtml(technique.description)"></div>
            <!-- for tactics: display list of techniques under the tactic -->
            <template v-if="technique.tactic && technique.techniques.length > 0">
                <h2>Technique<template v-if="technique.techniques.length > 1">s</template></h2>
                <ul>
                    <li v-for="t in technique.techniques" :key="t">
                        <router-link :to="'/technique/' + t">{{ getTechniqueData(t).name
                            }}</router-link>
                    </li>
                </ul>
            </template>

            <!-- if there are subtechniques, list them -->
            <template v-if="technique.subtechniques?.length > 0">
                <h2>Subtechnique<template v-if="technique.subtechniques?.length > 1">s</template></h2>
                <ul>
                    <li v-for="subtechnique in technique.subtechniques" :key="subtechnique">
                        <router-link :to="'/technique/' + subtechnique">{{ getTechniqueData(subtechnique).name
                            }}</router-link>
                    </li>
                </ul>
            </template>
            <!-- for techniques, display parent tactic -->
            <template v-if="!technique.tactic">
                <h2>Tactic<template v-if="parentTactic.length > 1">s</template></h2>
                <ul>
                    <li v-for="tactic in parentTactic" :key="tactic">
                        <router-link :to="'/tactic/' + tactic.id">{{ tactic.name
                            }}</router-link>
                    </li>
                </ul>
            </template>
            <div class="mt-8">
                <i class="pi pi-send text-ctid-gray mx-2"></i>
                <router-link :to="'/contact-us/update-technique/' + techniqueId">Suggest improvements to
                    this <template v-if="technique.tactic">tactic</template>
                    <template v-else>technique</template>
                </router-link>
            </div>
            <div>

            </div>
        </div>
        <div class="right-sidebar">

            <p class="sidebar-item">
                <span class="emphasis">ID: </span>
                {{ technique.id }}
            </p>

            <p v-if="technique.tactic && technique.techniques.length > 0" class="sidebar-item">
                <span class="emphasis">Technique<template v-if="technique.techniques.length > 1">s</template>: </span>
                <template v-for="(t, i) in technique.techniques" :key="t">
                    <router-link :to="'/technique/' + t">{{ getTechniqueData(t).name
                    }}</router-link>
                    <span v-if="i < technique.techniques.length - 1">, </span>
                </template>
            </p>
            <p v-if="technique.subtechniques?.length > 0" class="sidebar-item">
                <span class="emphasis">Subtechnique<template v-if="technique.subtechniques?.length > 1">s</template>:
                </span>
                <template v-for="(t, i) in technique.subtechniques" :key="t">
                    <router-link :to="'/technique/' + t">{{ getTechniqueData(t).name
                    }}</router-link>
                    <span v-if="i < technique.subtechniques.length - 1">, </span>
                </template>
            </p>
            <p v-if="!technique.tactic" class="sidebar-item">
                <span class="emphasis">Tactic<template v-if="parentTactic.length > 1">s</template>: </span>
                <template v-for="(tactic, i) in parentTactic" :key="tactic">
                    <router-link :to="'/tactic/' + tactic.id">{{ tactic.name
                    }}</router-link>
                    <span v-if="i < parentTactic.length - 1">, </span>
                </template>
            </p>
            <p class="sidebar-item">
                <span class="emphasis">Last Modified: </span>
                01/01/1900
            </p>
            <p class="sidebar-item">
                <span class="emphasis">Version: </span>
                v0.0
            </p>
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
            // Todo: add another label 
            { label: `${this.technique.name}`, route: `/technique/${this.$route.params.id}` }]
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
            return [this.matrixData.filter(i => i.tactic)[0]]

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

.sidebar h4, .sidebar-item h4 {
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

.attack-indicator {
    @apply text-ctid-red
}


.sidebar-item {
    @apply my-4
}

.sidebar-item .emphasis {
    @apply text-ctid-gray
}

.sidebar-item p {}
</style>
