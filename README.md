# Data Analysis Projects Repository

This repository contains 7 folders, each dedicated to a specific data analysis project using Python and Pandas. Each folder includes a Python script (`.py`) for data processing, analysis, and visualization, along with the corresponding CSV dataset. The analyses cover various domains such as education, global economics, nutrition, job market, space exploration, movies, and venture capital investments.

The Python scripts perform data cleaning, statistical calculations, hypothesis testing (where applicable), and generate visualizations using Matplotlib and other libraries. Below is a detailed description of each project, including the key analyses performed. Each section also includes a dedicated subsection for screenshots of the generated graphs, where you can insert images (e.g., via GitHub uploads or links).

## 1. Tests Results Analysis (Folder: 1_testsResults)

### Description
This project analyzes student performance data from the "StudentsPerformance.csv" dataset. It tests two main hypotheses:
- Hypothesis 1: Attending test preparation courses improves exam results for students whose parents do not have higher education. The analysis groups data by parental education level, calculates average scores for students with and without courses, and computes progress differences. Visualizations include bar charts for average results.
- Hypothesis 2: Students who had a proper breakfast perform better on tests. The analysis groups data by lunch type (standard vs. free/reduced), calculates average scores, and visualizes results using pie charts, bar charts, and box plots.

Key operations include data loading, creating average score columns, filtering, grouping, and plotting. Conclusions are drawn based on the results, rejecting or confirming the hypotheses.

### Screenshots
- ![Hypothesis 1: Average Results by Parental Education (With Courses)](screenshots/TestsResults/screenshot1-1.png)
- ![Hypothesis 1: Average Results by Parental Education (Without Courses)](screenshots/TestsResults/screenshot1-2.png)
- ![Hypothesis 2: Average Results by Lunch Type (Pie Chart)](screenshots/TestsResults/screenshot1-3.png)
- ![Hypothesis 2: Average Results by Lunch Type (Bar Chart)](screenshots/TestsResults/screenshot1-4.png)
- ![Hypothesis 2: Box Plot for Free/Reduced Lunch](screenshots/TestsResults/screenshot1-5.png)
- ![Hypothesis 2: Box Plot for Standard Lunch](screenshots/TestsResults/screenshot1-6.png)


## 2. Countries of the World Analysis (Folder: 2_countries)

### Description
This project analyzes global country data from the "countries of the world.csv" dataset. It focuses on population distribution, GDP comparisons, and correlations with factors like phone ownership, literacy, birthrate, and deathrate. Key analyses include:
- Histogram of population (up to 200 million).
- Bar chart of average GDP by region.
- Scatter plots for GDP vs. phones per 1000, literacy, birthrate, and deathrate.
- Bar charts for maximum GDP per region and countries with the highest GDP in each region.

Data cleaning involves converting comma-separated decimals to floats. Conclusions highlight economic disparities, correlations with wealth, and outliers like Monaco.

### Screenshots
- ![Population Distribution Histogram](screenshots/Countries/screenshot2-1.png)
- ![Average GDP by Region (Bar Chart)](screenshots/Countries/screenshot2-2.png)
- ![GDP vs. Phones per 1000 (Scatter Plot)](screenshots\Countries\screenshot2-3.png)
- ![GDP vs. Literacy (Scatter Plot)](screenshots/Countries/screenshot2-4.png)
- ![GDP vs. Birthrate (Scatter Plot)](screenshots/Countries/screenshot2-5.png)
- ![GDP vs. Deathrate (Scatter Plot)](screenshots/Countries/screenshot2-6.png)
- ![Maximum GDP per Region (Bar Chart)](screenshots/Countries/screenshot2-7.png)
- ![Countries with Highest GDP per Region (Bar Chart with Labels)](screenshots/Countries/screenshot2-8.png)


## 3. McDonald's Menu Analysis (Folder: 3_Menu)

### Description
This project analyzes nutritional data from McDonald's menu in the "McDonalds_Menu.csv" dataset. It examines vitamins, minerals, sugars, calories, and other metrics across categories. Key analyses include:
- Average % Daily Value for Vitamin A, C, Calcium, and Iron by category (pie and bar charts).
- Average sugars and calories by category (bar charts).
- Ratio of Vitamin A to C.
- Percentage of calories from fat.
- Most common product categories (bar chart).
- Average protein by category (bar chart).
- Correlation between total calories and calories from fat (scatter plot).
- Top 5 heaviest items by serving size (bar chart).

Data processing includes extracting grams from serving sizes and grouping by categories.

### Screenshots
- ![Vitamin A % by Category (Pie Chart)](screenshots/Menu/screenshot3-1.png)
- ![Vitamin A % by Category (Bar Chart)](screenshots/Menu/screenshot3-2.png)
- ![Vitamin C % by Category (Pie Chart)](screenshots/Menu/screenshot3-3.png)
- ![Vitamin C % by Category (Bar Chart)](screenshots/Menu/screenshot3-4.png)
- ![Calcium % by Category (Pie Chart)](screenshots/Menu/screenshot3-5.png)
- ![Calcium % by Category (Bar Chart)](screenshots/Menu/screenshot3-6.png)
- ![Iron % by Category (Pie Chart)](screenshots/Menu/screenshot3-7.png)
- ![Iron % by Category (Bar Chart)](screenshots/Menu/screenshot3-8.png)
- ![Sugars by Category (Bar Chart)](screenshots/Menu/screenshot3-9.png)
- ![Calories by Category (Bar Chart)](screenshots/Menu/screenshot3-10.png)
- ![Product Categories Count (Bar Chart)](screenshots/Menu/screenshot3-11.png)
- ![Protein by Category (Bar Chart)](screenshots/Menu/screenshot3-12.png)
- ![Calories vs. Calories from Fat (Scatter Plot)](screenshots/Menu/creenshot3-13.png)
- ![Top 5 Heaviest Items (Bar Chart)](screenshots/Menu/screenshot3-14.png)


## 4. Data Analyst Jobs Analysis (Folder: 4_Data Analyst Jobs)

### Description
This project analyzes job listings for Data Analysts from the "DataAnalyst.csv" dataset. It extracts and processes salary estimates, ratings, and other job details. Key analyses include:
- Histogram of salary distribution (min and max).
- Bar chart of top 10 job titles.
- Box plot of company ratings.
- Pie chart of top 10 industries.
- Scatter plots of ratings vs. min/max salary.

Data cleaning involves regex extraction of salary ranges and conversion to numeric values.

### Screenshots
- ![Salary Distribution Histogram](screenshots/DataAnalystJobs/screenshot4-1.png)
- ![Top 10 Job Titles (Bar Chart)](screenshots/DataAnalystJobs/screenshot4-2.png)
- ![Company Ratings Box Plot](screenshots/DataAnalystJobs/screenshot4-3.png)
- ![Top 10 Industries (Pie Chart)](screenshots/DataAnalystJobs/screenshot4-4.png)
- ![Ratings vs. Min Salary (Scatter Plot)](screenshots/DataAnalystJobs/screenshot4-5.png)
- ![Ratings vs. Max Salary (Scatter Plot)](screenshots/DataAnalystJobs/screenshot4-6.png)


## 5. Space Analysis (Folder: 5_Space)

### Description
This project analyzes space mission data from the "Space_Corrected.csv" dataset. It explores launches by companies, statuses, years, and countries. Key analyses include:
- Bar chart of top 10 companies by launches.
- Pie chart of rocket statuses.
- Bar chart of mission statuses.
- Bar and line charts of missions per year.
- Line plots of launches per year for selected companies (NASA, ISRO, CASC, SpaceX).
- Bar chart of launches by top 10 countries.
- Subplots of mission status percentages by country (using Plotly).

Data processing includes date parsing for years and country extraction from locations.

### Screenshots
- ![Top 10 Companies by Launches (Bar Chart)](screenshots/Space/screenshot5-1.png)
- ![Rocket Statuses (Pie Chart)](screenshots/Space/screenshot5-2.png)
- ![Mission Statuses (Bar Chart)](screenshots/Space/screenshot5-3.png)
- ![Missions per Year (Bar Chart)](screenshots/Space/screenshot5-4.png)
- ![Missions per Year (Line Chart)](screenshots/Space/screenshot5-5.png)
- ![Launches per Year by Selected Companies (Subplots)](screenshots/Space/screenshot5-6.png)
- ![Launches by Top 10 Countries (Bar Chart)](screenshots/Space/screenshot5-7.png)
- ![Mission Statuses by Country (Subplots)](screenshots/Space/screenshot5-8.png)


## 6. IMDB Movies Analysis (Folder: 6_IMDB)

### Description
This project analyzes IMDB movie data from the "IMDB-Movie-Data.csv" dataset. It focuses on genres, ratings, revenues, and trends over years. Key analyses include:
- Scatter plot of films per director vs. average rating.
- Pie chart of films by number of genres.
- Bar charts for revenue, Metascore, votes, and runtime by number of genres or year.
- Line and bar charts for average votes and revenue by year.
- Scatter plot of rating vs. revenue.
- Line chart of average runtime by year.
- Top 10 directors by average rating.
- Bar charts comparing Rating and Metascore by number of genres.

Data processing includes splitting genres and calculating genre counts.

### Screenshots
- ![Films per Director vs. Average Rating (Scatter Plot)](screenshots/IMDB/screenshot6-1.png)
- ![Films by Number of Genres (Pie Chart)](screenshots/IMDB/screenshot6-2.png)
- ![Revenue by Number of Genres (Bar Chart)](screenshots/IMDB/screenshot6-3.png)
- ![Metascore by Number of Genres (Bar Chart)](screenshots/IMDB/screenshot6-4.png)
- ![Votes by Year (Line Chart)](screenshots/IMDB/screenshot6-5.png)
- ![Votes by Year (Bar Chart)](screenshots/IMDB/screenshot6-6.png)
- ![Revenue by Year (Bar Chart)](screenshots/IMDB/screenshot6-7.png)
- ![Rating vs. Revenue (Scatter Plot)](screenshots/IMDB/screenshot6-8.png)
- ![Average Runtime by Year (Line Chart)](screenshots/IMDB/screenshot6-9.png)
- ![Rating vs. Metascore by Genres (Side-by-Side Bar Charts)](screenshots/IMDB/screenshot6-10.png)


## 7. Investments VC Analysis (Folder: 7_Investments)

### Description
This project analyzes venture capital investment data from the "investments_VC.csv" dataset. It explores startups by location, funding, and categories. Key analyses include:
- Bar and pie charts of top 5 cities by startup count.
- Bar chart of startups with/without grants.
- Most successful quarter and year by startup count.
- Bar and pie charts of top 5 years by startup count.
- Bar and pie charts of top 5 categories by startup count.

Data cleaning involves stripping strings and handling NaNs.

### Screenshots
- ![Top 5 Cities by Startups (Bar Chart)](screenshots/Investments/screenshot7-1.png)
- ![Top 5 Cities by Startups (Pie Chart)](screenshots/Investments/screenshot7-2.png)
- ![Startups with/without Grants (Bar Chart)](screenshots/Investments/screenshot7-3.png)
- ![Top 5 Years by Startups (Bar Chart)](screenshots/Investments/screenshot7-4.png)
- ![Top 5 Years by Startups (Pie Chart)](screenshots/Investments/screenshot7-5.png)
- ![Top 5 Categories by Startups (Bar Chart)](screenshots/Investments/screenshot7-6.png)
- ![Top 5 Categories by Startups (Pie Chart)](screenshots/Investments/screenshot7-7.png)
