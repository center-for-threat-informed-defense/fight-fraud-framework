<template>
  <div class="flex">
    <div class="main">
      <h1>Search</h1>
      <SiteSearch />
      <div v-for="result of visibleResults" :key="result.id" class="search-result">
        <h2>{{ result.id }} {{ result.name }}</h2>
        <p>{{ truncatedDescription(result.description) }}</p>
        <p v-if="result.tactics">Tactics: <template v-for="tactic of result.tactics" :key="tactic">
            <router-link :to="'/tactic/' + tactic">{{ getTacticData(tactic).name }}</router-link>
          </template>
        </p>
        <router-link :to="getResultURL(result)" class="link-blue-external small">View Page</router-link>
      </div>
      <Paginator v-model:first="first" :rows="rows" :totalRecords="filteredResults.length"
        :rowsPerPageOptions="[5, 10, 20, 30]" @page="onPageChange" />
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
import Paginator from 'primevue/paginator';
import { truncatedDescription, performSearch } from "../utils/Search";

export default defineComponent({
  components: { SiteSearch, MultiSelect, Paginator },
  data() {
    return {
      route: useRoute(),
      selectedTactics: [],
      matrixData: json,
      first: 0,
      rows: 5,
    }
  },
  watch: {
    // Reset pagination when the URL search query changes
    "route.params.query": {
      immediate: true,
      handler() {
        this.first = 0;
      },
    },
  },
  computed: {
    searchQuery() {
      console.log("query ", this.route.params.query)
      const raw = this.route.params.query;
      const s = typeof raw === "string" ? raw : "";
      return decodeURIComponent(s).trim();
    },
    tactics() {
      return this.matrixData.filter(i => i.tactic)
    },
    searchResults() {
      return performSearch(this.searchQuery)
    },
    filteredResults() {
      if (!this.selectedTactics || this.selectedTactics.length === 0) {
        return this.searchResults;
      }

      const selectedIds = new Set(this.selectedTactics.map((t) => t.id));

      return this.searchResults.filter((r) => {
        const tactics: string[] = Array.isArray(r.tactics) ? r.tactics : [];
        return tactics.some((tid) => selectedIds.has(tid));
      });
    },
    visibleResults() {
      return this.filteredResults.slice(this.first, this.rows + this.first);
    }
  },
  methods: {
    truncatedDescription(string: string) {
      return truncatedDescription(string);
    },
    getTacticData(id: string) {
      return this.matrixData.filter(i => i.id === id)[0]
    },
    onPageChange(event) {
      this.first = event.first;
      this.rows = event.rows;
    },
    getResultURL(result) {
      if (result.tactic) {
        return '/tactic/' + result.id + '/'
      }
      return '/technique/' + result.id + '/'
    }
  }
});
</script>

<style scoped>
.main {
  @apply w-full block
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

.search-result .link-blue-external {
  @apply mt-0
}
</style>
