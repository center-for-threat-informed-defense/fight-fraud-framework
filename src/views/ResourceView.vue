<template>
  <div class="flex h-full flex-col-reverse md:flex-row">
    <div class="sidebar">
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
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />
      <h1>Resources</h1>
      <h2>Download Data</h2>
      <p>Want to download the F3 framework to use in other Center for Threat-Informed Defense or MITRE ATT&CK tools?
        These download links provide you access to the data in all the formats you could need. </p>
      <div class="flex gap-8"><a href="f3-stix.json" download="f3-financial-stix-v1"
          class="link-blue-external small">Download
          STIX</a>
        <a href="f3-navigator.json" download="f3-financial-navigator-v1" class="link-blue-external small">Download
          Navigator Layer</a>
        <a href="f3-v1.json" download="f3-financial-json-v1" class="link-blue-external small">Download JSON</a>
        <a href="F3-v1.xlsx" download="f3-financial-excel-v1" class="link-blue-external small">Download Excel</a>

      </div>
      <h2>F3 Matrix</h2>
      <p>The F3 Matrix contains information on how adversaries move through an attack and provides a visual
        representation of where different techniques are classified. View information about techniques and how
        techniques and tactics interact on the Matrix page.</p>
      <router-link to="/matrix" class="link-blue-external small">Learn More</router-link>

      <h2>Tactic List</h2>
      <p>View a list of all tactics in the F3 framework. Tactics represent the "why" of an F3 technique or
        sub-technique. It is the adversary's tactical goal: the reason for performing an action. For example, an
        adversary may want to achieve credential access.</p>
      <router-link to="/tactic" class="link-blue-external small">Learn More</router-link>

      <h2>Technique List</h2>
      <p>View a list of all techniques in the F3 framework. Techniques represent 'how' an adversary achieves a tactical
        goal by performing an action. For example, an adversary may dump credentials to achieve credential access.</p>
      <router-link to="/technique" class="link-blue-external small">Learn More</router-link>


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
  }
})

</script>

<style scoped>
a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}
</style>
