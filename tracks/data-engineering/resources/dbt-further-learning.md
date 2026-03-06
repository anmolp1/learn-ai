# dbt - Further Learning

## What is dbt?

dbt (data build tool) is an open-source tool that lets data engineers and analysts write data transformations as SQL SELECT statements. dbt handles turning those SELECT statements into tables and views in your data warehouse, managing dependencies between models, running tests, and generating documentation.

In short: dbt is the "T" in ELT. You write SQL, and dbt manages the execution, ordering, and testing of those transformations.

## Why dbt is Not in the Core Curriculum

This program teaches data transformation using Python (pandas, BigQuery SQL). The concepts you learn — cleaning data, joining tables, aggregating, handling nulls, building reusable transformation logic — are the same concepts dbt applies, just expressed differently.

We chose Python-first for two reasons:

1. **Broader applicability.** Python transformation skills transfer to streaming pipelines, ML feature engineering, API integrations, and other contexts where dbt does not operate.
2. **Fewer moving parts.** Adding dbt introduces its own project structure, configuration, CLI, and Jinja templating on top of SQL. That is additional setup complexity that distracts from the core learning goals.

That said, dbt is widely used in production data teams, especially in analytics engineering roles. If you are working with a modern data stack (warehouse-centric, ELT pattern), learning dbt is a strong investment.

## Self-Study Resources

### Official Documentation

- **dbt Docs:** [docs.getdbt.com](https://docs.getdbt.com/)
  The complete reference. Start with the "What is dbt?" and "Quickstart" sections.

### Free Course

- **dbt Fundamentals:** [courses.getdbt.com/courses/fundamentals](https://courses.getdbt.com/courses/fundamentals)
  Free, self-paced course from dbt Labs. Covers models, tests, documentation, and sources. Takes approximately 5 hours.

### BigQuery-Specific Setup

- **dbt-bigquery Setup Guide:** [docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup)
  Step-by-step instructions for connecting dbt to BigQuery, including authentication with service accounts and OAuth.

### Supplementary Reading

- **dbt Best Practices:** [docs.getdbt.com/best-practices](https://docs.getdbt.com/best-practices)
  How production teams structure their dbt projects — useful once you have the basics down.

- **The Analytics Engineering Guide:** [getdbt.com/analytics-engineering/start-here](https://www.getdbt.com/analytics-engineering/start-here)
  Context on the role dbt plays in modern data teams and how analytics engineering differs from traditional data engineering.
