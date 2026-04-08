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
      const q = this.searchQuery;
      if (!q) return [];

      // Normalize + tokenize query: "Account takeover" -> ["account","takeover"]
      const tokens = this.normalize(q).split(" ").filter(Boolean);

      const results = [];

      for (const i of this.matrixData) {
        const id = i.id ?? "";
        const name = i.name ?? "";
        const desc = i.description ?? "";

        // Normalized fields (case-insensitive, punctuation-insensitive)
        const idN = this.normalize(id);
        const nameN = this.normalize(name);
        const descN = this.normalize(desc);

        const allText = `${idN} ${nameN} ${descN}`;

        // Require ALL tokens to be present somewhere (AND search)
        const allTokensPresent = tokens.every(t => allText.includes(t));
        if (!allTokensPresent) continue;

        // Scoring: weight matches in id/name/description
        let score = 0;
        for (const t of tokens) {
          score += 5 * this.countOccurrences(idN, t);
          score += 3 * this.countOccurrences(nameN, t);
          score += 1 * this.countOccurrences(descN, t);
        }

        // Bonus if exact normalized phrase occurs (keeps phrase results on top)
        const phrase = this.normalize(q);
        if (allText.includes(phrase)) score += 10;

        if (score > 0) results.push({ ...i, searchScore: score });
      }

      return results.sort((a, b) => b.searchScore - a.searchScore);
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
    normalize(s: string) {
      // lowercase, remove diacritics, turn punctuation into spaces, collapse whitespace
      return s
        .toLowerCase()
        .normalize("NFKD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9]+/g, " ")
        .trim()
        .replace(/\s+/g, " ");
    },

    countOccurrences(haystack: string, needle: string) {
      if (!needle) return 0;
      let count = 0;
      let idx = 0;
      for (; ;) {
        idx = haystack.indexOf(needle, idx);
        if (idx === -1) break;
        count++;
        idx += needle.length;
      }
      return count;
    },
    truncatedDescription(text: string) {
      const words = text.split(' ');
      if (words.length > 50) {
        return words.slice(0, 50).join(' ') + '...';
      }
      return text;

    },
    getTacticData(id: string) {
      return this.matrixData.filter(i => i.id === id)[0]
    },
    onPageChange(event) {
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
