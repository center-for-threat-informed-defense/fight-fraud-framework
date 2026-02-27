<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mt-0" />
    <div>
        <h1>Fight Financial Fraud <span class="highlight">Matrix</span></h1>
        <p>The F3 Matrix contains information on how adversaries move through an attack and provides a visual
            representation of where different techniques are classified. View information about techniques and how
            techniques and tactics interact on the Matrix page.
        </p>
    </div>
    <div class="mt-8">
        <matrix-container />
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MatrixContainer from "../components/MatrixContainer.vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
    components: { BreadcrumbComponent, MatrixContainer },
    data() {
        return {
            breadcrumbItems: [
                { label: "Resources", route: "/resources" },
                { label: "Matrix", route: "/matrix" }
            ],
        }
    }
});
</script>

<style scoped></style>
