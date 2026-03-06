# Where AI Falls Short for Data Engineers

AI coding assistants are powerful for generating boilerplate, writing tests, and scaffolding pipelines. But there are areas where AI consistently underperforms — and a data engineer's judgment is irreplaceable.

Know these limits so you can use AI effectively and catch its mistakes.

## Areas Where AI Struggles

### 1. Partition Strategy
AI will generate valid partitioning configs, but it doesn't know your query patterns, data volume growth, or cost constraints. A partition on `created_date` is reasonable but may be wrong if 90% of your queries filter by `region`.

**What to do:** Define your partition and clustering strategy based on your actual query patterns, then ask AI to implement it.

### 2. Cost Optimization
AI defaults to "works correctly" not "works cheaply." It won't flag that a `SELECT *` in a BigQuery transformation scans the full table, or that your Cloud Function is over-provisioned.

**What to do:** Review AI-generated queries for full table scans, unnecessary columns, and resource sizing. Check your billing dashboard regularly.

### 3. Late-Arriving Data
Handling records that arrive after a batch has already processed is a design decision, not a code generation task. AI will give you a working approach but not necessarily the right one for your SLA.

**What to do:** Define your late-arrival policy (reprocess, append, ignore) before asking AI to implement it.

### 4. Slowly Changing Dimensions (SCD)
AI can generate SCD Type 1 or Type 2 logic, but choosing between them requires understanding business requirements: does anyone need historical values? How often do dimensions change? What's the query impact of Type 2?

**What to do:** Decide the SCD type based on business needs. Then use AI to implement the merge/upsert logic.

### 5. Complex Business Rules
"Revenue = quantity * price" is easy. "Revenue = quantity * price, unless the customer has a volume discount tier, which is retroactively applied at quarter-end, and excludes promotional items unless the promotion was approved by category managers" is not.

**What to do:** Document business rules in plain language first. Feed them to AI as a spec, then verify every edge case.

### 6. Performance Tuning
AI can write a correct query, but it can't analyze your execution plan, identify skewed joins, or know that your `user_events` table has a 100:1 skew on `user_id = 'anonymous'`.

**What to do:** Use AI to write the first draft, then profile with `EXPLAIN`, check for data skew, and optimize based on actual metrics.

### 7. Data Governance Decisions
Which fields are PII? What's the retention policy? Who should have access? These are organizational and legal decisions, not code decisions.

**What to do:** Define governance policies with your team/legal. Use AI to implement them (masking, access controls, retention rules) but never to decide them.

## The Pattern

In every case, the pattern is the same:

1. **You decide** the approach (partition strategy, business rules, governance policy)
2. **AI implements** the decision (writes the code, config, or test)
3. **You verify** the implementation (review, test, profile)

AI is a force multiplier for implementation. It is not a substitute for engineering judgment.
