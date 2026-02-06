<template>
  <main>
    <div class="hero">
      <div class="flex container">
        <div class="w-1/2 pr-20">
          <h1 class="font-medium text-4xl ">Fight Financial Fraud</h1>
          <div class="flex flex-wrap gap-x-40">
            <div v-for="link in featuredLinks" :key="link.label" class=" w-32">
              <router-link :to="link.route" class="link-blue-external">{{
                link.label }}</router-link>
            </div>
          </div>
        </div>
        <div class="w-1/2">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
            dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
            ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
            anim id est laborum.</p>
          <router-link to="/about" class="link-blue-external">Learn More</router-link>
        </div>
      </div>
    </div>
  </main>
  <div class="matrix-container">
    <h1 class="text-center text-3xl">Fight Financial Fraud Matrix</h1>
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
        { label: "Tactics", route: "/tactics" },

        {
          label: "Techniques", route: "/techniques"
        }
      ],
    };
  },
})
</script>
<style scoped>
.hero {
  @apply py-20 m-0 bg-ctid-light-gray/30 absolute top-0 left-0 w-screen;
  height: 50vh;

}

.hero .container {
  width: 75vw;
  margin: auto;
  margin-bottom: 0;
  padding-top: 100px;
  padding-bottom: 40px;
}

.matrix-container {
  margin-top: 40vh;
  padding-top: 10px;
}
</style>