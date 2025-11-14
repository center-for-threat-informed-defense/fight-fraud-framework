<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1><span class="highlight">{{ technique.id }}</span> {{ technique.name }}</h1>
        <h2>Description</h2>
        <p>{{ technique.description }}</p>
        <template v-if="technique.subtechniques">
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

export default defineComponent({
    components: { BreadcrumbComponent },
    data() {
        return {
            matrixData: json,
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
    }
});
</script>

<style scoped>
.highlight {
    @apply text-ctid-blue font-medium
}
</style>
