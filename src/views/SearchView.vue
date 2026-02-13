<template>
  <div class="flex">
    <div class="main">
      <h1>Search</h1>
      <SiteSearch />
      <div v-for="result of filteredResults" :key="result.id" class="search-result">
        <h2>{{ result.id }} {{ result.name }}</h2>
        <p>{{ truncatedDescription(result.description) }}</p>
        <p v-if="resultTactics(result)">
          Tactics: <template v-for="tactic of resultTactics(result)" :key="tactic.id">
            <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
          </template>
        </p>
      </div>
    </div>
    <div class="search-sidebar">
      <h2>Filter By:</h2>
      <h3>Tactic</h3>
      <MultiSelect v-model="selectedTactics" :options="tactics" optionLabel="name" filter placeholder="All Tactics"
        :maxSelectedLabels="3" class="w-full md:w-80" />
    </div>
  </div>

</template>
<script lang="ts">
import { defineComponent } from "vue";
import { useRoute } from 'vue-router';
import SiteSearch from "../components/SiteSearch.vue";
import MultiSelect from 'primevue/multiselect';
import json from "../data/matrix-data.json";

export default defineComponent({
  components: { SiteSearch, MultiSelect },
  data() {
    return {
      route: useRoute(),
      selectedTactics: [],
      matrixData: json
    }
  },
  computed: {
    searchQuery() {
      return this.route.query.q;
    },
    tactics() {
      return this.matrixData.filter(i => i.tactic)
    },
    searchResults() {
      // todo: write search algorithm
      return [this.matrixData[8], this.matrixData[6]]
    },
    filteredResults() {

      // if (this.selectedTactics.length > 0) {
      //   return this.searchResults.filter()
      // }
      return this.searchResults;
    }
  },
  methods: {
    truncatedDescription(text: string) {
      const words = text.split(' ');
      if (words.length > 50) {
        return words.slice(0, 50).join(' ') + '...';
      }
      return text;

    },
    resultTactics(result) {
      if (result?.tactic) {
        return null;
      }
      return [this.matrixData[0]]
    }
  }
});
</script>

<style>
.main {
  @apply w-full
}

.search-sidebar {
  @apply border-l-2 border-ctid-light-gray h-screen ml-6 pl-6 w-1/4;
}

.search-result p {
  @apply text-sm
}

.search-result h2 {
  @apply mt-10
}

a, p a {
  @apply text-ctid-blue hover:text-ctid-navy hover:underline
}
</style>
