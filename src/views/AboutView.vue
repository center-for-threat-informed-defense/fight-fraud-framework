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
      <h1>About</h1>

      <p>MITRE F3™ is an authoritative, analyst-developed knowledge base of fraud actor behavior as observed in
        cyber-based fraud incidents. These incidents involve the intentional use of deceptive or illegal practices to fraudulently obtain money, assets, or information from individuals or institutions, and include actions carried out over cyber channels. Grounded in real-world fraud tactics and created by fraud fusion analysts, it
        consolidates key fraud knowledge into a structured, transparent, and operationally relevant resource. </p>

      <h2>Design Principles and Methodology</h2>
      <p>The Design Principles and Methodology describe the motivation behind the creation of F3, its design philosophy,
        the components contained within the knowledge base, and how it can be used. It is meant to be used as an
        authoritative source of information about F3, as well as to help guide how the framework is expanded and
        maintained.</p>
      <router-link to="/about/methodology" class="link-blue-external small">Learn More</router-link>

      <h2>Contributors</h2>
      <p>F3 has been developed in collaboration with CTID members from Aviation Information Sharing and Analysis Center
        (A-ISAC), Citi, CrowdStrike, Financial Services ISAC (FS-ISAC), JPMorganChase, Lloyds Banking Group, Marsh,
        National Retail Federation (NRF), Retail & Hospitality ISAC (RH-ISAC), Standard Chartered, and Verizon Business.
        CTID also recognizes Group-IB as a key
        data contributor. </p>
      <router-link to="/about/contributors" class="link-blue-external small">Learn More</router-link>

      <h2>Contact Us</h2>
      <p>F3 will expand and evolve over time, and we welcome your feedback on the F3 knowledge base and resources. If
        you have information regarding cyber fraud behavior you think may be useful, we would like to hear from you.</p>
      <router-link to="/about/contact-us" class="link-blue-external small">Contact Us</router-link>

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
