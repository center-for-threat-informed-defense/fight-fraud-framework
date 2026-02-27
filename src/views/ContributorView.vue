<template>
  <div class="flex h-full flex-1">
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
      <h1>Contributors</h1>

      <p>The F3 framework was developed in collaboration with members from Aviation ISAC, Citi, FS-ISAC, JPMorganChase,
        Lloyds Banking Group, Marsh, NRF, and Retail & Hospitality ISAC.</p>
      <div class="flex gap-4 my-10">
        <div v-for="person of contributors" :key="person.name" class="w-60">
          <img :src="person.img" />
          <h2 class="mt-2 mb-1 leading-none">{{ person.name }}</h2>
          <p class="leading-none">{{ person.role }}, {{ person.company }}</p>
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
    return {
      breadcrumbItems: [
        { label: "About", route: "/about" },
        { label: "Project Contributors", route: "/about/contributors" },
      ],
      contributors: [
        {
          name: "Suneel Sundar",
          role: "Director of R&D",
          company: "CTID",
          img: "https://ctid.mitre.org/img/team/suneel_sundar.jpg"
        },
        {
          name: "Mike Cunningham",
          role: "R&D Program Manager",
          company: "CTID",
          img: "https://ctid.mitre.org/img/team/mike_cunningham.png",
        },
        {
          name: "Tiffany Bergeron",
          role: "Chief Architect, Mappings Program",
          company: "CTID",
          img: "https://ctid.mitre.org/img/team/tiffany_bergeron.jpg",
        },
        // {
        //   name: "",
        //   role: "",
        //   company: "",
        //   img: "",
        // }
      ]
    };
  },
  computed: {
  }
})

</script>

<style scoped>
.main {
  @apply w-full block
}

.sidebar {
  @apply border-r-2 border-ctid-light-gray mr-6 pr-6 w-1/4;
}

a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}
</style>
