<template>
  <div class="flex">
    <div class="sidebar">
      <h2>Resources</h2>
      <router-link to="/contact-us/new-technique">
        <h3>Contact Us</h3>
      </router-link>
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />

      <p>Resource page</p>
    </div>
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
        { label: "Resources", route: "/resources" },
      ],
    };
  },
  computed: {
    tactics() {
      return this.matrixData.filter(i => i.tactic)
    },
  }
})

</script>

<style scoped>
.main {
  @apply w-full block
}

.sidebar {
  @apply border-r-2 border-ctid-light-gray h-screen mr-6 pr-6 w-1/4;
}

a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}
</style>
