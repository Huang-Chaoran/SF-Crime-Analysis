## Project Highlights

- Analyzed 2.2 million crime records
- Built using Apache Spark and Databricks
- Applied Spark SQL for large-scale aggregation
- Identified temporal crime patterns
- Performed spatial hotspot detection using K-Means clustering
- Generated actionable insights for public safety planning

# San Francisco Crime Analysis using Spark SQL and K-Means

## Project Overview

This project analyzes historical crime incidents in San Francisco from 2003 to May 2018 using Apache Spark, Spark SQL and K-Means clustering.

The objective is to identify:

- Crime category patterns
- Geographic crime hotspots
- Temporal crime trends
- District-level crime distributions

The project was completed using Databricks and PySpark.

---

## Dataset

Dataset Source:

https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry

Dataset Information:

- Time Period: 2003 – May 2018
- Records: Approximately 2.2 million
- Fields:
  - Crime Category
  - Date
  - Time
  - Police District
  - Geographic Coordinates
  - Resolution Status

The original dataset is not included in this repository due to its large size.

---

## Technologies

- Apache Spark
- Spark SQL
- PySpark
- Databricks
- K-Means Clustering
- Data Visualization

---

# Analysis 1: Crime Category Distribution

The most common crime category is LARCENY/THEFT.

Property-related crimes account for a significant proportion of all incidents.

!(<img width="1051" height="500" alt="visualization" src="https://github.com/user-attachments/assets/e709fbf2-9b6b-4531-8b10-f3d876ac1c34" />
)

---

# Analysis 2: Crime Distribution by District

The Southern district reports the highest crime volume, suggesting that public safety resources and patrol planning should prioritize this area.

<img width="1051" height="500" alt="visualization (5)" src="https://github.com/user-attachments/assets/adfbcf24-3959-45cb-9dd4-80b0c17d80a6" />


---

# Analysis 3: Crime by Day of Week

Crime activity tends to increase toward weekends.

Friday records the highest number of incidents.

<img width="1051" height="500" alt="visualization (6)" src="https://github.com/user-attachments/assets/378fe7b0-12aa-451f-8cd1-585e0773c2a1" />


---

# Analysis 4: Crime Trend by Year

Crime volume remains relatively stable between 2003 and 2017.

The decline observed in 2018 is due to incomplete data collection (January–May only).

<img width="1051" height="500" alt="visualization (1)" src="https://github.com/user-attachments/assets/859fcd3c-27e9-476c-b687-fb57777eeabb" />


---

# Analysis 5: Crime Activity by Hour

Crime incidents are lowest during early morning hours.

Crime activity peaks during afternoon and evening hours, indicating periods where increased police presence may improve crime prevention.

<img width="1051" height="500" alt="visualization (2)" src="https://github.com/user-attachments/assets/9d07b8fd-4fd1-4fab-9171-f503769a0186" />


---

# Analysis 6: Spatial Crime Hotspots (K-Means)


K-Means clustering was applied to geographic coordinates (longitude and latitude).

Five distinct crime hotspot regions were identified across San Francisco.

The clustering results reveal that crime incidents are not uniformly distributed but are concentrated in specific urban areas.

These findings can support:

- Resource allocation
- Patrol route planning
- Crime prevention strategies
- Urban safety management

<img width="1051" height="500" alt="visualization (3)" src="https://github.com/user-attachments/assets/001323f9-46e3-4998-8fbe-b931b2cb928e" />

<img width="1051" height="500" alt="visualization (4)" src="https://github.com/user-attachments/assets/c99d53d8-67cb-48ac-a260-fbe267557aa8" />


---

# Key Findings

1. LARCENY/THEFT is the dominant crime category.
2. Southern district experiences the highest crime volume.
3. Crime activity increases toward weekends.
4. Evening hours show the highest crime frequency.
5. Crime incidents are geographically concentrated in several hotspot regions.

---

## Repository Structure

```text
SF-Crime-Analysis/
│
├── README.md
├── sf_crime_analysis.py
└── images/
    ├── crime_category_distribution.png
    ├── district_analysis.png
    ├── day_of_week_distribution.png
    ├── yearly_trend.png
    ├── hourly_trend.png
    ├── cluster_count.png
    └── spatial_clusters.png
```


