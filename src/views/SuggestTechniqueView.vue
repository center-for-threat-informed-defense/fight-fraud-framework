<template>
  <div class="flex h-full flex-col-reverse md:flex-row">
    <div class="sidebar">
      <h2>Contact Us</h2>
      <router-link to="/contact-us/new-technique">
        <h3>Suggest a New Technique</h3>
      </router-link>
      <router-link to="/contact-us/update-technique">
        <h3>Suggest Technique Updates</h3>
      </router-link>
      <router-link to="/contact-us">
        <h3>General</h3>
      </router-link>
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />
      <h1>Contact Us</h1>
      <h2 class="mb-4 mt-2">Suggest a New Technique</h2>

      <div class="form flex flex-col gap-6">
        <div class="flex flex-col">
          <label for="technique_name">Technique Name</label>
          <p class="description"> Propose a name for your new technique.</p>
          <InputText id="technique_name" />
        </div>
        <div class="flex flex-col">
          <label for="technique_description">Technique Description</label>
          <p class="description"> Tell us more about your proposed technique.</p>
          <PrimeTextarea id="technique_description" />
        </div>
        <div class="flex flex-col">
          <label for="technique_rationale">Rationale</label>
          <p class="description">Why is this technique needed? What gap do you see in the existing F3 framework that
            requires this technique?</p>
          <PrimeTextarea id="technique_rationale" />
        </div>
        <div class="flex flex-col">
          <label for="tactic">Tactic</label>
          <p class="description">Which tactic should this technique be assigned to?</p>
          <PrimeSelect id="tactic" :options="tactics" optionLabel="name" optionValue="id" />
        </div>
        <PrimeButton class="rounded-none w-fit">Submit</PrimeButton>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import InputText from 'primevue/inputtext';
import PrimeTextarea from 'primevue/textarea';
import PrimeSelect from 'primevue/select';
import PrimeButton from "primevue/button"
import json from "../data/matrix-data.json";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
  components: { InputText, PrimeTextarea, PrimeSelect, PrimeButton, BreadcrumbComponent },
  data() {
    return {
      matrixData: json,
      breadcrumbItems: [
        { label: "Contact Us", route: "/contact-us" },
        { label: "Suggest A New Technique", route: "/contact-us/new-technique" },

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
a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}

label {
  @apply uppercase pb-0 text-lg;
  font-family: "Fira Sans Extra Condensed", sans-serif;
}

.description {
  @apply -mt-1 pt-0 text-sm mb-1
}

button {
  border-radius: 0;
  margin: auto;
  text-transform: uppercase;
  font-family: "Fira Sans Extra Condensed", sans-serif;

}
</style>
