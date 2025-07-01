# Custom Event Tracking System

**Tools:** JavaScript, Google Analytics 4 (GA4), BigQuery, Python  
**Type:** Analytics | User Behavior Tracking | Retention Analysis

---

## Project Objective

Build a custom event-tracking framework for a SaaS dashboard to:
- Track feature usage and user interactions
- Export GA4 event data to BigQuery
- Perform cohort and retention analysis with Python

---

## Tools & Stack

- JavaScript (frontend event tracking)
- Google Analytics 4 (event collection)
- BigQuery (data warehousing)
- Python (analysis & visualization)

---

##  Project Structure

| Folder       | Description                             |
|--------------|-----------------------------------------|
| `web/`       | Demo HTML app with trackable elements   |
| `analytics/` | JS script for GA4 custom tracking       |
| `bigquery/`  | Python script for cohort analysis       |
| `data/`      | Sample exported data (mock or real)     |

---

##  Live Tracking Example

```html
<button data-button-name="Save Report" class="trackable-button">Save Report</button>
