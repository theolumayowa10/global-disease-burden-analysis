# Global Disease Burden Analysis (2010–2019)

This project explores global disease burden patterns over a 10-year period (2010–2019) using a cleaned dataset of 33,360 records. The analysis focuses on understanding trends across countries, diseases, and age groups, and identifying the major drivers of global health challenges.

## Objectives
- Clean and structure the raw pathology dataset for analysis.  
- Examine global disease trends over time.  
- Identify top diseases contributing to the global burden.  
- Compare disease patterns between countries (e.g., Nigeria vs India).  
- Analyze age-group differences and population percentages.  
- Highlight fastest-growing diseases and year-over-year changes.

## Dataset
- **Years:** 2010–2019  
- **Size:** 33,360 cleaned rows  
- **Columns:** country, ISO-2, measure, age, cause, year, Number, Percent, Rate  
- **Output:** Fully cleaned final dataset (`pathologies_clean_final.csv`)

## Key Insights
- Global disease burden fluctuated between 32–35 billion cases, peaking in 2018.  
- Major contributors include asthma, diabetes mellitus type 2, cardiovascular diseases, and nutritional deficiencies.  
- Protein-energy malnutrition and iodine deficiency showed the fastest growth.  
- Nigeria mirrors global trends but exhibits sharper fluctuations.  
- Ages **5–19** are significantly affected, especially by asthma and malnutrition.  
- Most diseases impact **0–10%** of populations, with some exceeding 15%.

## Analysis Performed
- Time-series analysis of global and country-level trends  
- Ranking of top diseases by total burden  
- Distribution analysis for Percent and Number  
- Year-over-year growth calculation  
- Fastest-growing disease identification  
- Age-group comparison  
- Country comparison (Nigeria vs India)  
- Boxplot variability analysis across diseases

## Technologies Used
- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **NumPy**

## Files Included
- `pathologies_clean_final.csv` — cleaned final dataset  
- `figures/` — all generated charts  
- `Pathologies.ipynb` or `.py` scripts — analysis notebook/code  
- `README.md` — documentation

## Author
**Mayowa Oluyole**  
Data Analyst 

