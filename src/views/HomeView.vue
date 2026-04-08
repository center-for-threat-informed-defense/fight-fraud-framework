<template>
  <main>
    <section class="hero full-bleed">
      <div class="hero-inner">
        <div class="hero-grid">
          <div class="hero-left">
            <h1 class="font-medium text-4xl">Fight Fraud Framework</h1>

            <div class="grid grid-cols-2 gap-x-2 gap-y-2 mt-6 w-96">
              <div v-for="link in featuredLinks" :key="link.label" class="w-32">
                <router-link :to="link.route" class="link-blue-external">
                  {{ link.label }}
                </router-link>
              </div>
            </div>
          </div>

          <div class="hero-right">
            <p>The MITRE Fight Fraud Framework™ (F3) is a curated knowledge base of tactics and techniques used by financial fraud actors, derived from real-world observations of cyber fraud incidents. The
              framework includes behaviors that characterize known fraud TTPs and references existing <a
                href="https://attack.mitre.org/" target="blank">MITRE ATT&CK®</a> cyber techniques as applicable to
              financial fraud. F3 provides a common structure and taxonomy to consistently describe and enumerate
              the material events of a cyber fraud incident, enabling stronger collaboration on fraud prevention,
              detection, and response across organizational teams. The knowledge base is globally accessible, open, and
              available at no charge to any person or organization.
            </p>
            <router-link to="/about" class="link-blue-external">Learn More</router-link>
          </div>
        </div>
      </div>
    </section>

    <section class="matrix-container">
      <h1 class="text-center font-medium text-3xl mb-6 mt-8">
        Fight Fraud Framework Matrix
      </h1>
      <matrix-container />
    </section>
  </main>
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
        { label: "Contributors", route: "/about/contributors" },
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
.full-bleed {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

/* Pull background to the top of the viewport */
.hero {
  @apply bg-ctid-light-gray/30;
  margin-top: -7rem;
  padding-top: 7rem;
  padding-bottom: 3rem;
}

/* Now this can be "normal" spacing, not huge top padding */
.hero-inner {
  @apply mx-auto w-11/12 lg:w-3/4;
  @apply py-5 sm:py-6;
}

.hero-grid {
  @apply flex flex-col lg:flex-row;
  @apply gap-10 lg:gap-16;
  @apply items-start;
}

.hero-left,
.hero-right {
  @apply w-full lg:w-1/2;
}

.matrix-container {
  @apply pt-10;
}
</style>