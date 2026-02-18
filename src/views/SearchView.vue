<template>
  <div class="flex">
    <div class="main">
      <h1>Search</h1>
      <SiteSearch />
      <div v-for="result of visibleResults" :key="result.id" class="search-result">
        <h2>{{ result.id }} {{ result.name }}</h2>
        <p>{{ truncatedDescription(result.description) }}</p>
        <p v-if="resultTactics(result)">
          Tactics: <template v-for="tactic of resultTactics(result)" :key="tactic.id">
            <router-link :to="'/tactic/' + tactic.id">{{ tactic.name }}</router-link>
          </template>
        </p>
        <router-link :to="'/technique/' + result.id" class="link-blue-external small">View Page</router-link>
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
  computed: {
    searchQuery() {
      return this.route.query.q;
    },
    tactics() {
      return this.matrixData.filter(i => i.tactic)
    },
    searchResults() {
      // Prioritize techniques over tactics
      // Look for matches in ID, name, description
      const matches = [];
      this.matrixData.forEach((i) => {
        let matchScore = 0;
        const regex = new RegExp(this.searchQuery, "gi");

        if (i.id.match(regex)) {
          matchScore += 5;
        }

        if (i.name.match(regex)) {
          const count = i.description.match(regex);
          matchScore += 3 * count?.length;
        }
        if (i.description.match(regex)) {
          const count = i.description.match(regex);
          matchScore += count.length;
        }

        if (matchScore > 0) {
          matches.push({
            ...i,
            searchScore: matchScore
          })
        }
      })
      return matches.sort((a, b) => b.searchScore - a.searchScore);

    },
    filteredResults() {

      // if (this.selectedTactics.length > 0) {
      //   return this.searchResults.filter()
      // }
      return this.searchResults;
    },
    visibleResults() {
      return this.filteredResults.slice(this.first, this.rows + this.first);
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
    }, onPageChange(event) {
      this.first = event.first;
      this.rows = event.rows;
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
