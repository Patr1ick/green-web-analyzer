import { createStore, Store } from "vuex";

import { ResultsModel } from "../models/result";

export interface State {
    requestResult: ResultsModel | null;
    isLoading: boolean;
}

declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
      $store: Store<State>
    }
  }

const store = createStore<State>({
    state: {
        requestResult: null,
        isLoading: false
    },
    mutations: {
        setRequestResult(state, payload: ResultsModel){
            state.requestResult = payload;
        },
        invertIsLoading(state){
            state.isLoading = !state.isLoading;
        }
    },
    getters:{
        isResultNull(state){
            return state.requestResult === null;
        },
        // isResponseNull: (state) => (id: number) => {
        //     if (state == null){
        //         return
        //     }else {
        //         return state.requestResult.criteria[0].details.requests[id].response == null;
        //     }
        // }
    }
});

export default store;