import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("countries of the world.csv")

print(df.info())

# перетворюємо тип даних в стовпчиках "Literacy (%)", "Phones (per 1000)", "Birthrate", "Deathrate" на float
def clean_comas(word):
        word = str(word)
        number = word.replace(",", ".")
        return float(number)

df["Literacy (%)"] = df["Literacy (%)"].apply(clean_comas)
df["Phones (per 1000)"] = df["Phones (per 1000)"].apply(clean_comas)
df["Birthrate"] = df["Birthrate"].apply(clean_comas)
df["Deathrate"] = df["Deathrate"].apply(clean_comas)



#----------------------------- 1. Найрозповсюдніша к-ть населення країн (до 200 000 000) -----------------------------
df[df['Population']<200000000]["Population"].plot(
      kind="hist", 
      grid=True,
      title="The most common population of countries",
      xlabel="Range (population)",
      ylabel="Frequency")
plt.show()



#----------------------------- 2. ВВП різних регіонів -----------------------------
# Групування даних і підрахунок середнього ВВП для кожного регіону
grouped_data = df.groupby("Region")["GDP ($ per capita)"].mean()

grouped_data.plot(
    kind="barh",
    title="GDP ($ per capita) of different regions", 
    xlabel="GDP ($ per capita)",
    ylabel="Region",
    grid=True, 
    figsize=(8,4))

plt.tight_layout()  # Автоматично підганяє елементи графіка для уникнення накладань
plt.show()

# Висновок: Північна Америка має надзвичайно велике відхилення головним чином через присутність США, які самотужки змінюють 
# середнє значення. Здається, регіони на південь від Сахари мають справді низький ВВП, 
# що не дивно, враховуючи, наскільки малий імпорт та експорт.



#----------------------------- 3. Зв'язок ВВП регіону та к-ті телефонів на 1000 населення -----------------------------
df.plot(
      x = 'GDP ($ per capita)', 
      y = 'Phones (per 1000)', 
      kind = 'scatter', 
      title="Dependence of GDP and number of phones", 
      xlabel="GDP ($ per capita)",
      ylabel="Phones (per 1000)",
      grid=True)
plt.show()

# Висновок: Дивлячись на кількість телефонів на 1000 осіб, ми помічаємо, що вона збільшується з регіонами в міру зростання ВВП. Оскільки 
# в країні з високим ВВП все більше і більше людей мають більший статок, вони, як правило, мають більше пристроїв.

# Звернімо увагу на викид, у якому кількість телефонів перевищує кількість телефонів для окремих людей! Подивимося, яка це країна
print(df[df['Phones (per 1000)']>1000])

# Висновок: Mонако! Не дивно, враховуючи, наскільки крихітною є нація та надзвичайно багато багатих людей там проживає




#----------------------------- 4. Зв'язок ВВП регіону та рівня гграмотності -----------------------------
df.plot(
      x = 'GDP ($ per capita)', 
      y = 'Literacy (%)', 
      kind = 'scatter', 
      title="Relationship between GDP and literacy rate",
      grid=True, 
      xlabel="GDP ($ per capita)", 
      ylabel="Literacy (%)")
plt.show()

# # Висновок: рівень рамотності вище в країнах з вищим ВВП. Це пов’язано з тим, що зростання ВВП є характерним для великих галузей і 
# розвинених країн, які вимагають високого рівня грамотності для спілкування.



#----------------------------- 5. Зв'язок ВВП регіону та рівня народжуваності -----------------------------
df.plot(
      x = 'GDP ($ per capita)', 
      y = 'Birthrate', 
      kind = 'scatter', 
      title="The relationship between GDP and birthrate rate", 
      grid=True, 
      xlabel="GDP ($ per capita)", 
      ylabel="Birthrate")
plt.show()




#----------------------------- 6. Зв'язок ВВП регіону та рівня смертності -----------------------------
df.plot(
      x = 'GDP ($ per capita)', 
      y = 'Deathrate', 
      kind = 'scatter', 
      title="Relationship between GDP and deathrate", 
      grid=True, 
      xlabel="GDP ($ per capita)", 
      ylabel="Deathrate")
plt.show()



# ----------------------------- 7 Найбільший показник ВВП кожного регіону ----------------------------------------------------------
df.groupby("Region")["GDP ($ per capita)"].max().plot(
      kind = "barh", 
      grid=True, 
      xlabel="GDP ($ per capita)", 
      ylabel="Region",
      title="The highest GDP indicator of each region")
plt.tight_layout()
plt.show()


# ----------------------------- 8 Країни з найвищим ВВП у кожному регіоні -----------------------------
# знаходимо країни з найвищим ВВП в кожному регіоні
top_gdp_countries = df.loc[df.groupby("Region")["GDP ($ per capita)"].idxmax()]

# Підготовка даних для графіку
regions = top_gdp_countries["Region"]
gdp_values = top_gdp_countries["GDP ($ per capita)"]
countries = top_gdp_countries["Country"]

# Створюємо графік (напряму беремо з модуля pyplot метод barh для побудови стовпчиків діаграми)
plt.figure(figsize=(8, 6))
bars = plt.barh(regions, gdp_values, color="skyblue")

# Додаємо назви країн на графік
# функція zip об'єднує два списки (bars і countries) у послідовність пар
for bar, country in zip(bars, countries):
    plt.text(
        bar.get_width() + 500,  # Додаємо зміщення праворуч
        bar.get_y() + bar.get_height() / 2,  # Вирівнюємо текст по центру стовпця
        country,
        va="center"
    )

plt.title("Countries with the highest GDP in each region")
plt.xlabel("GDP ($ per capita)")
plt.ylabel("Region")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()