import { createRouter, createWebHashHistory } from "vue-router";
import { nextTick } from "vue";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import MatrixView from "@/views/MatrixView.vue";
import TechniqueView from "@/views/TechniqueView.vue";
import TechniqueListView from "@/views/TechniqueListView.vue";
import TacticListView from "@/views/TacticListView.vue";
import SearchView from "@/views/SearchView.vue";
import ResourceView from "@/views/ResourceView.vue";
// import SuggestTechniqueView from "@/views/SuggestTechniqueView.vue";
// import UpdateTechniqueView from "@/views/UpdateTechniqueView.vue";
import ContactUsView from "@/views/ContactUsView.vue";
import DesignPrinciplesView from "@/views/DesignPrinciplesView.vue";
import ContributorView from "@/views/ContributorView.vue";
import VersionHistoryView from "@/views/VersionHistoryView.vue";

const routes = [
  {
    path: "/",
    name: "",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/about/contributors",
    name: "contributors",
    component: ContributorView,
  },
  {
    path: "/about/methodology",
    name: "methodology",
    component: DesignPrinciplesView,
  },
  {
    path: "/about/contact-us",
    name: "contact",
    component: ContactUsView,
  },
  // {
  //   path: "/contact-us/new-technique",
  //   name: "suggest-technique",
  //   component: SuggestTechniqueView,
  // },
  // {
  //   path: "/contact-us/update-technique/:id?",
  //   name: "update-technique",
  //   component: UpdateTechniqueView,
  // },
  {
    path: "/resources",
    name: "resources",
    component: ResourceView,
  },
  {
    path: "/resources/versions",
    name: "versions",
    component: VersionHistoryView,
  },
  {
    path: "/matrix",
    name: "matrix",
    component: MatrixView,
  },
  {
    path: "/tactic",
    name: "tactics",
    component: TacticListView,
  },
  {
    path: "/technique",
    name: "techniques",
    component: TechniqueListView,
  },
  {
    path: "/technique/:id",
    name: "technique",
    component: TechniqueView,
  },
  {
    path: "/tactic/:id",
    name: "tactic",
    component: TechniqueView,
  },
  {
    path: "/search/:query?",
    name: "search",
    component: SearchView,
  },
];

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: routes,
  scrollBehavior() {
    // always scroll to top when linking to a new page
    return { top: 0 };
  },
});

router.afterEach((to) => {
  nextTick(() => {
    document.title = to.meta.title
      ? to.meta.title + " | MITRE Fight Fraud Framework™"
      : "MITRE Fight Fraud Framework™";
  });
});

export { router };
