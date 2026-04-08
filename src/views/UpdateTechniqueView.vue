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
      <h2 class="mb-4 mt-2">Suggest Updates to Technique</h2>

      <div class="form flex flex-col gap-6">
        <div class="flex flex-col">
          <label for="technique">Technique Name</label>
          <p class="description">Which technique do you want to give feedback on?</p>
          <PrimeSelect id="technique" :options="techniques" optionLabel="name" optionValue="id" v-model="techniqueId" />
        </div>
        <div class="flex flex-col">
          <label for="feedback">Feedback</label>
          <p class="description">What needs to be changed about this technique?</p>
          <PrimeTextarea id="feedback" v-model="feedback" />
        </div>
        <PrimeButton class="rounded-none w-fit">Submit</PrimeButton>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import PrimeTextarea from 'primevue/textarea';
import PrimeSelect from 'primevue/select';
import PrimeButton from "primevue/button"
import json from "../data/matrix-data.json";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
  components: { PrimeTextarea, PrimeSelect, PrimeButton, BreadcrumbComponent },
  data() {
    return {
      breadcrumbItems: [
        { label: "Contact Us", route: "/contact-us" },
        { label: "Suggest Technique Updates", route: "/contact-us/update-technique" },

      ],
      matrixData: json,
      feedback: null,
    };
  },
  computed: {
    techniques() {
      return this.matrixData
    },
    techniqueId() {
      return this.$route.params.id;
    }
  }
})

</script>

<style scoped>
label {
  @apply uppercase pb-0 text-lg;
  font-family: "Fira Sans Extra Condensed", sans-serif;
}

.description {
  @apply -mt-1 pt-0 text-sm mb-1
}

a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}

button {
  border-radius: 0;
  margin: auto;
  text-transform: uppercase;
  font-family: "Fira Sans Extra Condensed", sans-serif;

}
</style>
