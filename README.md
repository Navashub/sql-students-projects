# Retail Sales Analytics Project

A comprehensive data analytics project analyzing retail sales transactions across product categories, customer demographics, and temporal patterns. This project demonstrates end-to-end analytics from data exploration to executive-level insights and recommendations.

**Status:** ✅ Complete | **Dataset:** 1,000 retail transactions | **Date Range:** 2023-2024

---

## 📋 Project Overview

This project analyzes a retail sales dataset containing 1,000 transactions across three product categories (Beauty, Clothing, Electronics) with customer demographics and transaction details. The analysis provides actionable insights for business decision-making at the CEO/Director level.

### Key Learning Objectives
- Data exploration and statistical analysis
- Customer segmentation and behavioral insights
- Time-series and category performance analysis
- Translating data into business recommendations
- Presenting analytical findings to executives

---

## 📁 Project Structure

```
sql-students-projects/
├── README.md                                    # This file
├── CEO_DIRECTOR_QUESTIONS.md                    # Executive review criteria & expected answers
├── RETAIL SALES ANALYTICS PROJECT.pdf           # Project requirements & specifications
├── retail_sales_dataset.csv                     # Dataset (1,000 transactions)
├── analyze_sales.py                             # Data analysis script
├── load_to_neon.py                              # Neon PostgreSQL data loader
└── .gitignore                                   # Git configuration
```

---

## 📊 Dataset Details

### File: `retail_sales_dataset.csv`

**Records:** 1,000 retail transactions  
**Date Range:** January 2023 - December 2024  
**Time Period:** Full year data

### Columns:
| Column | Type | Description |
|--------|------|-------------|
| `Transaction ID` | Integer | Unique transaction identifier (1-1000) |
| `Date` | Date | Transaction date (YYYY-MM-DD) |
| `Customer ID` | Text | Customer identifier (CUST001-CUST1000) |
| `Gender` | Text | Male / Female |
| `Age` | Integer | Customer age (18-64) |
| `Product Category` | Text | Beauty / Clothing / Electronics |
| `Quantity` | Integer | Units purchased (1-4) |
| `Price per Unit` | Numeric | Unit price ($25-$500) |
| `Total Amount` | Numeric | Transaction total ($25-$2,000) |

### Sample Data:
```
Transaction ID,Date,Customer ID,Gender,Age,Product Category,Quantity,Price per Unit,Total Amount
1,2023-11-24,CUST001,Male,34,Beauty,3,50,150
2,2023-02-27,CUST002,Female,26,Clothing,2,500,1000
3,2023-01-13,CUST003,Male,50,Electronics,1,30,30
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- Virtual environment (`.venv/`)
- PostgreSQL/Neon database access (optional)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Navashub/sql-students-projects.git
   cd sql-students-projects
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install pandas psycopg
   ```

---

## 📈 Analysis Scripts

### 1. `analyze_sales.py` - Data Analysis

**Purpose:** Perform exploratory data analysis and generate business insights

**Functionality:**
- Load CSV dataset into pandas DataFrame
- Generate summary statistics
- Segment customers by age groups
- Analyze revenue by category, quarter, gender, and age
- Identify weekend vs. weekday patterns
- Create demographic-based customer segments

**Usage:**
```bash
python analyze_sales.py
```

**Output:**
- Revenue by product category
- Quarterly performance trends
- Gender-based purchasing patterns
- Age group segmentation
- Weekend vs. weekday comparison
- Customer-category preferences

---

### 2. `load_to_neon.py` - Database Loading

**Purpose:** Load retail sales data into Neon PostgreSQL database

**Features:**
- Creates `retail_sales` table if not exists
- Uses efficient COPY command for bulk insert
- Handles CSV header row automatically
- Verifies row count after load

**Usage:**
```bash
python load_to_neon.py
```

**Database Connection:**
```
postgresql://neondb_owner:password@endpoint.neon.tech/neondb
```

**Expected Output:**
```
row_count 1000
```

---

## 📋 Key Analysis Questions & Expected Insights

The project is designed to prepare students to answer executive-level questions:

### Revenue & Profitability
- ✅ What is total revenue by category?
- ✅ Which quarters performed best?
- ✅ What is average transaction value by category?

### Customer Insights
- ✅ Who are our most valuable customer segments?
- ✅ Do gender and age affect purchasing patterns?
- ✅ What are the demographic characteristics?

### Operational Efficiency
- ✅ What is average order size?
- ✅ Do weekends outperform weekdays?
- ✅ Which products are underperforming?

### Strategic Recommendations
- ✅ Which category should we expand?
- ✅ What is our growth trajectory?
- ✅ What are actionable next steps?

**See `CEO_DIRECTOR_QUESTIONS.md` for detailed expectations and evaluation rubric.**

---

## 🎯 Expected Deliverables

When presenting this analysis, students should provide:

### 1. Executive Summary (1-2 slides)
- Key metrics at a glance
- Top findings
- Recommended actions

### 2. Detailed Analysis (3-5 slides)
- Revenue breakdown by category/quarter
- Customer demographic analysis
- Performance trends
- Comparative metrics (weekend vs. weekday, gender, age groups)

### 3. Visualizations
- Bar charts: Revenue by category
- Pie charts: Market share
- Line graphs: Quarterly trends
- Heat maps: Customer segments

### 4. Recommendations
- Top 3 actionable insights
- Expected business impact
- Implementation timeline
- Success metrics

### 5. Data Quality Discussion
- Dataset overview
- Analysis methodology
- Assumptions & limitations
- Further analysis needed

---

## 🔍 How to Analyze the Data

### Basic Workflow:

1. **Explore the Dataset**
   ```python
   import pandas as pd
   df = pd.read_csv('retail_sales_dataset.csv')
   print(df.info())
   print(df.describe())
   ```

2. **Run the Analysis Script**
   ```bash
   python analyze_sales.py
   ```

3. **Segment Customers**
   - By age: 18-30, 31-45, 46-60, 60+
   - By gender: Male/Female
   - By product preference: Category analysis

4. **Time-Series Analysis**
   - Convert date to datetime
   - Group by quarter, month, day of week
   - Identify seasonal patterns

5. **Comparative Analysis**
   - Weekend vs. Weekday
   - High-value vs. Low-value customers
   - Category performance rankings

6. **Statistical Insights**
   - Average, median, standard deviation
   - Percentile analysis
   - Correlation analysis

---

## 💡 Analysis Tips

✅ **Do:**
- Use specific numbers and percentages
- Compare categories and segments
- Identify trends and patterns
- Provide business context for every finding
- Support recommendations with data

❌ **Don't:**
- Make vague claims ("sales are good")
- Ignore underperforming segments
- Skip methodology explanation
- Present only totals without breakdown
- Forget to discuss data quality

---

## 📌 Neon Database Setup (Optional)

If using PostgreSQL for analysis:

1. **Connection String:**
   ```
   postgresql://neondb_owner:password@ep-square-credit-anpj5kzh-pooler.c-6.us-east-1.aws.neon.tech/neondb
   ```

2. **Load Data:**
   ```bash
   python load_to_neon.py
   ```

3. **Query Data:**
   ```sql
   SELECT COUNT(*) FROM retail_sales;
   SELECT COUNT(DISTINCT customer_id) FROM retail_sales;
   SELECT product_category, COUNT(*) FROM retail_sales GROUP BY product_category;
   ```

---

## 📚 Resources

- **Project Brief:** `RETAIL SALES ANALYTICS PROJECT.pdf`
- **CEO Review Guide:** `CEO_DIRECTOR_QUESTIONS.md`
- **Dataset:** `retail_sales_dataset.csv`

---

## ✅ Checklist Before Presentation

- [ ] Analyzed all three product categories
- [ ] Compared performance across quarters
- [ ] Segmented customers by demographics
- [ ] Analyzed weekend vs. weekday patterns
- [ ] Generated at least 3 recommendations
- [ ] Created visualizations for key metrics
- [ ] Prepared answers to CEO questions
- [ ] Verified data quality and assumptions
- [ ] Practiced presentation (5-10 minutes)
- [ ] Prepared for follow-up questions

---

## 🤝 Contributing

This is a student project. For questions or improvements:
1. Review the project requirements (PDF)
2. Check the CEO questions guide
3. Refer to the analysis scripts

---

## 📄 License

Educational project - All rights reserved.

---

**Last Updated:** May 12, 2026  
**Project Status:** ✅ Complete  
**Commits:** 5 organized commits to GitHub
