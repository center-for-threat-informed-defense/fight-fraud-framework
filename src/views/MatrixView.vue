<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mt-0" />
    <div>
        <h1>MITRE Fight Fraud Framework <span class="highlight">Matrix</span></h1>
        <p>The relationship between tactics, techniques, and sub-techniques used by financial fraud actors in cyber-based fraud incidents can be viewed in the F3 Matrix. The F3
            Matrix provides a visual representation of F3 tactics (these are the fraud actor's goals) and the different
            techniques under each tactic, which are actions fraud actors may use to achieve that goal. Some techniques
            can be expanded to show more specific sub-techniques that describe in more detail how those actions may be
            performed.
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
