<template>
  <main>
    <div class="hero">
      <div class="flex container">
        <div class="w-1/2 pr-20">
          <h1 class="font-medium text-4xl ">MITRE Fight Fraud Framework™</h1>
          <div class="flex flex-wrap gap-x-40">
            <div v-for="link in featuredLinks" :key="link.label" class=" w-32">
              <router-link :to="link.route" class="link-blue-external">{{
                link.label }}</router-link>
            </div>
          </div>
        </div>
        <div class="w-1/2">
          <p>The MITRE Fight Fraud Framework™ (F3 Framework) is a curated knowledge base of tactics, techniques, and
            procedures
            (TTPs) used by fraud actors. The F3 Framework includes behaviors that characterize known fraud TTPs and
            references existing <a href="https://attack.mitre.org/" target="blank">MITRE ATT&CK®</a> cyber techniques as
            applicable to
            financial fraud. The F3 Framework provides a living
            knowledge base of fraud actor TTPs based on real-world observations of fraud incidents as seen by banking
            institutions. </p>
          <router-link to="/about" class="link-blue-external">Learn More</router-link>
        </div>
      </div>
    </div>
  </main>
  <div class="matrix-container">
    <h1 class="text-center font-medium text-3xl mb-6">MITRE Fight Fraud Framework™ Matrix</h1>
    <matrix-container />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MatrixContainer from "../components/MatrixContainer.vue";

export default defineComponent({
  components: { MatrixContainer },
  data() {
    return {
      featuredLinks: [
        {
          label: "Resources", route: "/resources"
        },
        { label: "Contributors", route: "/" },
        { label: "Tactics", route: "/tactic" },

        {
          label: "Techniques", route: "/technique"
        }
      ],
    };
  },
})
</script>
<style scoped>
.hero {
  @apply py-20 m-0 bg-ctid-light-gray/30 absolute top-0 left-0 w-screen;
  min-height: 60vh;
}

.hero .container {
  width: 75vw;
  margin: auto;
  margin-bottom: 0;
  padding-top: 150px;
  padding-bottom: 40px;
}

.matrix-container {
  @apply mt-[70vh] sm:mt-[60vh] md:mt-[50vh];
  padding-top: 10px;
}

.matrix-container h1 {
  @apply mt-40 sm:mt-20 lg:mt-10 xl:mt-0;
}
</style>