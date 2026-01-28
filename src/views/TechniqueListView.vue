<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1>Techniques</h1>

    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
    components: { BreadcrumbComponent },
    data() {
        return {
            breadcrumbItems: [
                { label: "Techniques", route: "/techniques" },
            ],
        }
    }
});
</script>

<style scoped></style>
