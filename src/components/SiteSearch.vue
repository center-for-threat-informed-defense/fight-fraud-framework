<template>
    <InputGroup>
        <InputText v-model="searchTerm" size="small" variant="outline" placeholder="Search" @submit="clickSearch" />
        <InputGroupAddon>
            <PrimeButton severity="secondary" variant="icon" @click="clickSearch">
                <i class="pi pi-search"></i>
            </PrimeButton>
        </InputGroupAddon>
    </InputGroup>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';
import { useRoute } from 'vue-router';
import PrimeButton from "primevue/button"

export default defineComponent({
    components: { InputGroup, PrimeButton, InputGroupAddon, InputText },
    data() {
        return {
            router: useRouter(),
            route: useRoute(),
            searchTerm: this.$route.params.query || ''

        };
    },
    methods: {
        clickSearch() {
            this.router.push({
                name: 'search',
                params: { query: this.searchTerm }
            });
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
</style>
