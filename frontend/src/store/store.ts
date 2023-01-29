import { createStore, Store } from "vuex";

import { ResultsModel } from "../models/result";

export interface State {
    requestResult: ResultsModel | null;
    isLoading: boolean;
    showDisclaimer: boolean;
}

declare module "@vue/runtime-core" {
    interface ComponentCustomProperties {
        $store: Store<State>;
    }
}

const store = createStore<State>({
    state: {
        requestResult: null,
        isLoading: false,
        showDisclaimer: true,
    },
    mutations: {
        setRequestResult(state, payload: ResultsModel) {
            state.requestResult = payload;
        },
        invertIsLoading(state) {
            state.isLoading = !state.isLoading;
        },
        setShowDisclaimer(state, payload: boolean) {
            state.showDisclaimer = payload;
        },
    },
    getters: {
        isResultNull(state) {
            return state.requestResult === null;
        },
    },
});

export default store;
