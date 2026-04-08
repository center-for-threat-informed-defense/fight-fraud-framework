<template>
    <div class="flex h-full flex-col md:flex-row">
        <div class="sidebar hidden md:block">
            <Accordion multiple :value="sidenavValue">
                <template v-for="tactic in tactics" :key="tactic.id">
                    <AccordionPanel :value="tactic.id">
                        <AccordionHeader> <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
                        </AccordionHeader>
                        <AccordionContent>
                            <ul v-if="getTacticTechniques(tactic)">
                                <li v-for="technique of getTacticTechniques(tactic)" :key="technique">
                                    <router-link :to="'/technique/' + technique">{{ getTechniqueData(technique)?.name
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
            <h1> {{ technique?.name }} <a v-if="technique.isAttack" :href="getAttackURL()" class="attack-indicator"
                    target="_blank">&</a></h1>
            <h2>Description</h2>
            <div class="markdown-html" v-html="renderedHtml(technique.description)"></div>
            <!-- for tactics: display list of techniques under the tactic -->
            <template v-if="technique.tactic && getTacticTechniques(technique).length > 0">
                <h2>Technique<template v-if="getTacticTechniques(technique).length > 1">s</template></h2>
                <ul>
                    <li v-for="t in getTacticTechniques(technique)" :key="t">
                        <router-link :to="'/technique/' + t">{{ getTechniqueData(t)?.name
                            }}</router-link>
                    </li>
                </ul>
            </template>

            <!-- if there are subtechniques, list them -->
            <template v-if="technique.subtechniques?.length > 0">
                <h2>Subtechnique<template v-if="technique.subtechniques?.length > 1">s</template></h2>
                <ul>
                    <li v-for="subtechnique in technique.subtechniques" :key="subtechnique">
                        <router-link :to="'/technique/' + subtechnique">{{ getTechniqueData(subtechnique)?.name
                            }}</router-link>
                    </li>
                </ul>
            </template>
            <!-- for techniques, display parent tactic -->
            <template v-if="!technique.tactic">
                <h2>Tactic<template v-if="technique.tactics.length > 1">s</template></h2>
                <ul>
                    <li v-for="tactic in technique.tactics" :key="tactic">
                        <router-link :to="'/tactic/' + tactic">{{ getTechniqueData(tactic).name
                            }}</router-link>
                    </li>
                </ul>
            </template>
            <div class="mt-8">
                <i class="pi pi-wrench text-ctid-gray mx-2"></i>
                <a
                    :href="'mailto:ctid@mitre.org?subject=Fight%20Fraud%20Framework%20Feedback:%20' + technique.name.replaceAll(' ', '%20')">Suggest
                    improvements to
                    this <template v-if="technique.tactic">tactic</template>
                    <template v-else>technique</template>
                </a>
            </div>
            <div v-if="searchResults && searchResults.length > 0">
                <h2>Didn't find what you're looking for?</h2>
                <p class=" -mt-2 mb-2">Check out some other results from your most recent search</p>
                <div class="result-row">
                    <div v-for="result of searchResults" :key="result.id" class="suggested-result">
                        <h3><router-link :to="'/technique/' + result.id">{{ result.name }}</router-link></h3>
                        <p>{{ truncatedDescription(result.description) }}</p>
                        <router-link :to="'/technique/' + result.id" class="link-blue-external small">View
                            Page</router-link>

                    </div>
                </div>
            </div>
        </div>
        <div class="right-sidebar">

            <p class="sidebar-item">
                <span class="emphasis">ID: </span>
                {{ technique.id }}
            </p>

            <p v-if="technique.tactic && getTacticTechniques(technique).length > 0" class="sidebar-item">
                <span class="emphasis">Technique<template v-if="getTacticTechniques(technique).length > 1">s</template>:
                </span>
                <template v-for="(t, i) in getTacticTechniques(technique)" :key="t">
                    <router-link :to="'/technique/' + t">{{ getTechniqueData(t).name
                    }}</router-link>
                    <span v-if="i < getTacticTechniques(technique).length - 1">, </span>
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
                <span class="emphasis">Tactic<template v-if="technique.tactics.length > 1">s</template>: </span>
                <template v-for="(tactic, i) in technique.tactics" :key="tactic">
                    <router-link :to="'/tactic/' + tactic">{{ getTechniqueData(tactic).name
                    }}</router-link>
                    <span v-if="i < technique.tactics.length - 1">, </span>
                </template>
            </p>
            <p class="sidebar-item">
                <span class="emphasis">Last Modified: </span>
                {{ technique?.lastModified ? new Date(technique.lastModified).toLocaleDateString() : null }}
            </p>
            <p class="sidebar-item">
                <span class="emphasis">Version: </span>
                v{{ technique?.version }}
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
            console.log("finding match ", this.matrixData?.filter(i => i.id == this.techniqueId)[0])
            return this.matrixData?.filter(i => i.id == this.techniqueId)[0]
        },
        tactics() {
            return this.matrixData.filter(i => i.tactic)
        },
        sidenavValue() {
            if (this.technique.tactic) {
                return [this.technique.id]
            }
            return [this.technique.tactics[0]]
        },
        searchQuery() {
            const searchBar = document.getElementById('search-bar');
            if (searchBar.value) {
                return searchBar.value
            }
            return null;
        },
        searchResults() {
            if (!this.searchQuery) {
                return null;
            }
            let matches = [];
            this.matrixData.forEach((i) => {
                let matchScore = 0;
                const regex = new RegExp(this.searchQuery, "gi");

                if (i.id.match(regex)) {
                    matchScore += 5;
                }

                if (i.name.match(regex)) {
                    const count = i.description.match(regex);
                    matchScore += 3 * count?.length;
                }
                if (i.description.match(regex)) {
                    const count = i.description.match(regex);
                    matchScore += count.length;
                }

                if (matchScore > 0) {
                    matches.push({
                        ...i,
                        searchScore: matchScore
                    })
                }
            })
            // remove current item from search results
            matches = matches.filter(m => m.id !== this.techniqueId)
            matches = matches.sort((a, b) => b.searchScore - a.searchScore);
            return matches.slice(0, 3)
        },

    },
    methods: {
        renderedHtml(data: string) {
            return this.md.render(data);
        },
        truncatedDescription(text: string) {
            if (!text) return null;
            const words = text?.split(' ');
            if (words.length > 25) {
                return words.slice(0, 25).join(' ') + '...';
            }
            return text;

        },
        getTechniqueData(id: string) {
            return this.matrixData.filter(i => i.id === id)[0]
        },
        getTacticTechniques(tactic) {
            const matches = [];
            this.matrixData.forEach(i => {
                if (i.tactics?.includes(tactic.id)) {
                    matches.push(i.id)
                }
            })
            return matches;
        },
        getAttackURL() {
            if (this.technique.tactic) {
                return 'https://attack.mitre.org/tactics/' + this.technique.id + '/'
            }
            return 'https://attack.mitre.org/techniques/' + this.technique.id.replace(".", "/") + '/'
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

.result-row {
    @apply xl:flex block gap-2;
}

.suggested-result {
    @apply border-ctid-light-gray border-[1px] py-4 px-6 my-1;
    width: auto
}

.suggested-result h3 {
    @apply text-lg font-medium
}
</style>
