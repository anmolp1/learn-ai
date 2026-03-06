# Data Engineering Capstone Guidelines

## Overview

Build a complete, AI-assisted data pipeline that ingests, transforms, deploys, and monitors real data. This is not a tutorial project — it should solve a problem you care about.

## Requirements

1. **Data source:** Real or realistic (public API, open dataset, or your own data)
2. **Pipeline stages:** Ingestion → Transformation (3+ steps) → Loading → Monitoring
3. **Infrastructure:** Deployed to GCP via Terraform (free tier resources)
4. **Testing:** Unit tests + at least one integration test
5. **Monitoring:** Automated quality checks with alerting
6. **Documentation:** Complete README + inline documentation
7. **Repository:** Public GitHub repo

## Timeline

| Session | Milestone |
|---------|-----------|
| 0 | Choose data source, set up repo |
| 1 | Define pipeline scope, write initial prompts |
| 2 | Build ingestion + transformation layers |
| 3 | Deploy infrastructure with Terraform |
| 4 | Add monitoring and AI-powered alerting |
| 5 | Production readiness audit + fixes |
| 6 | Present |

## Example Projects

| Project | Data Source | Pipeline |
|---------|-----------|----------|
| Weather Analytics | OpenWeather API | Ingest hourly → aggregate daily/weekly → detect anomalies → alert on extremes |
| GitHub Activity Monitor | GitHub API | Ingest repo events → classify by type → trend analysis → weekly summary report |
| E-commerce Analytics | Kaggle dataset or Faker-generated | Ingest transactions → customer segmentation → revenue metrics → data quality monitoring |
| Public Transit Tracker | GTFS feeds | Ingest schedules + real-time → delay calculation → route performance → anomaly detection |
| Financial Data Pipeline | Alpha Vantage / Yahoo Finance API | Ingest stock data → technical indicators → cross-asset correlation → drift detection |

## Repo Structure

```
my-capstone/
├── README.md                 # What, why, setup, run, test, monitor
├── src/
│   ├── ingestion/           # Data extraction scripts
│   ├── transformation/      # Transform logic (Python/dbt)
│   └── monitoring/          # Quality checks, alerting
├── infrastructure/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
├── tests/
│   ├── unit/
│   └── integration/
├── .github/
│   └── workflows/
│       └── test.yml         # CI: run tests on push
├── docs/
│   ├── architecture.md      # Pipeline architecture diagram/description
│   └── monitoring.md        # What's monitored, alert thresholds
└── .gitignore
```

## Evaluation Rubric

| Criteria | Weight | Great |
|----------|--------|-------|
| Problem definition | 10% | Real problem, clear scope, well-articulated |
| Pipeline completeness | 25% | All stages work: ingest → transform → load → monitor |
| AI integration | 20% | AI used thoughtfully throughout — not just for boilerplate |
| Infrastructure | 15% | Terraform deploys cleanly, follows security best practices |
| Testing + quality | 15% | Tests exist, pass, and cover meaningful cases |
| Documentation | 15% | Someone else could clone, deploy, and operate this pipeline |
