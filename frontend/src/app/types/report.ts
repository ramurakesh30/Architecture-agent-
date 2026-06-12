export interface CategoryScores {
  security: number;
  availability: number;
  reliability: number;
  scalability: number;
  cost: number;
  observability: number;
}

export interface Finding {

  message: string;

  severity?: string;
}

export interface Report {

  category_scores: CategoryScores;

  findings: Finding[];
}