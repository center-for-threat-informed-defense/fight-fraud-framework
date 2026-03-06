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
      <h2 class="mb-4 mt-2">General Inquiries</h2>

      <div class="form flex flex-col gap-y-6">
        <div class="flex gap-x-4">
          <div class="flex flex-col w-full">
            <label for="first_name">First Name</label>
            <InputText id="first_name" />
          </div>
          <div class="flex flex-col w-full">
            <label for="last_name">Last Name</label>
            <InputText id="last_name" />
          </div>
        </div>

        <div class="flex flex-col w-full">
          <label for="email">Email</label>
          <InputText id="email" />
        </div>
        <div class="flex flex-col w-full">
          <label for="description">Question/Comment</label>
          <p class="description">What do you want to ask our team?</p>
          <PrimeTextarea id="description" />
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
import PrimeButton from "primevue/button"
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
  components: { InputText, PrimeTextarea, PrimeButton, BreadcrumbComponent },
  data() {
    return {
      breadcrumbItems: [
        { label: "Contact Us", route: "/contact-us" },
      ],
    };
  },
  computed: {

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
