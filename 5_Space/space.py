import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Space_Corrected.csv')

df = df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1)

print(df.info())

# ---------------------1. К-ть запусків кожної компанії---------------------
df.groupby("Company Name").size().sort_values(ascending=False).head(10).plot(
    kind='barh', 
    figsize=(10,5), 
    grid=True,
    title="Number of launches by each company",
    xlabel="Number of launches",
    ylabel="Company Name")
plt.show()


# ---------------------2. Статус Ракет---------------------
df["Status Rocket"].value_counts().plot(
    kind='pie', 
    title = "Rocket Status")
plt.show()



# ---------------------3. Статус Місій---------------------
df["Status Mission"].value_counts().plot(
    kind='barh', 
    figsize=(10,5), 
    title = "Mission Status", 
    xlabel="Number of missions",
    ylabel="Status",
    grid=True)
plt.show()



# ---------------------4. К-ть місій кожен рік---------------------
def data_split(data):
    # Розбиваємо рядок на частини
    parts = data.split()
    # Рік знаходиться на 4-й позиції (індекс 3)
    return int(parts[3])

df["Year"] = df["Datum"].apply(data_split)

df["Year"].value_counts().plot(
    kind='bar', 
    figsize=(20,7), 
    title = "Missions per Year", 
    grid=True)
plt.show()

df["Year"].value_counts().sort_index().plot(
    kind='line', 
    figsize=(20,7), 
    title = "Missions per Year", grid=True)
plt.show()



# 5. ---------------------Лінійні графіки к-ті косм. запусків компаній кожен рік---------------------
import seaborn as sns

# Витягуємо рік запуску з дати та додаємо стовпчик 'Count' зі значенням 1 для подальшого підрахунку запусків
df['Year']=df['Datum'].str.split(' ',expand=True)[3]  # Розбиваємо рядок дати 'Datum' на частини та беремо 4-й елемент як рік
df['Count']=1  # Додаємо стовпчик 'Count' для подальшого підрахунку кількості запусків за рік

# Створюємо окремі датафрейми для кожної компанії, щоб їх запуски можна було відобразити на окремих графіках
df_nasa=df[df['Company Name']=='NASA']
df_isro=df[df['Company Name']=='ISRO']
df_casc=df[df['Company Name']=='CASC']
df_spaceX=df[df['Company Name']=='SpaceX']

# Створюємо фігуру для розміщення всіх графіків та задаємо розміри фігури
fig1=plt.figure(figsize=(20,15))

# Задаємо заголовок для всієї фігури
fig1.suptitle("Selected state-owned companies and their launch years", fontsize=18)

# Перший підграфік для запусків NASA
ax1=fig1.add_subplot(221)                   # Додаємо підграфік у сітці 2x2 на першій позиції
sns.lineplot(x="Year", y="Count", data=df_nasa.groupby('Year')['Count'].sum().reset_index(), ax=ax1,color='maroon')
ax1.set_title('NASA Launch Years',size=10)  # Заголовок підграфіка
ax1.tick_params(axis='x', rotation=90)      # Повертаємо підписи по осі X вертикально для кращої читабельності

# Другий підграфік для запусків SpaceX
ax2=fig1.add_subplot(222)                   # Додаємо підграфік у сітці 2x2 на другій позиції
sns.lineplot(x="Year", y="Count", data=df_spaceX.groupby('Year')['Count'].sum().reset_index(), ax=ax2,color='darkolivegreen')
ax2.set_title('SpaceX Launch Years',size=10)
ax2.tick_params(axis='x', rotation=90)  

# Третій підграфік для запусків CASC
ax3=fig1.add_subplot(223)                   # Додаємо підграфік у сітці 2x2 на третій позиції
sns.lineplot(x="Year", y="Count", data=df_casc.groupby('Year')['Count'].sum().reset_index(), ax=ax3,color='darkslategrey')
ax3.set_title('CASC Launch Years',size=10)
ax3.tick_params(axis='x', rotation=90)  

# Четвертий підграфік для запусків ISRO
ax4=fig1.add_subplot(224)                   # Додаємо підграфік у сітці 2x2 на четвертій позиції
sns.lineplot(x="Year", y="Count", data=df_isro.groupby('Year')['Count'].sum().reset_index(), ax=ax4,color='navy')
ax4.set_title('ISRO Launch Years',size=10)
ax4.tick_params(axis='x', rotation=90)  

# Налаштовуємо відстань між підграфіками для кращої читабельності
plt.subplots_adjust(wspace=0.3, hspace=0.35)  
plt.show()

#splitting the datum column for relevant info
# df['Month']=df['Datum'].str.split(' ', expand=True)[1]
# df['Year']=df['Datum'].str.split(' ',expand=True)[3]


# ---------------------6. К-ть запусків по країнам---------------------
# Створюємо словник для приведення деяких значень місць запусків до відповідних країн
# У словнику 'countries_dict' ключі представляють назви, які можуть з'явитися в стовпчику "Location" як останні елементи, 
# а значення — це назви країн, до яких належать ці місця запусків
countries_dict = {
    'Russia' : 'Russian Federation',
    'New Mexico' : 'USA',
    "Yellow Sea": 'China',
    "Shahrud Missile Test Site": "Iran",
    "Pacific Missile Range Facility": 'USA',
    "Barents Sea": 'Russian Federation',
    "Gran Canaria": 'USA'
}

# Витягуємо країну з колонки "Location", яка містить місце запуску (місто, регіон, країна)
# Спочатку розбиваємо рядки у колонці "Location" за комами і пробілами (", "), обираємо останній елемент як країну
# Далі застосовуємо заміну відповідно до словника countries_dict, щоб привести значення до єдиного формату
df['Country'] = df["Location"].str.split(", ").str[-1].replace(countries_dict)

# Підраховуємо кількість запусків по кожній країні, обираємо перші 10 країн з найбільшою кількістю запусків
# Створюємо горизонтальну стовпчикову діаграму з кількістю запусків по кожній країні
df['Country'].value_counts().head(10).plot(kind="barh", xlabel="Count", ylabel="Country", title="Total launches by each Country", grid=True)
plt.show()



# ---------------------7. статуси місій в різних країнах---------------------
from plotly.subplots import make_subplots           # Імпортуємо функцію для створення багаторядкових графіків
import plotly.graph_objects as go                   # Імпортуємо модуль для створення графічних об'єктів Plotly
from sklearn.preprocessing import LabelEncoder      # Імпортуємо LabelEncoder для кодування категоріальних даних

# Створюємо об'єкт кодувальника для перетворення текстових значень у числові коди
encoder = LabelEncoder()
# Навчаємо кодувальник на колонці "Status Mission", щоб отримати числові значення для кожного статусу місії
encoder.fit(df["Status Mission"])

# Визначаємо кольори для кожного числового коду статусу місії (0 - "red", 1 - "Orange", 2 - "Yellow", 3 - "Green")
colors = {0: "red",             
          1 : "Orange",         
          2 : "Yellow", 
          3 : "Green"}

# Створюємо багаторядковий графік, з чотирма рядками і чотирма стовпцями
# Підписи на графіку будуть унікальні назви країн зі стовпця "Country" у нашому DataFrame
fig = make_subplots(rows = 4, cols = 4, subplot_titles = df["Country"].unique())

# Запускаємо цикл по кожній унікальній країні у стовпчику "Country" (для побудови окремого графіка для кожної країни)
for i, country in enumerate(df["Country"].unique()):
    # Вираховуємо відсоткове відношення кількості кожного статусу місії для поточної країни
    counts = df[df["Country"] == country]["Status Mission"].value_counts(normalize = True)*100
    # Визначаємо кольори для кожного статусу місії у поточній країні на основі закодованих значень статусів
    color = [colors[x] for x in encoder.transform(counts.index)]
    # Створюємо стовпчиковий графік (trace) для поточної країни
    trace = go.Bar(
        x=counts.index,              # По осі X — унікальні значення статусів місій
        y=counts.values,             # По осі Y — відсоткові значення статусів місій
        name=country,                # Назва графіка — назва поточної країни
        marker={"color": color},     # Вказуємо кольори для стовпчиків відповідно до статусу місії
        showlegend=False             # Вимикаємо легенду для кожного графіка, щоб не дублювати інформацію
    )
    # Додаємо створений графік (trace) у відповідне місце багаторядкового графіка
    fig.add_trace(trace, row = (i//4) + 1, col = (i%4)+1)

# Налаштовуємо заголовок усього графіка, а також розміри графіка (висота - 1000, ширина - 1100)
fig.update_layout(title = {"text":"Countries and Mission Status"}, height = 1000, width = 1100)

# Додаємо назву осі Y ("Percentage") для кожного рядка в багаторядковому графіку
for i in range(1,5):
    fig.update_yaxes(title_text = "Percentage", row = i, col = 1)
    
# Відображаємо графік
fig.show()