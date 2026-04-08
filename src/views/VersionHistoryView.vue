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
      <h1>Version History</h1>
      <p>The MITRE F3 catalog is versioned using a major.minor version schema. The major releases contain substantial
        updates to the framework, including new techniques or tactics. The minor version number incrememnts for small
        releases, which include typo and data corrections but not typically new content. </p>
      <p>Below are a list of versions of the ATT&CK website preserved for posterity, including a permalink to each
        release's download artifacts.</p>
      <h2>Current Version</h2>
      <div class="version">
        <div class="w-1/2 my-auto">
          <h3>MITRE F3 v1.0</h3>
          <p>April 2026 - Current</p>
        </div>

        <div class="grid grid-cols-2 w-1/2">
          <a :href="stixUrl" download="f3-financial-stix-v1" class="link-blue-external small">Download
            STIX</a>
          <a :href="navigatorUrl" download="f3-financial-navigator-v1" class="link-blue-external small">Download
            Navigator Layer</a>
          <a :href="jsonUrl" download="f3-financial-json-v1" class="link-blue-external small">Download JSON</a>
          <a :href="excelUrl" download="f3-financial-excel-v1" class="link-blue-external small">Download Excel</a>
        </div>

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
    const baseUrl = import.meta.env.BASE_URL
    return {
      stixUrl: `${baseUrl}f3-stix.json`,
      navigatorUrl: `${baseUrl}f3-navigator.json`,
      jsonUrl: `${baseUrl}f3-v1.json`,
      excelUrl: `${baseUrl}F3-v1.xlsx`,
      breadcrumbItems: [
        { label: "Resources", route: "/resources" },
        { label: "Version History", route: "/resources/versions" },
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

.version {
  @apply border-ctid-light-gray border-[1px] py-4 px-6 my-1 flex
}

.version h3 {
  @apply font-medium normal-case text-lg
}
</style>
