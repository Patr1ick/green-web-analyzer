import { createApp } from "vue";
import App from "./App.vue";

import router from "./router/router.js";
import store from "./store/store.js";

import BasicButton from "./components/UI/BasicButton.vue";
import BasicCard from "./components/UI/BasicCard.vue";
import BasicAccordion from "./components/UI/BasicAccordion.vue";
import BasicHint from "./components/UI/BasicHint.vue";

const app = createApp(App);

app.use(router);
app.use(store);

app.component("BasicButton", BasicButton)
    .component("BasicCard", BasicCard)
    .component("BasicAccordion", BasicAccordion)
    .component("BasicHint", BasicHint);

app.mount("#app");
