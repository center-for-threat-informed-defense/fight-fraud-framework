<template>
  <div class="flex h-full flex-col-reverse md:flex-row">
    <div class="sidebar">
      <h2><router-link to="/about">About</router-link></h2>
      <router-link to="/about/methodology">
        <h3>Design Principles</h3>
      </router-link>
      <router-link to="/about/contributors">
        <h3>Contributors</h3>
      </router-link>
      <router-link to="/about/contact-us">
        <h3>Contact Us</h3>
      </router-link>
      <h2><router-link to="/resources">Resources</router-link></h2>
      <router-link to="/matrix">
        <h3>Matrix</h3>
      </router-link>
      <router-link to="/technique">
        <h3>Techniques</h3>
      </router-link>
      <router-link to="/tactic">
        <h3>Tactics</h3>
      </router-link>
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />
      <h1>Contact Us</h1>
      <p class="mt-6">Contact CTID with any questions or comments or to sign up to get more involved with CTID.</p>
      <a href="https://ctid.mitre.org/get-involved/#stay-informed" target="_blank" class="btn btn-external">Contact the
        Center <i class="pi pi-external-link"></i>
      </a>
      <p class="mt-6">F3 will expand and evolve over time, and we welcome your feedback on the F3 knowledge base and
        resources. We're particularly interested in feedback on any existing techniques or techniques used by fraud
        actors in real-world, cyber-based incidents that are not yet represented in F3. You can either email us with
        those suggestions or submit a GitHub issue. If you're submitting feedback on an existing technique, please
        include its name.</p>
      <div class="flex gap-2">
        <a href="mailto:ctid@mitre.org?subject=Fight%20Fraud%20Framework%20Feedback" target="_blank"
          class="btn btn-external">Email Us <i class="pi pi-external-link"></i>
        </a>
        <a href="https://github.com/center-for-threat-informed-defense/fight-financial-fraud/issues/new" target="_blank"
          class="btn btn-external">Submit a GitHub Issue <i class="pi pi-external-link"></i>
        </a>
      </div>
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
        { label: "About", route: "/about" },
        { label: "Contact Us", route: "/about/contact-us" },
      ],
    };
  },
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
