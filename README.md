# Bat vs. Rat: The Forage Files - Investigation A
## HIT140 Foundations of Data Science - Assessment 2

### Team Members
- **Harsh Rastogi** - Data Analysis & Statistical Testing
- Renish - Data Visualization & Interpretation  
- Hena Akter - Data Exploration & Documentation
- Princy - Research Methodology & Presentation

### Project Overview
This repository contains our team's statistical analysis investigating whether Egyptian Fruit Bats (Rousettus aegyptiacus) perceive Black Rats (Rattus rattus) as potential predators rather than mere food competitors.

### Research Question (Investigation A)
Do bats perceive rats not just as competitors for food but also as potential predators ?

### Key Findings
- Risk-avoiding bats: 84.3% success rate (386/458 attempts)
- Risk-taking bats: 21.8% success rate (98/449 attempts)  
- Statistical significance: Chi-square = 352.83, p < 0.000001
- Conclusion: Strong evidence that bats perceive rats as predators

### Repository Structure
```
HIT140_G51_A2/
├── data/
│   ├── dataset1.csv          # Individual bat landing events
│   └── dataset2.csv          # 30-minute observation periods
├── analysis.py               # Complete exploratory analysis
├── final_analysis.py         # Clean final analysis code
├── bat_behavior_analysis.png # Detailed visualization
├── final_results.png         # Summary visualization
├── presentation_script.md    # Team presentation talking points
└── README.md                # This file
```

### Files to Submit
1. GitHub Repository URL: Contains all analysis code and documentation
2. YouTube Presentation URL: 10-minute team presentation (unlisted)

### Analysis Summary
Our analysis of 907 bat landing events revealed that bats exhibiting risk-avoidance behavior (avoiding confrontation with rats) achieved significantly higher foraging success compared to bats that engaged in risk-taking behavior (attacking or confronting rats). This pattern provides strong evidence that bats perceive rats as predatory threats rather than simple food competitors.

### Methodology
1. Data Exploration: Examined 907 bat landing events and 2,123 observation periods
2. Descriptive Analysis: Calculated success rates and timing patterns by risk behavior
3. Statistical Testing: Chi-square test confirming significant behavioral differences
4. Visualization**: Created charts showing success rate disparities

### Key Variables Analyzed
- `risk`: Risk-taking (1) vs. risk-avoidance (0) behavior
- `reward`: Foraging success (1) vs. failure (0)
- `bat_landing_to_food`: Time delay before approaching food
- `seconds_after_rat_arrival`: Timing relative to rat presence

### Statistical Results
- Chi-square statistic: 352.83
- P-value: < 0.000001 (highly significant)
- Effect size: Risk-avoiders are 4x more successful
- Sample size: 907 observations

### Tools Used
- Python 3.x - Primary analysis language
- pandas - Data manipulation and analysis
- matplotlib - Data visualization
- scipy.stats - Statistical testing

### Academic Integrity Statement
This analysis adheres to CDU's academic integrity policies. All statistical analyses are conducted ethically with proper documentation of methodology and assumptions.

### Data Source
Chen, Xing; Harten, Lee; Rachum, Adi; Attia, Liraz; Yovel, Yossi (2025), "Complex competition interactions between Egyptian fruit bats and black rats in the real world", Mendeley Data, V1, doi: 10.17632/gt7j39b2cf.1 (License CC BY 4.0)

### Course Information
- Course: HIT140 Foundations of Data Science
- Institution: Charles Darwin University  
- Instructor: Dr Yakub Sebastian
- Assessment: Group Project - Assessment 2
- Due Date: 11 September 2025, 14:00 ACST
