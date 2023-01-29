export interface MetricsModel {
    size: number;
    requests: number;
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
    criteria: Array<CriteriaModel>
}