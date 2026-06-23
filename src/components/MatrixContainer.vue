<template>
    <div class="matrix">
        <div class="tactic-row">
            <div class="tactic" v-for="tactic in tactics" :key="tactic.id">
                <p>
                    <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
                    <span class="attack-indicator" v-if="tactic?.isAttack">&</span>
                </p>
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
            const tactics = this.matrixData.filter(i => i.tactic);
            const stealthIndex = tactics.findIndex(tactic => tactic.id === "TA0005");
            const defenseImpairmentIndex = tactics.findIndex(tactic => tactic.id === "TA0112");

            if (stealthIndex === -1 || defenseImpairmentIndex === -1) {
                return tactics;
            }

            const orderedTactics = [...tactics];
            const [defenseImpairment] = orderedTactics.splice(defenseImpairmentIndex, 1);
            const updatedStealthIndex = orderedTactics.findIndex(tactic => tactic.id === "TA0005");
            orderedTactics.splice(updatedStealthIndex + 1, 0, defenseImpairment);

            return orderedTactics;
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
    width: 100%;
    overflow-x: scroll;
    overflow-y: visible;
}

.tactic-row {
    @apply flex border-collapse border-b-2 border-ctid-light-gray mb-2 mx-auto w-fit;
}

.tactic {
    @apply px-2 py-2 w-40 mt-auto flex;
}

.tactic p a {
    @apply text-ctid-blue mb-[2px] font-medium hover:text-ctid-navy;
}

.tactic p {
    @apply leading-none align-bottom mt-auto;
}

.technique-container {
    @apply flex gap-1 mx-auto w-fit pb-10;
}
</style>
