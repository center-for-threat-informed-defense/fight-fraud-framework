<template>
    <div class="matrix">
        <div class="tactic-row">
            <div class="tactic" v-for="tactic in tactics" :key="tactic.id">
                <h5>
                    <router-link :to="'/tactic/' + tactic.id">{{ tactic.id }}</router-link>
                    <span class="attack-indicator" v-if="tactic?.isAttack">&</span>
                </h5>
                <p>{{ tactic.name }}</p>
            </div>
        </div>
        <div class="technique-container">
            <div v-for="tactic in tactics" :key="tactic.id">
                <template v-for="tid in getTacticTechniques(tactic)" :key="tid">
                    <matrix-technique :techniqueId="tid" v-if="tid.split('.').length <= 1" />
                </template>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MatrixTechnique from "./MatrixTechnique.vue";
import json from "../data/matrix-data.json";

export default defineComponent({
    components: { MatrixTechnique },
    data() {
        return {
            matrixData: json
        };
    },
    computed: {
        tactics() {
            return this.matrixData.filter(i => i.tactic)
        }
    },
    methods: {
        getTacticTechniques(tactic) {
            const matches = [];
            this.matrixData.forEach(i => {
                if (i.tactics?.includes(tactic.id)) {
                    matches.push(i.id)
                }
            })
            return matches;
        }
    }
});
</script>

<style scoped>
.matrix {
    border-collapse: collapse !important;
}

.tactic-row {
    @apply flex border-collapse border-b-2 border-ctid-light-gray mb-2;
}

.tactic {
    @apply px-4 py-2 w-40;
}

.tactic h5 a {
    @apply text-ctid-blue mb-[2px] font-medium hover:text-ctid-navy;
}

.tactic p {
    @apply leading-none;
}

.technique-container {
    @apply flex gap-0;
}
</style>
