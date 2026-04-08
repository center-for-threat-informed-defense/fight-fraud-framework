<template>
  <navigation-menu />
  <div class="d-flex">
    <div id="page-body">
      <router-view></router-view>
    </div>
  </div>
  <navigation-footer />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import 'primeicons/primeicons.css'
import NavigationMenu from "./components/NavigationMenu.vue";
import NavigationFooter from "./components/NavigationFooter.vue";

export default defineComponent({
  components: {
    NavigationMenu, NavigationFooter
  },
});
</script>

<style>
#page-body {
  @apply mt-20 mb-10
}
</style>
