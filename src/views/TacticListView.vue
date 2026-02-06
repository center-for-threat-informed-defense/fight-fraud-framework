<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1>Tactics</h1>
        <p>Tactics represent the "why" of an ATT&CK technique or sub-technique. It is the adversary's tactical goal: the
            reason for performing an action. For example, an adversary may want to achieve credential access.</p>

        <DataTable v-model:filters="filters" :value="tactics" dataKey="id" :globalFilterFields="['id', 'name']">
            <template #header>
                <div class="flex justify-end">
                    <InputGroup>
                        <InputText size="small" variant="outline" v-model="filters['global'].value"
                            placeholder="Search" />
                        <InputGroupAddon>
                            <Button severity="secondary" variant="icon">
                                <i class="pi pi-search"></i>
                            </Button>
                        </InputGroupAddon>
                    </InputGroup>
                </div>
            </template>
            <Column header="ID" field="id" filterField="technique.id"></Column>
            <Column header="Name" field="name" filterField="technique.name"></Column>
            <Column header="Link">
                <template #body="{ data }">
                    <router-link :to="'/tactic/' + data.id">See More <i class="pi pi-arrow-right ml-1"
                            style="font-size: .75rem"></i>
                    </router-link>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import json from "../data/matrix-data.json";
import DataTable from "primevue/datatable";
import Column from 'primevue/column';
import { FilterMatchMode } from '@primevue/core/api';
import InputText from 'primevue/inputtext';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';

export default defineComponent({
    components: { BreadcrumbComponent, DataTable, Column, InputGroup, InputGroupAddon, InputText },
    data() {
        return {
            matrixData: json,
            breadcrumbItems: [
                { label: "Tactics", route: "/tactic" },
            ],
            filters: {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
            }
        }
    },
    computed: {
        tactics() {
            return this.matrixData.filter(i => i.tactic)
        },
    }
});
</script>

<style scoped>
.p-inputgroup {
    max-width: 200px;
}

a {
    @apply text-ctid-blue hover:text-ctid-navy hover:underline
}
</style>
