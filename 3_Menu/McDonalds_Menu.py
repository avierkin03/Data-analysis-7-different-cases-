import pandas as pd
import matplotlib.pyplot as plt
import math

# Завантажуємо дані з CSV файлу
df = pd.read_csv('McDonalds_Menu.csv')
print(df.info())
print(df.head())


#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми вітаміну А?
df.groupby(by="Category")["Vitamin A (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='pie', 
    ylabel="",
    title="Vitamin A (% Daily Value) different menu categories")
plt.show()
df.groupby(by="Category")["Vitamin A (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='barh', 
    figsize=(10,5),
    title="Vitamin A (% Daily Value) different menu categories",
    xlabel="% Daily Value",
    ylabel="Categories")
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми вітаміну С?
df.groupby(by="Category")["Vitamin C (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='pie', 
    ylabel="",
    title="Vitamin C (% Daily Value) different menu categories")
plt.show()
df.groupby(by="Category")["Vitamin C (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='barh', 
    figsize=(10,5),
    title="Vitamin C (% Daily Value) different menu categories",
    xlabel="% Daily Value",
    ylabel="Categories")
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми Кальцію?
df.groupby(by="Category")["Calcium (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='pie', 
    ylabel="",
    title="Calcium (% Daily Value) different menu categories")
plt.show()
df.groupby(by="Category")["Calcium (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='barh', 
    figsize=(10,5),
    title="Calcium (% Daily Value) different menu categories",
    xlabel="% Daily Value",
    ylabel="Categories")
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми Заліза?
df.groupby(by="Category")["Iron (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='pie',
    ylabel="", 
    title="Iron (% Daily Value) different menu categories")
plt.show()
df.groupby(by="Category")["Iron (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(
    kind='barh', 
    figsize=(10,5),
    title="Iron (% Daily Value) different menu categories",
    xlabel="% Daily Value",
    ylabel="Categories")
plt.show()

#------------------------------------0-------------------------------------
# В якій їжі Макдональдсу найбільше цукру?
df.groupby("Category")["Sugars"].mean().head(5).plot(
    kind = "barh", 
    grid = True, 
    title="Which McDonald's food has the most sugar?",
    ylabel="Categories",
    xlabel="Grams\Serving")
plt.show()


#------------------------------------0-------------------------------------
# В якій категорії меню найбільше калорій
df[['Category', 'Calories']].groupby('Category').mean().head(10).plot(
    kind='barh', 
    figsize=(10,5),
    title="Which menu category has the most calories on average?",
    ylabel="Categories",
    xlabel="Calories")
plt.show()



#------------------------------------1-------------------------------------
# У скільки разів більше у меню McDonalds Вітаміну А ніж Вітаміну C
avaverage_vitama = df['Vitamin A (% Daily Value)'].mean()
avaverage_vitamc = df['Vitamin C (% Daily Value)'].mean()

# Обчислюємо наскільки більше в середньому міститься вітаміну А ніж вітаміну С
result = avaverage_vitama / avaverage_vitamc

# Округлюємо результат до двох знаків після коми
rounded_result = round(result, 2)

print('У:', rounded_result)



#----------------------------------2-----------------------------------------
# Яка частка калорій отриманих з жиру серед усіх калорій в їжі Макдональдсу
avaverage_calories = df['Calories'].mean()
avaverage_fat = df['Calories from Fat'].mean()

result = (avaverage_fat / avaverage_calories) * 100

rounded_result = round(result, 2)

print('Склад жиру:', rounded_result)



#------------------------------------3-------------------------------------
# Якої продукції в меню Макдональдс найбільше?
df["Category"].value_counts().plot(
    kind="barh", 
    title="What product is on the McDonald's menu the most?",
    ylabel="Categories", 
    xlabel="Number of items", 
    figsize=(12, 6))
plt.show()



#------------------------------------4-------------------------------------
# В якій їжі Макдональдсу найбільше протеїну?
df.groupby(by = "Category")["Protein"].mean().plot(
    kind = 'barh', 
    figsize = (15, 7), 
    grid = True,
    title="Which McDonald's food has the most protein?",
    ylabel="Categories", 
    xlabel="Grams\Serving")
plt.show()


#------------------------------------5-------------------------------------
# Чи існує взаємозв'язок між загальною к-тю калорій та к-тю калорій отриманих з жиру?
df.plot(
    x = 'Calories', 
    y = 'Calories from Fat', 
    kind = 'scatter', 
    figsize=(10, 4), 
    title="Is there a relationship between total calories and calories from fat?",
    xlabel="Calories", 
    ylabel="Calories from Fat")
plt.show()

#Бачимо, що зв'язок дуже сильний. Це може вказувати на те, що більшість калорій, які люди отримують з їжі Макдональдса отримуються саме з жирної їжі:(



# -----------------------6. іТоп-5 найбільш великі по вазі позиції в меню-----------------------
# Перезаписуємо у ствпичк Serving Size вагу страв у грамах
def extact_grams(text):
    if "g" in text:
        start = text.find("(") + 1
        end = text.find(' g')
        # Вирізаємо число між дужками
        grams = text[start:end]
        return float(grams)
    else:
        return 0

df["Serving Size"] = df["Serving Size"].apply(extact_grams)

# Сортування по стовбцю "Serving Size" за зростанням
df_sorted = df.sort_values(by='Serving Size', ascending=False)

# Вибираємо топ-5 страв
top_5 = df_sorted[['Item', 'Serving Size']].head()

# Побудова графіку
top_5.plot(x='Item', y='Serving Size', kind='barh', figsize=(10, 5), legend=False)

# Додаємо підписи та заголовок
plt.xlabel('Serving Size (g)')
plt.ylabel('Item')
plt.title('Top 5 Items by Serving Size in McDonald\'s Menu')
plt.tight_layout()
plt.show()



