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
      <h1>Contributors</h1>

      <p>The MITRE Fight Fraud Framework (F3)™ was developed through MITRE’s Center for Threat-Informed Defense (CTID)
        and CTID member-powered collaboration. With the understanding that the challenges we face are bigger than
        ourselves, our members join CTID prepared to tackle hard problems in a uniquely collaborative environment. CTID
        gratefully acknowledges the significant contributions and deep expertise provided by Aviation Information
        Sharing and Analysis Center (A-ISAC), Citi, CrowdStrike, Financial Services ISAC (FS-ISAC), JPMorganChase,
        Lloyds Banking Group, Marsh, National Retail Federation (NRF), Retail & Hospitality ISAC (RH-ISAC), Standard
        Chartered, and Verizon Business towards the development of MITRE F3™. CTID further recognizes Group-IB as a key
        data contributor whose insights and contributions supported the development of F3.</p>

      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 my-10 gap-x-20 gap-y-10">
        <div v-for="contributor of contributors" :key="contributor.name" class="contributor">
          <img :src="contributor.img" />
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import groupIB from "@/assets/Group-IB.png";

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
          name: "Aviation ISAC",
          link: "",
          img: "https://ctid.mitre.org/img/participants/a_isac.png"
        },
        {
          name: "Citi",
          link: "",
          img: "https://ctid.mitre.org/img/participants/citi.png",
        },
        {
          name: "Crowdstrike",
          link: "",
          img: "https://ctid.mitre.org/img/participants/crowdstrike.png",
        },
        {
          name: "FS-ISAC",
          link: "",
          img: "https://ctid.mitre.org/img/participants/fs_isac.png",
        },
        {
          name: "Group-IB",
          link: "",
          img: groupIB
        }, {
          name: "JPMorganChase",
          link: "",
          img: "https://ctid.mitre.org/img/participants/jp_morgan.png",
        }
        , {
          name: "Lloyds Banking Group",
          link: "",
          img: "https://ctid.mitre.org/img/participants/lloyds.png",
        },

        {
          name: "Marsh",
          link: "",
          img: "https://ctid.mitre.org/img/participants/marsh.png",
        },
        {
          name: "NRF",
          link: "",
          img: "https://ctid.mitre.org/img/participants/nrf.png",
        }, {
          name: "Retail & Hospitality ISAC",
          link: "",
          img: "https://ctid.mitre.org/img/participants/retail_hospitality_isac.png",
        },
        {
          name: "Standard Chartered",
          link: "",
          img: "https://ctid.mitre.org/img/participants/standard_chartered.png",
        },
        {
          name: "Verizon Business",
          link: "",
          img: "https://ctid.mitre.org/img/participants/verizon.png",
        }
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

a h3 {
  @apply text-ctid-blue hover:text-ctid-navy
}

.contributor {
  @apply flex w-full h-20
}

.contributor img {
  @apply m-auto h-20 w-auto object-contain
}
</style>
