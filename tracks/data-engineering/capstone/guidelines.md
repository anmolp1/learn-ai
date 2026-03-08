# Data Engineering Capstone Guidelines

## Overview

Build a complete, AI-assisted data pipeline that ingests, transforms, deploys, and monitors real data. Choose one of the four capstone projects below — each has been vetted for scope, data source reliability, and alignment with the program's learning objectives.

> **These are the supported capstone options.** Each project uses a free, stable data source and fits within GCP free tier. Pick the one whose problem domain interests you most — all four are designed to exercise the full rubric equally.

## Requirements

1. **Data source:** One of the four approved projects below (free, public data sources)
2. **Pipeline stages:** Ingestion → Transformation (3+ steps) → Loading → Monitoring
3. **Infrastructure:** Deployed to GCP via Terraform (free tier resources)
4. **Testing:** Unit tests + at least one integration test
5. **Monitoring:** Automated quality checks with alerting
6. **Documentation:** Complete README + inline documentation
7. **Repository:** Public GitHub repo

## Timeline

| Session | Milestone |
|---------|-----------|
| 0 | Choose project, set up repo, verify data source access |
| 1 | Define pipeline scope, map transformations, draft prompts for pipeline components |
| 2 | Build ingestion + transformation steps with tests |
| 3 | Deploy BigQuery + Cloud Storage + IAM via Terraform |
| 4 | Add monitoring agent with AI-powered quality checks |
| 5 | Production readiness audit + fixes |
| 6 | Present |

## Capstone Projects

### 1. Earthquake Monitor

Build a pipeline that ingests real-time earthquake data, enriches it with geographic and impact analysis, and monitors for significant seismic events.

**Data source:** [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/) — free, no API key required, real-time GeoJSON feeds updated every minute.

**Pipeline stages:**

| Stage | Details |
|-------|---------|
| Ingest | Poll USGS real-time GeoJSON feed (all earthquakes, past hour/day) on a schedule |
| Transform 1 | Parse nested GeoJSON, flatten to tabular format, normalize magnitude scales |
| Transform 2 | Enrich with geographic context — reverse-geocode to country/region, calculate distance to nearest major city |
| Transform 3 | Classify impact severity (micro/minor/moderate/major/great) using magnitude + depth + population proximity |
| Load | Write to BigQuery with partitioning by date and clustering by region |
| Monitor | Alert on events above configurable magnitude threshold; detect unusual frequency patterns |

**AI integration points:**
- Schema inference from nested GeoJSON response
- Generate geographic enrichment logic (haversine distance, region classification)
- Anomaly detection prompt: "Given this week's earthquake frequency by region, identify unusual patterns"
- AI-generated test cases for edge cases (e.g., events at the antimeridian, magnitude 0 events)
- Monitoring rule design: prompt AI to suggest alert thresholds based on historical baselines

**Session milestones:**

| Session | Milestone |
|---------|-----------|
| 0 | Set up repo, verify USGS API access, explore GeoJSON feed structure |
| 1 | Define schema, map transformation steps, draft prompts for pipeline components |
| 2 | Build ingestion (scheduled poll) + transformation steps with tests |
| 3 | Deploy BigQuery + Cloud Storage + IAM via Terraform |
| 4 | Add monitoring agent: magnitude alerts, frequency anomaly detection, data freshness checks |
| 5 | Security audit, error handling, CI/CD, complete documentation |
| 6 | Present |

---

### 2. NYC 311 Complaint Analyzer

Build a pipeline that ingests NYC 311 service request data, classifies and aggregates complaints by type and geography, and monitors for emerging neighborhood issues.

**Data source:** [NYC Open Data — 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) — free, 30M+ rows, SODA API with free app token.

**Pipeline stages:**

| Stage | Details |
|-------|---------|
| Ingest | Query SODA API for recent complaints using date filters and pagination |
| Transform 1 | Clean and standardize complaint types (normalize 200+ categories into ~15 top-level groups) |
| Transform 2 | Enrich with geographic aggregation — roll up to neighborhood/community board level, compute complaint density |
| Transform 3 | Calculate resolution metrics — time-to-close by category, agency response rates, open vs. closed ratios |
| Load | Write to BigQuery with partitioning by created date and clustering by complaint group |
| Monitor | Alert on complaint volume spikes in any category; track data completeness (null rates for key fields) |

**AI integration points:**
- Schema design: prompt AI to propose a normalized schema from the raw 40+ field SODA response
- AI-assisted complaint category mapping (group 200+ raw types into meaningful categories)
- Anomaly detection: "Given complaint volumes by borough this week vs. last month, flag anomalies"
- AI-generated data quality rules (expected null rates, valid value ranges per field)
- Test generation: create unit tests for edge cases in category mapping (new complaint types, null descriptors, malformed dates)

**Session milestones:**

| Session | Milestone |
|---------|-----------|
| 0 | Set up repo, register for NYC Open Data app token, explore dataset schema |
| 1 | Define complaint taxonomy, map transformations, draft prompts for pipeline components |
| 2 | Build ingestion (paginated API calls) + transformation steps with tests |
| 3 | Deploy BigQuery + Cloud Storage + IAM via Terraform |
| 4 | Add monitoring agent: volume spike detection, data completeness checks, resolution time alerts |
| 5 | Security audit, error handling, CI/CD, complete documentation |
| 6 | Present |

---

### 3. GitHub Activity Tracker

Build a pipeline that ingests event activity from popular GitHub repositories, classifies and trends contributor behavior, and monitors for unusual activity patterns.

**Data source:** [GitHub Events API](https://docs.github.com/en/rest/activity/events) — free, 5,000 requests/hour with personal access token.

**Pipeline stages:**

| Stage | Details |
|-------|---------|
| Ingest | Poll events for a curated list of repositories (5–10 popular open-source repos) on a schedule |
| Transform 1 | Parse event payloads, extract actor, event type, timestamp, and repo metadata |
| Transform 2 | Classify events into activity categories (code, review, discussion, maintenance) and compute contributor engagement scores |
| Transform 3 | Aggregate into time-series metrics — daily active contributors, event velocity, PR merge rates |
| Load | Write to BigQuery with partitioning by event date and clustering by repository |
| Monitor | Alert on unusual activity drops (stale repos), contribution spikes, or bot-like behavior patterns |

**AI integration points:**
- Schema inference from nested event payloads (different event types have different structures)
- AI-assisted event classification logic (map 30+ GitHub event types to meaningful categories)
- Trend analysis prompt: "Given this repo's weekly commit velocity, is the current week normal?"
- AI-generated test data covering all event types
- Monitoring rule design: prompt AI to define "healthy" vs. "concerning" activity patterns for open-source repos

**Session milestones:**

| Session | Milestone |
|---------|-----------|
| 0 | Set up repo, create GitHub personal access token, select target repositories |
| 1 | Map event types to categories, define metrics, draft prompts for pipeline components |
| 2 | Build ingestion (multi-repo polling) + transformation steps with tests |
| 3 | Deploy BigQuery + Cloud Storage + IAM via Terraform |
| 4 | Add monitoring agent: activity anomaly detection, bot detection, data freshness checks |
| 5 | Security audit, error handling, CI/CD, complete documentation |
| 6 | Present |

---

### 4. Weather Analytics

Build a pipeline that ingests weather forecast and historical data, computes aggregated climate metrics, and monitors for extreme weather patterns and forecast accuracy.

**Data source:** [Open-Meteo API](https://open-meteo.com/) — free for non-commercial use, no API key required, 60+ weather variables, historical data included.

**Pipeline stages:**

| Stage | Details |
|-------|---------|
| Ingest | Fetch hourly forecast + historical actuals for a set of cities (10–15 locations) on a daily schedule |
| Transform 1 | Aggregate hourly data into daily summaries — min/max/avg temperature, total precipitation, wind extremes |
| Transform 2 | Compare forecast vs. actual — calculate forecast accuracy metrics (MAE, bias) by location and lead time |
| Transform 3 | Detect anomalies — flag days where temperature or precipitation deviates >2σ from 30-day rolling average |
| Load | Write to BigQuery with partitioning by date and clustering by location |
| Monitor | Alert on extreme weather events; track data source availability; flag degrading forecast accuracy |

**AI integration points:**
- Schema design: prompt AI to select and structure the most meaningful variables from Open-Meteo's 60+ available fields
- Generate forecast-vs-actual comparison logic (MAE, bias calculations across locations and lead times)
- Anomaly detection: "Given 30 days of temperature data for these cities, which readings are statistical outliers?"
- AI-generated test cases for edge cases (missing data points, timezone boundaries, leap years)
- Monitoring prompt: "Design alert thresholds for extreme weather that minimize false positives"

**Session milestones:**

| Session | Milestone |
|---------|-----------|
| 0 | Set up repo, verify Open-Meteo API access, select target cities |
| 1 | Define weather metrics, map transformations, draft prompts for pipeline components |
| 2 | Build ingestion (multi-city fetch) + transformation steps with tests |
| 3 | Deploy BigQuery + Cloud Storage + IAM via Terraform |
| 4 | Add monitoring agent: extreme weather alerts, forecast accuracy tracking, data freshness checks |
| 5 | Security audit, error handling, CI/CD, complete documentation |
| 6 | Present |

## Repo Structure

```
my-capstone/
├── README.md                 # What, why, setup, run, test, monitor
├── src/
│   ├── ingestion/           # Data extraction scripts
│   ├── transformation/      # Transform logic (Python)
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

> **Note:** The rubric rewards your learning journey, not just completeness. A thoughtful Tier 2 or Tier 3 presentation (see [Session 6](curriculum/session-06-ship-it/)) that shows genuine learning will score well.
