<template>
  <div class=" flex h-full flex-col-reverse md:flex-row">
    <div class="sidebar">
      <h2><router-link to="/about">About</router-link></h2>
      <router-link to="/about/methodology">
        <h3>Design Principles</h3>
      </router-link>
      <router-link to="/about/contributors">
        <h3>Contributors</h3>
      </router-link>
      <router-link to="/contact-us">
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
      <h1>About</h1>

      <p>The F3 Framework is an authoritative, analyst-developed knowledge base of real-world fraud actor behavior as
        seen in fraud incidents experienced by banking institutions. Grounded in real-world fraud tactics and created by
        fraud fusion analysts, it consolidates key fraud knowledge into a structured, transparent, and operationally
        relevant resource. </p>

      <h2>Design Principles and Methodology</h2>
      <p>This page provides the motivation behind the creation of the F3 Framework, its design philosophy, the
        components contained within the knowledge base, and how it can be used. It is meant to be used as an
        authoritative source of information about F3, as well as to help guide how the framework is expanded and
        maintained. </p>
      <router-link to="/about/methodology" class="link-blue-external small">Learn More</router-link>

      <h2>Contributors</h2>
      <p>The F3 framework was developed in collaboration with members from Aviation ISAC, Citi, FS-ISAC, JPMorganChase,
        Lloyds Banking Group, Marsh, NRF, and Retail & Hospitality ISAC. </p>
      <router-link to="/about/contributors" class="link-blue-external small">Learn More</router-link>

      <h2>Contact Us</h2>
      <p>We welcome any feedback on the F3 Framework and its resources. We have dedicated forms to identify new
        techniques to be added to the framework, suggest updates to existing techniques, and more.</p>
      <router-link to="/contact-us" class="link-blue-external small">Contact Us</router-link>

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
      ],
    };
  },
  computed: {
  }
})

</script>

<style scoped>
a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}
</style>
