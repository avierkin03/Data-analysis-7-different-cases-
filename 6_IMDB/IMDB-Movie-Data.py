import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB-Movie-Data.csv")

#видаляємо з датафрейма всі порожні значення
df.dropna(axis=0, inplace=True)

#функція, яка розділяє рядок з комами на список 
def split_genres(genres):
   return genres.split(',')

#переписуємо стовпичк 'Genre' - представляємо його елементи у вигляді списку
df['Genre'] = df['Genre'].apply(split_genres)
#створюємо новий стовпчик 'Number of genres' - тут показиватимуться к-ть жанрів для кожного фільма
df['Number of genres'] = df['Genre'].apply(len)



# 1. Рахуємо кількість фільмів для кожного режисера
films_per_director = df['Director'].value_counts()

# 2. Рахуємо середній рейтинг для кожного режисера
avg_rating_per_director = df.groupby('Director')['Rating'].mean()

# 3. Об'єднуємо дані в один датафрейм
director_stats = pd.DataFrame({
    'Number of Films': films_per_director,
    'Average Rating': avg_rating_per_director
})

# 4. Будуємо графік розсіювання
director_stats.plot(
    kind='scatter', 
    x='Number of Films', 
    y='Average Rating', 
    title='The relationship between the number of films a director has and the average rating', 
    xlabel='Number of Films', 
    ylabel='Average Rating', 
    grid=True, 
    figsize=(10, 6)
)

# Відображаємо графік
plt.show()

# Додатково: виведемо перші кілька рядків для перевірки
print(director_stats.head())

#----------------------------------------------------------1-------------------------------------------------------
#1. Фільмів з якою кількістю жанрів найбільше?
df["Number of genres"].value_counts().plot(
   kind ='pie',
   title="What are the most films with the most genres?",
   ylabel="")
plt.show()
#Висновок1: на діаграмі бачимо, що найбільша к-ть фільмів, які відносяться одночасно до 3-х жанрів


#----------------------------------------------------------2-------------------------------------------------------
#2. Чи залежить прибуток фільма від к-ті жанрів, до яких він відноситься?
#Показуємо середнє арифметичне прибутку для фільмів, які мають 1\2\3 жанри
df.groupby(by = "Number of genres")["Revenue (Millions)"].mean().plot(
   kind = "barh", 
   grid = True,
   title="Film revenue depending on the number of genres",
   ylabel="Number of genres",
   xlabel="Average revenue (Millions)")
plt.show()
#Висновок2: фільми, які мають більше жанрів приносять більше грошей



#----------------------------------------------------------3-------------------------------------------------------
#3. Чи залежить рейтинг фільма на сайті Metascore від к-ті жанрів, до яких він відноситься?
#Показуємо середнє арифметичне рейтингу на сайті Metascore для фільмів, які мають 1\2\3 жанри
df.groupby(by = "Number of genres")["Metascore"].mean().plot(
   kind = "barh", 
   grid = True,
   title="Film rating on Metascore depending on the number of genres",
   ylabel="Number of genres",
   xlabel="Average Metascore Rating")
plt.show()
#Висновок3: незалежно від к-ті жанрів(1\2\3), в середньому фільми мають приблизно однакову середню оцінку на сайті Metascore


#----------------------------------------------------------4-------------------------------------------------------
#4. У якому році люди в середньому найбільше залишали оцінок фільмам?
#лінійний графік
df.groupby(by = "Year")["Votes"].mean().plot(
   kind="line", 
   grid=True,
   title="In which year did people, on average, leave the most ratings for movies?",
   ylabel="Number of Votes",
   xlabel="Years")
plt.show()

#ступінчаста діаграма
df.groupby(by = "Year")["Votes"].mean().plot(
   kind="barh", 
   grid = True,
   title="In which year did people, on average, leave the most ratings for movies?",
   ylabel="Number of Votes",
   xlabel="Years")
plt.show()
#Висновок4: по графікам бачимо, що найбільша к-ть відгуків була дана за 2012 рік (трохи менше 300 000 відгуків)



#----------------------------------------------------------5-------------------------------------------------------
#5. У якому році був найвищий середній дохід з одного фільма?
print("Середній дохід по фільмам, в залежності від року його виходу:")
print(df.groupby("Year")["Revenue (Millions)"].mean())

df.groupby(by = "Year")["Revenue (Millions)"].mean().plot(
   kind="barh", 
   grid = True,
   title="Which year had the highest average revenue per film?",
   ylabel="Years",
   xlabel="Average Revenue (Millions)")
plt.show()
#Висновок5: по графіку бачимо, що найбільший середній дохід за 1 фільм був в 209 році (приблизно 115 000$)




#----------------------------------------------------------6-------------------------------------------------------
#6. Чи впливає рейтинг фільма на його прибуток?
df.plot(
   x = 'Rating', 
   y = 'Revenue (Millions)', 
   kind = 'scatter',
   title="Does a film's rating affect its profits?",
   ylabel="Revenue (Millions)",
   xlabel="Rating")
plt.show()
#Висновок6: на діаграмі розсіювання бачимо, що зв'язок не сильний, проте рисутній - фільми з кращим рейтингом мають трохи кращий прибуток




#----------------------------------------------------------7-------------------------------------------------------
#7. Як з роками змінювалася середня тривалість фільмів?
average_runtimes = df.groupby('Year')['Runtime (Minutes)'].mean()
print(average_runtimes)

df.groupby('Year')['Runtime (Minutes)'].mean().plot(
   kind="line", 
   x='Year', 
   y='Runtime (Minutes)', 
   title='Changing movie lengths over the years', 
   xlabel="Year", 
   ylabel="Average Runtime (Minutes))", 
   grid=True, 
   figsize=(10, 6))
plt.show()
#Висновок7: (на графіку все видно)



#----------------------------------------------------------8-------------------------------------------------------
#8. Який середній рейтинг фільмів у кожного режисера?
print("Середній рейтинг фільмів у кожного режисера:")
print(df.groupby(by = "Director")["Rating"].mean().sort_values(ascending=False).head(10))



#----------------------------------------------------------9-------------------------------------------------------
#8. На скільки відмінні Rating фільмів порівняно з Metascore
# Групуємо дані за кількістю жанрів і рахуємо середнє значення
avg_ratings = df.groupby('Number of genres')['Rating'].mean()
avg_metascores = df.groupby('Number of genres')['Metascore'].mean()

# Створюємо фігури та осі для двох стовпчастих діаграм
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Перша діаграма — середній рейтинг
axes[0].bar(avg_ratings.index, avg_ratings.values, color='blue', alpha=0.7)
axes[0].set_title('Average rating (Rating)')
axes[0].set_xlabel('Number of genres')
axes[0].set_ylabel('Average Rating')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)

# Друга діаграма — середній Metascore
axes[1].bar(avg_metascores.index, avg_metascores.values, color='red', alpha=0.7)
axes[1].set_title('Average rating (Metascore)')
axes[1].set_xlabel('Number of genres')
axes[1].set_ylabel('Average Metascore rating')
axes[1].grid(axis='y', linestyle='--', alpha=0.5)

# Відображаємо графіки
plt.tight_layout()
plt.show()