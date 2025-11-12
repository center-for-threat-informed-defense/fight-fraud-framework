import { createApp } from "vue";
import { router } from "./router";
import App from "./App.vue";
import "./index.css";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/mdc-light-deeppurple/theme.css";
// import "bootstrap/dist/css/bootstrap.min.css"; // For Bootstrap styles
// import "bootstrap"; // For Bootstrap's JavaScript functionality (requires Popper.js and jQuery)

createApp(App).use(router).use(PrimeVue).mount("#app");
