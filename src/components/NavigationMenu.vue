<template>
  <nav class="navbar">
    <div class="flex justify-between mx-8">
      <router-link to="/" class="my-auto w-max">
        <h1>MITRE Fight Fraud Framework™</h1>
      </router-link>
      <div class="lg:flex hidden w-max gap-10">
        <TabMenu class="w-max" :model="items" :active-index="getActiveIndex()">
          <template #item="{ item, props }">
            <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
              <a :to="href" v-bind="props.action" @click="navigate">
                <span v-bind="props.label">{{ item.label }}</span>
              </a>
            </router-link>
          </template>
        </TabMenu>
        <SiteSearch />
      </div>
      <div class=" lg:hidden inline-block w-max my-auto">
        <MenuBar :model="[...items, { label: 'Search', route: '/search' }]" id="overlay_menu" ref="menu"
          class=" text-white z-50  p-menubar-mobile">
          <template #item="{ item, props }">
            <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
              <a :to="href" v-bind="props.action" @click="navigate">
                <span v-bind="props.label">{{ item.label }}</span>
              </a>
            </router-link>
          </template>
        </MenuBar>
        <Menu ref="menu" :model="items" popup class="!min-w-fit" />
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import TabMenu from "primevue/tabmenu";
import MenuBar from "primevue/menubar";
import { useRouter } from 'vue-router';
import SiteSearch from "./SiteSearch.vue"

export default defineComponent({
  components: { TabMenu, MenuBar, SiteSearch },
  data() {
    return {
      router: useRouter(),
      items: [
        { label: "Home", route: "/" },
        { label: "About", route: "/about" },
        {
          label: "Resources", route: "/resources"
        },
        {
          label: "Matrix", route: "/matrix"
        }
      ],
      searchTerm: null,
    };
  },
  methods: {
    getActiveIndex() {
      const route = this.$route.path;
      return this.items.findIndex(function (item) {
        return item.route.split("/")[1] === route.split("/")[1];
      });
    },
  },
});
</script>

<style scoped>
/* Navigation */
.navbar {
  @apply fixed bg-ctid-navy text-white pt-1 w-full top-0 z-50
}

.navbar h1 {
  @apply my-auto font-medium text-xl uppercase w-max
}

.p-inputgroup {
  @apply w-80
}

.p-inputgroup {
  @apply my-1
}

.p-inputtext-sm.p-inputfield-sm, .p-inputgroupaddon {
  @apply bg-ctid-navy text-ctid-light-gray
}

.p-inputgroupaddon button {
  @apply text-ctid-light-gray
}

.p-menubar.p-menubar-mobile {
  @apply bg-ctid-navy border-none
}

.p-menubar.p-menubar-mobile .p-menubar-button {
  @apply text-white fill-white
}
</style>
