<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mt-0" />
    <div>
        <h1>Fight Financial Fraud <span class="highlight">Matrix</span></h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
            magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
            commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
            anim id est laborum.</p>
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
                { label: "Matrix", route: "/resources/matrix" }
            ],
        }
    }
});
</script>

<style scoped></style>
