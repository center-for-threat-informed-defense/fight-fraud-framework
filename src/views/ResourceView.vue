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
      <p>F3 data can be used in several ways to foster collaboration and shared understanding across teams that may each
        have their own tools and processes. You may also want to use F3 data with other CTID or MITRE ATT&CK ® tools.
        These download links provide you F3 data in various formats to explore cyber fraud TTPs, describe incidents, and
        coordinate efforts.</p>
      <div class="flex gap-8"><a :href="stixUrl" download="f3-stix-v1" class="link-blue-external small">Download
          STIX</a>
        <a :href="navigatorUrl" download="f3-navigator-v1" class="link-blue-external small">Download
          Navigator Layer</a>
        <!-- <a href="f3-v1.json" download="f3-json-v1" class="link-blue-external small">Download JSON</a> -->
        <a :href="excelUrl" download="f3-excel-v1" class="link-blue-external small">Download Excel</a>

      </div>
      <h2>F3 Matrix</h2>
      <p>The F3 Matrix provides a visual representation of the relationship between tactics, techniques, and
        sub-techniques. View information about techniques and how techniques and tactics interact on the Matrix page.
      </p>
      <router-link to="/matrix" class="link-blue-external small">Learn More</router-link>

      <h2>Tactic List</h2>
      <p>View a list of all F3 tactics. Tactics represent the "why" of an F3 technique or sub-technique: the fraud
        actor's tactical goal and the reason for performing an action. For example, a fraud actor may conduct resource
        development to establish infrastructure or capabilities to support fraud activities.</p>
      <router-link to="/tactic" class="link-blue-external small">Learn More</router-link>

      <h2>Technique List</h2>
      <p>View a list of all F3 techniques. Techniques represent 'how' a fraud actor achieves a tactical goal by
        performing an action. For example, a fraud actor may create fake materials such as forged documents and
        supporting artifacts to prepare for attempting fraud.</p>
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
    const baseUrl = import.meta.env.BASE_URL
    return {
      stixUrl: `${baseUrl}f3-stix.json`,
      navigatorUrl: `${baseUrl}f3-navigator.json`,
      excelUrl: `${baseUrl}F3-v1.xlsx`,
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
