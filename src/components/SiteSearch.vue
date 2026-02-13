<template>
    <InputGroup>
        <InputText v-model="searchTerm" size="small" variant="outline" placeholder="Search" />
        <InputGroupAddon>
            <Button severity="secondary" variant="icon" @click="clickSearch">
                <i class="pi pi-search"></i>
            </Button>
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
import Button from "primevue/button"

export default defineComponent({
    components: { InputGroup, InputGroupAddon, InputText, Button },
    data() {
        return {
            router: useRouter(),
            route: useRoute(),

        };
    },
    methods: {
        clickSearch() {
            this.router.push({
                path: '/search',
                query: { q: this.searchTerm }
            });
        }
    },
    computed: {
        searchTerm() {
            return this.route.query.q;
        }
    }
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
