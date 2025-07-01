from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

client = bigquery.Client()

# project and dataset
query = """
SELECT
  user_pseudo_id,
  MIN(PARSE_DATE('%Y%m%d', event_date)) AS cohort_date,
  PARSE_DATE('%Y%m%d', event_date) AS activity_date
FROM
  `your_project_id.analytics_34256.events_*`
WHERE
  event_name = 'button_click'
GROUP BY user_pseudo_id, event_date
"""

df = client.query(query).to_dataframe()

# Cohort index: days since first use
df['days_since'] = (df['activity_date'] - df['cohort_date']).dt.days

# Count users by cohort and day
cohort_data = df.groupby(['cohort_date', 'days_since'])['user_pseudo_id'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='cohort_date', columns='days_since', values='user_pseudo_id').fillna(0)

# Plot
plt.figure(figsize=(12,6))
sns.heatmap(cohort_pivot, cmap='Blues', linewidths=0.5)
plt.title('Cohort Retention: Button Click Events')
plt.xlabel('Days Since First Interaction')
plt.ylabel('Cohort Start Date')
plt.tight_layout()
plt.show()
