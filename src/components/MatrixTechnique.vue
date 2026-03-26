<template>
    <div class="flex box-border items-stretch">

        <div :class="['technique', { 'supertechnique': technique?.subtechniques?.length > 0 }]">
            <p><router-link :to="'/technique/' + techniqueId">
                    {{ technique?.name }}

                </router-link>
                <span class="attack-indicator" v-if="technique?.isAttack">&</span>
            </p>
        </div>
        <div v-if="technique?.subtechniques?.length > 0" class="expand-btn" @click="clickExpand">
            <span v-if="isOpen">-</span>
            <span v-else>+</span>
        </div>
        <div v-else-if="isSubtechnique" class="subtechnique-border"></div>
        <div v-else class="spacer"></div>
    </div>
    <div v-if="isOpen">
        <template v-for="subtechnique in technique?.subtechniques" :key="subtechnique">
            <matrix-technique :techniqueId="subtechnique" :isSubtechnique="true" />
        </template>
    </div>

</template>

<script lang="ts">
import { defineComponent } from "vue";
import json from "../data/matrix-data.json";

export default defineComponent({
    components: {},
    data() {
        return {
            matrixData: json,
            isOpen: false,
        };
    },
    props: {
        techniqueId: String,
        isSubtechnique: {
            type: Boolean,
            default: false,
        }
    },
    computed: {
        technique() {
            return this.matrixData?.filter(i => i.id == this.techniqueId)[0]
        }
    },
    methods: {
        clickExpand() {
            this.isOpen = !this.isOpen;
        }
    }
});
</script>

<style scoped>
.technique {
    @apply w-[144px] px-2 py-2 border-ctid-light-gray border-[1px] -mb-[1px] box-border
}

.technique a {
    @apply text-ctid-blue font-medium hover:text-ctid-navy;
}

.technique p {
    @apply leading-none text-sm;
}

.expand-btn {
    @apply w-3 bg-ctid-light-gray text-white border-ctid-light-gray border-2 box-border cursor-pointer flex;
}

.spacer {
    @apply w-3;
}

.subtechnique-border {
    @apply w-1 mr-auto bg-ctid-light-gray;
}

.expand-btn span {
    @apply m-auto text-center;
}
</style>
