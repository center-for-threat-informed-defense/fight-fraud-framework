<template>
    <div ref="container">
        <InputGroup>
            <InputText name="search-bar" v-model="searchTerm" size="small" variant="outline" placeholder="Search"
                @keyup.enter="clickSearch" id="search-bar" @keyup="showActiveSearch ? performSearch() : null" />
            <InputGroupAddon>
                <PrimeButton severity="secondary" variant="icon" @click="clickSearch">
                    <i class="pi pi-search"></i>
                </PrimeButton>
            </InputGroupAddon>
        </InputGroup>
        <div v-if="showActiveSearch && searchResults.length > 0 && searchTerm && focused" class="search-results">
            <div v-for="result of searchResults" :key="result.id" class="w-96 bg-white">
                <h6><router-link :to="getResultURL(result)">{{ result.id }} {{ result.name }}</router-link></h6>
                <p>{{ truncatedDescription(result.description) }}</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import PrimeButton from "primevue/button"
import { truncatedDescription, performSearch } from "../utils/Search";
import json from "../data/matrix-data.json";
import { useFocusWithin } from '@vueuse/core'

export default defineComponent({
    components: { InputGroup, PrimeButton, InputGroupAddon, InputText },
    setup() {
        // logic to set focus for search bar and any items within there
        const container = ref(null);
        const { focused } = useFocusWithin(container)
        return {
            container,
            focused
        }
    },
    data() {
        return {
            searchTerm: "",
            searchResults: [],
            matrixData: json,
        };
    },
    props: {
        showActiveSearch: {
            type: Boolean,
            default: false
        }
    },
    watch: {
        "$route.params.query": {
            immediate: true,
            handler(q) {
                this.searchTerm = typeof q === "string" ? q : "";
            },
        },
    },
    methods: {
        truncatedDescription(string: string) {
            return truncatedDescription(string, 20);
        },
        getTacticData(id: string) {
            return this.matrixData.filter(i => i.id === id)[0]
        },
        clickSearch() {
            this.$router.push({
                name: "search",
                params: { query: this.searchTerm || "" },
            });
        },
        performSearch() {
            const results = performSearch(this.searchTerm);
            this.searchResults = results.slice(0, 3)
        },
        getResultURL(result) {
            if (result.tactic) {
                return '/tactic/' + result.id + '/'
            }
            return '/technique/' + result.id + '/'
        }

    },
});
</script>

<style scoped>
.p-inputgroup {
    @apply w-80
}

.p-inputgroup {
    @apply my-1
}

.navbar .p-inputtext-sm.p-inputfield-sm, .navbar .p-inputgroupaddon {
    @apply bg-ctid-navy text-ctid-light-gray
}

.navbar .p-button-secondary {
    @apply bg-ctid-navy text-ctid-light-gray border-none;
}

.navbar .p-inputgroupaddon button {
    @apply text-ctid-light-gray
}

.search-results {
    @apply absolute right-8 bg-white text-ctid-black px-6 py-4 shadow-lg rounded-lg
}

.search-results h6 {
    @apply mt-4 font-medium
}

.search-results p {
    @apply text-sm
}
</style>
