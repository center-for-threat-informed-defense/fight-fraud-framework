<template>
    <breadcrumb-component :breadcrumbItems="breadcrumbItems" />
    <div>
        <h1>Techniques</h1>
        <p>Techniques represent “how” a fraud actor achieves a tactical goal by performing an action. There may be
            multiple ways to perform a technique, resulting in distinct sub-techniques that describe more specific
            methods of how behavior is used to achieve an objective. Not all techniques have sub-techniques.</p>
        <p>F3 technique and sub-technique identifiers are of the format F#### for techniques and F####.#### for
            sub-techniques and are unique within the knowledgebase; or, if a technique or sub-technique already exists
            in the ATT&CK knowledgebase, the ATT&CK identifier is used (i.e., T####, T####.###).</p>

        <DataTable v-model:filters="filters" :value="techniques" dataKey="id"
            :globalFilterFields="['id', 'name', 'description']" class="w-full">
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
                    <router-link :to="'/technique/' + data.id">{{ data.id }}
                    </router-link>
                </template>
            </Column>
            <Column header="Name" filterField="technique.name">
                <template #body="{ data }">
                    <router-link :to="'/technique/' + data.id">{{ data.name }}
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
                { label: "Techniques", route: "/techniques" },
            ],
            filters: {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
            }
        }
    },
    computed: {
        techniques() {
            return this.matrixData.filter(i => !i.tactic)
        },
    },
    methods: {
        getShortDescription(technique) {
            const words = technique.description.split(' ');
            if (words.length > 50) {
                return words.slice(0, 50).join(' ') + '...';
            }
            return technique.description;
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

/* Make the internal table fixed-width and allow wrapping */
:deep(.p-datatable-table) {
    table-layout: fixed;
    width: 100%;
}

/* Allow cell content to wrap instead of forcing a long single line */
:deep(.p-datatable-tbody > tr > td) {
    white-space: normal;
    word-break: break-word;
}

:deep(.description-col) {
    @apply w-2/3 xl:w-3/4 hidden md:table-cell
}
</style>
