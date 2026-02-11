---
name: data-science
description: Analyzes datasets (CSV/JSON/SQL) and generates visualizations.
inputs:
  - data_source: "(Required) File path or SQL query result."
  - analysis_goal: "(Required) What do you want to know? (e.g., 'Trend over time')"
outputs:
  - insight_text: "Summary of findings."
  - visualization_code: "Python code (Matplotlib/Seaborn) to generate charts."
---

# Data Science Protocol

## 1. Tooling (The Lab)
* **Language:** Python (Pandas, Matplotlib, Seaborn).
* **Action:**
    1.  Load data into a DataFrame.
    2.  Clean data (Handle missing values).
    3.  Perform statistical analysis (Mean, Median, Correlation).

## 2. Visualization (The Art)
* **Rule:** Always verify if a chart is better than a table.
* **Types:**
    * **Time Series:** Line Chart.
    * **Distribution:** Histogram/Box Plot.
    * **Comparison:** Bar Chart.

## 3. Output Format
Provide the analysis in a clean Markdown report with the Python code block for reproduction.