import { createApp } from "vue";
import { router } from "./router";
import App from "./App.vue";
import Aura from "@primevue/themes/aura";
import "./index.css";
import PrimeVue from "primevue/config";
import { semantic } from "@primeuix/themes/aura/base";

createApp(App)
  .use(router)
  .use(PrimeVue, {
    theme: {
      preset: {
        ...Aura,
        semantic: {
          ...semantic,
          primary: {
            500: "#005B94",
          },
        },
      },
      options: {
        darkModeSelector: "none",
      },
    },
  })
  .mount("#app");
