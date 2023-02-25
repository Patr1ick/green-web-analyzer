export interface MetricsModel {
    size: number;
    requests: number;
    potential_savings: number;
}

export interface CriteriaModel {
    id: number;
    accepted: boolean;
    details: any;
}

export interface ResultsModel {
    url: string;
    date: Date;
    metrics: MetricsModel;
    criteria: Array<CriteriaModel>;
}

export interface RequestModel {
    date: Date;
    method: string;
    path: string;
    response: ResponseModel;
    size: number;
    url: string;
}
interface ResponseModel {
    status_code: number;
    type: string;
}
