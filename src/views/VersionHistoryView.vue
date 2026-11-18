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
      <p>The MITRE F3 catalog is versioned using a major.minor version schema. Major releases contain substantial
        updates to the framework. Minor releases may include new or modified content, typo corrections, and data
        corrections.</p>
      <p>Below are versions of the F3 data preserved for historical reference, including permanent links to each
        release's download artifacts.</p>
      <h2>Current Version</h2>
      <div class="version">
        <div class="w-1/2 my-auto">
          <h3>MITRE F3 v{{ currentVersion }}</h3>
          <p>November 2026 - Current</p>
        </div>

        <div class="grid grid-cols-2 w-1/2">
          <a :href="stixUrl" :download="`f3-financial-stix-v${currentVersion}`" class="link-blue-external small">Download
            STIX</a>
          <a :href="navigatorUrl" :download="`f3-financial-navigator-v${currentVersion}`" class="link-blue-external small">Download
            Navigator Layer</a>
          <a :href="jsonUrl" :download="`f3-financial-json-v${currentVersion}`" class="link-blue-external small">Download JSON</a>
          <a :href="excelUrl" :download="`f3-financial-excel-v${currentVersion}`" class="link-blue-external small">Download Excel</a>
        </div>

      </div>

      <h2>Previous Versions</h2>
      <div class="version">
        <div class="w-1/2 my-auto">
          <h3>MITRE F3 v1.2</h3>
          <p>September 2026</p>
        </div>

        <div class="grid grid-cols-2 w-1/2">
          <a :href="v12StixUrl" download="f3-financial-stix-v1.2" class="link-blue-external small">Download
            STIX</a>
          <a :href="v12NavigatorUrl" download="f3-financial-navigator-v1.2" class="link-blue-external small">Download
            Navigator Layer</a>
          <a :href="v12JsonUrl" download="f3-financial-json-v1.2" class="link-blue-external small">Download JSON</a>
          <a :href="v12ExcelUrl" download="f3-financial-excel-v1.2" class="link-blue-external small">Download Excel</a>
        </div>
      </div>

      <div class="version">
        <div class="w-1/2 my-auto">
          <h3>MITRE F3 v1.1</h3>
          <p>June 2026</p>
        </div>

        <div class="grid grid-cols-2 w-1/2">
          <a :href="previousStixUrl" download="f3-financial-stix-v1.1" class="link-blue-external small">Download
            STIX</a>
          <a :href="previousNavigatorUrl" download="f3-financial-navigator-v1.1" class="link-blue-external small">Download
            Navigator Layer</a>
          <a :href="previousJsonUrl" download="f3-financial-json-v1.1" class="link-blue-external small">Download JSON</a>
          <a :href="previousExcelUrl" download="f3-financial-excel-v1.1" class="link-blue-external small">Download Excel</a>
        </div>
      </div>

    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import packageInfo from "../../package.json";

export default defineComponent({
  components: { BreadcrumbComponent },

  data() {
    const baseUrl = import.meta.env.BASE_URL
    const currentVersion = packageInfo.f3Version
    return {
      currentVersion,
      stixUrl: `${baseUrl}f3-stix-v${currentVersion}.json`,
      navigatorUrl: `${baseUrl}f3-navigator-v${currentVersion}.json`,
      jsonUrl: `${baseUrl}f3-v${currentVersion}.json`,
      excelUrl: `${baseUrl}f3-excel-v${currentVersion}.xlsx`,
      v12StixUrl: `${baseUrl}f3-stix-v1.2.json`,
      v12NavigatorUrl: `${baseUrl}f3-navigator-v1.2.json`,
      v12JsonUrl: `${baseUrl}f3-v1.2.json`,
      v12ExcelUrl: `${baseUrl}f3-excel-v1.2.xlsx`,
      previousStixUrl: `${baseUrl}f3-stix-v1.1.json`,
      previousNavigatorUrl: `${baseUrl}f3-navigator-v1.1.json`,
      previousJsonUrl: `${baseUrl}f3-v1.1.json`,
      previousExcelUrl: `${baseUrl}f3-excel-v1.1.xlsx`,
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
