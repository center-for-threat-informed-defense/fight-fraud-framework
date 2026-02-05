import { createApp } from "vue";
import { router } from "./router";
import App from "./App.vue";
import Aura from "@primevue/themes/aura"; // Import the Material preset
import "./index.css";
import PrimeVue from "primevue/config";

createApp(App)
  .use(router)
  .use(PrimeVue, {
    theme: {
      preset: Aura,
    },
  })
  .mount("#app");
