<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1>Tactics</h1>
        <p>Tactics represent the “why” of an F3 technique or sub-technique: the fraud actor's tactical goal and the
            reason for performing an action. Tactics are not the same as phases of a fraud incident and not every tactic
            will be present in every fraud incident.
        </p>
        <p>F3 tactics are of the format FA#### and are unique within the knowledgebase; or, if a tactic already exists
            in the ATT&CK knowledgebase, the ATT&CK identifier is used (i.e., TA####).</p>
        <DataTable v-model:filters="filters" :value="tactics" dataKey="id"
            :globalFilterFields="['id', 'name', 'description']">
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
            <Column header="ID" filterField="technique.id">
                <template #body="{ data }">
                    <router-link :to="'/tactic/' + data.id">{{ data.id }}
                    </router-link>
                </template>
            </Column>
            <Column header="Name" filterField="technique.name">
                <template #body="{ data }">
                    <router-link :to="'/tactic/' + data.id">{{ data.name }}
                    </router-link>
                </template>
            </Column>
            <Column header="Description" filterField="technique.description" headerClass="description-col"
                bodyClass="description-col">
                <template #body="{ data }">
                    {{ getShortDescription(data) }}
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
                { label: "Resources", route: "/resources" },
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
    },
    methods: {
        getShortDescription(tactic) {
            const lines: string[] = tactic.description.split(/\r\n|\r|\n/);
            return lines[0]
        }
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

:deep(.description-col) {
    @apply w-2/3 xl:w-3/4 hidden md:table-cell
}
</style>
