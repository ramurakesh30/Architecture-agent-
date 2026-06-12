export interface BenchmarkFramework {

  name: string;

  score: number;

  passed_controls: number;

  total_controls: number;

  failed_controls: string[];
}

export interface BenchmarkResult {

  overall_score: number;

  frameworks: BenchmarkFramework[];

  failed_controls: string[];
}

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
}

export interface ComplianceFramework {

  name: string;

  score: number;

  passed_controls: number;

  total_controls: number;

  failed_controls: string[];
}

export interface ComplianceResult {

  frameworks: ComplianceFramework[];
}

export interface Recommendation {

  category: string;

  message: string;
}

export interface RecommendationResult {

    security: string;

    reliability: string;

    scalability: string;
  
}

export interface Report {

  category_scores: CategoryScores;

  findings: Finding[];

  compliance_result?: ComplianceResult;

  benchmark_result?: BenchmarkResult;

  architecture_documentation?: any;

  recommendation_result?: RecommendationResult;

  recommendations?: Recommendation[];
}