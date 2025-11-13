import { createRouter, createWebHashHistory } from "vue-router";
import { nextTick } from "vue";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import MatrixView from "@/views/MatrixView.vue";

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
    path: "/resources/matrix",
    name: "matrix",
    component: MatrixView,
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
      ? to.meta.title + " | Fight Financial Fraud"
      : "Fight Financial Fraud";
  });
});

export { router };
