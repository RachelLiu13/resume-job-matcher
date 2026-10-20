# Resume match: sample_resume → sample_job

**Fit score: 72/100**

Jordan is a solid match on the core analyst profile: about 3 years of e-commerce marketing analytics, SQL, Python (pandas), Tableau, statistics, and exposure to A/B testing on a checkout page. The main gaps are churn/lifetime-value modeling and production data work with dbt/pipelines, and the experimentation experience is described too vaguely to show depth.

## Strengths

- **2+ years of analytics experience** — Marketing Analyst at Brightside Home Goods, 2022–2025 (about 3 years), plus Research Assistant role 2025–2026.
- **Strong SQL and Python (pandas)** — Cleaned customer data in Excel and SQL; built a Python sales forecasting model; skills list Python (pandas, scikit-learn) and SQL.
- **Build dashboards in Tableau** — Research Assistant: built a Tableau dashboard showing forecast accuracy by region; weekly traffic and sales reports at Brightside.
- **Experience with experimentation and statistics** — Helped test two versions of the checkout page; analyzed email campaign results; skills list statistics and regression; M.S. Business Analytics.
- **Clear communication with cross-functional stakeholders** — Told managers which email campaigns worked; produced weekly reports for the marketing team; prepared data so other teams could use it.
- **Growth/funnel domain context** — E-commerce experience with website traffic, email campaigns and checkout conversion, which carries over to sign-up and onboarding funnels.

## Gaps

- **Model churn and lifetime value** (must-have) — No churn or LTV work appears on the resume. Build a portfolio project using a public subscription/churn dataset (e.g., the Telco churn data): a scikit-learn churn classifier plus a simple cohort-based LTV estimate, written up with retention recommendations. In interviews, connect your sales forecasting and regression experience to it.
- **Write production SQL and maintain data pipelines with dbt** (must-have) — Your SQL work was data cleaning, not production pipelines. Complete dbt's free dbt Fundamentals course and build a small dbt project (staging → marts, with tests and docs) on a free warehouse tier. Frame the Brightside data cleaning as preparing reusable datasets for other teams, without overstating it.
- **Design and analyze A/B tests (depth of experimentation)** (must-have) — You have exposure ('helped the team test'), but your role is unclear. If you did any of the design, metric choice, sample size or significance testing, say so explicitly. If not, study power analysis and sequential testing pitfalls, and reanalyze a public A/B test dataset end to end.
- **Looker** (nice-to-have) — The job accepts Tableau or Looker, so your Tableau experience covers this. Optionally, explore Looker Studio to show familiarity.
- **dbt, Snowflake** (nice-to-have) — Neither is on the resume. Snowflake offers a free trial, so you could host the dbt portfolio project there to cover both at once.
- **Causal inference** (nice-to-have) — Not on the resume. Check whether your M.S. coursework covered difference-in-differences or propensity methods, and list it if so. Otherwise, a short applied course or a project measuring the impact of an email campaign would help.

## Suggested bullet rewrites

> **Before:** Helped the team test two versions of the checkout page.
>
> **After:** Supported an A/B test of two checkout page variants, [specify your part: e.g., defining the conversion metric, pulling results in SQL, testing statistical significance].

_Uses the job's 'A/B test' language and forces you to state your actual role. Fill in the bracket only with what you really did._

> **Before:** Analyzed results of email campaigns and told managers which ones worked.
>
> **After:** Analyzed email campaign performance and recommended to marketing managers which campaigns to prioritize.

_Reframes 'told managers' as stakeholder communication and prioritization, which mirrors the job's retention-campaign focus. Add real metrics (open or conversion rates) if you have them._

> **Before:** Cleaned customer data in Excel and SQL so other teams could use it.
>
> **After:** Cleaned and prepared customer datasets in SQL and Excel, making them reusable for cross-functional teams.

_Leads with SQL and stresses reusable data for other teams, which is the closest accurate link to the pipeline and cross-functional requirements._

> **Before:** Made weekly reports on website traffic and sales for the marketing team.
>
> **After:** Delivered weekly website traffic and sales reporting to the marketing team to track funnel performance.

_'Funnel performance' uses growth vocabulary, and 'delivered to the marketing team' shows stakeholder service. Name the tool you used if it was Tableau or Excel._

> **Before:** Built a Python model to forecast monthly store sales; compared it with last year's numbers.
>
> **After:** Built a Python (pandas, scikit-learn) model forecasting monthly store sales and evaluated its accuracy against a prior-year baseline.

_Names the exact stack the job asks for and frames the comparison as baseline evaluation, a modeling skill that transfers to churn and LTV work._

## Likely interview questions

1. Walk me through the checkout A/B test: what was your role, how was the sample size determined, which metric did you use, and how did you decide the result was significant?
2. We need to model churn and lifetime value for subscribers. How would you approach it, and what from your forecasting work would carry over?
3. Have you written SQL that runs in production or used dbt? How would you structure and test a transformation pipeline that feeds a growth dashboard?

## Keyword check (no AI)

Skills named in the job that also appear in the resume: **50%**

- Matched: Python, SQL, Tableau, data visualization, pandas, statistics
- Missing: A/B testing, ETL, Snowflake, causal inference, dbt, stakeholder management
