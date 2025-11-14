<template>
    <breadcrumb :model="breadcrumbItems" :home="{ icon: 'pi pi-home', route: '/' }">
        <template #item="{ item, props }">
            <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                <a :href="href" v-bind="props.action" @click="navigate">
                    <span :class="[item.icon, 'text-color']" />
                    <span class="text-primary">{{ item.label }}</span>
                </a>
            </router-link>
            <a v-else :href="item.url" :target="item.target" v-bind="props.action">
                <span class="text-surface-700 dark:text-surface-0">{{ item.label }}</span>
            </a>
        </template>
    </breadcrumb>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Breadcrumb from 'primevue/breadcrumb';

export default defineComponent({
    components: { Breadcrumb },
    props: {
        breadcrumbItems: []
    },
});
</script>

<style scoped></style>
