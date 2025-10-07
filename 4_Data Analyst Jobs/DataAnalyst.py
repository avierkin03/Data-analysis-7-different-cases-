import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DataAnalyst.csv')


# Витягуємо мінімальну та максимальну зарплату зі стовпця "Salary Estimate"
# salary_pattern = r'\$([\dK]+)-\$([\dK]+)' - це регулярний вираз (regex), який визначає шаблон для пошуку зарплат у форматі, наприклад, $50K-$70K
# \$ - символ $, екранований через \, бо $ має спеціальне значення в regex
# ([\dK]+) — група, яка захоплює одне або більше (+) значень:
#               \d - будь-яка цифра (0–9)
#               K - символ K, який часто використовується для позначення тисяч
# - — дефіс, що відокремлює мінімальну та максимальну зарплату
# \$([\dK]+) - друга група, яка захоплює значення для максимальної зарплати (так само, як і перша)
salary_pattern = r'\$([\dK]+)-\$([\dK]+)'
# str.extract - це метод Pandas, який дозволяє застосувати регулярний вираз до рядків у колонці DataFrame
# Метод знаходить усі відповідності регулярному виразу в колонці Salary Estimate.
# Якщо регулярний вираз має групи (вказані у круглих дужках ()), то метод повертає результат у вигляді DataFrame, де кожна група стає окремою колонко
df[['Min Salary', 'Max Salary']] = df['Salary Estimate'].str.extract(salary_pattern)

# Перетворюємо отримані значення зарплати в числові (у тисячах)
def convert_salary(salary):
    if 'K' in salary:
        return int(salary.replace('K', '')) * 1000
    return int(salary)

df['Min Salary'] = df['Min Salary'].fillna('0').apply(convert_salary)
df['Max Salary'] = df['Max Salary'].fillna('0').apply(convert_salary)



# ------------------------------------------- 1. Розподіл зарплати для посад аналітика даних -------------------------------------------
# перетворюємо таблицю із двома стовпцями - Min Salary і Max Salary - на довгий формат (long format) з одним стовпцем Salary
salary_data = df[['Min Salary', 'Max Salary']].melt(value_name='Salary')

# Побудова гістограми 
salary_data['Salary'].plot.hist(
    bins=30, 
    color='skyblue', 
    figsize=(12, 6), 
    title='Salary Estimates Distribution for Data Analyst Positions')
plt.xlabel('Salary (in USD)')
plt.ylabel('Frequency')
plt.show()


# ------------------------------------------- 2. 10 найкращих вакансій для аналітиків даних -------------------------------------------
df['Job Title'].value_counts().head(10).plot(kind='bar', color='coral', figsize=(12, 6))
plt.title('10 Best Jobs for Data Analysts')
plt.xlabel('Job title')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# ------------------------------------------- 3. Розподіл рейтингів компаній -------------------------------------------
# Побудова boxplot 
plt.figure(figsize=(8, 6))  # Розмір графіка
df['Rating'].plot.box(
    vert=False,  # Горизонтальний boxplot
    patch_artist=True,  # Заливка прямокутника кольором
    color=dict(boxes='skyblue', whiskers='black', medians='red', caps='black')  # Кольори для елементів
)
plt.title('Distribution of company ratings')  # Заголовок
plt.xlabel('Rating')  # Підпис осі X
plt.show()



# ------------------------------------------- 4. 10 найкращих галузей для посад аналітика даних-------------------------------------------
industry_counts = df['Industry'].value_counts().head(10)
industry_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Set3', figsize=(10, 8))
plt.title('10 Best Industries for Data Analyst Jobs')
plt.ylabel('')  # Hide the y-label
plt.show()



# ------------------------------------------- 5. Рейтинги порівняно з мінімальною зарплатою за галузями-------------------------------------------
df.plot(x = "Rating", y = "Min Salary", kind = "scatter", figsize=(10, 4))
plt.title('Ratings compared to minimum wage by industry')  # Заголовок
plt.xlabel('Company rating')  # Підпис осі X
plt.ylabel('Minimum wage (in US dollars)')  # Підпис осі Y
plt.show()


# ------------------------------------------- 6. Рейтинги порівняно з максимальною зарплатою за галузями-------------------------------------------
df.plot(x = "Rating", y = "Max Salary", kind = "scatter", figsize=(10, 4))
plt.title('Ratings compared to maximum salary by industry')  # Заголовок
plt.xlabel('Company rating')  # Підпис осі X
plt.ylabel('Maximum wage (in US dollars)')  # Підпис осі Y
plt.show()