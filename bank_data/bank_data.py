#!/usr/bin/env python
# coding: utf-8

# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
# Наталия, привет!
# 
# Меня зовут Олег Михеев, и я буду проверять твой проект. Предлагаю общаться на "ты", но если тебе будет некомфортно, обязательно сообщи, и мы перейдем на "вы". Моя главная цель - не указать на твои ошибки, а поделиться опытом и подготовить тебя к работе аналитиком. Увидев у тебя ошибку, я постараюсь указать на её наличие и дам возможность найти и самостоятельно исправить её.
# 
# В проверке проекта я буду использовать разные цвета для обозначения комментариев. Например:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h3> Комментарий ревьюера ✔️<a class="tocSkip"> </h3>
# 
# Так выделены удачные решения, на которые можно опираться в будущем.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h3> Комментарий ревьюера ⚠️<a class="tocSkip"> </h3>
# 
# Когда решение на отдельном шаге станет лучше, если внести небольшие коррективы.
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h3> Комментарий ревьюера ❌<a class="tocSkip"></h3>
# 
#  А так выделены решения, которые необходимо доработать, чтобы я мог принять проект.
# </div>
#     
#   
# Если вносишь изменения в проект, указывай, пожалуйста, это в своих комментариях. Будет удобно, если обозначишь их заметным цветом. Например, вот так:
#        
# <div class="alert alert-block alert-info">
#     
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# Можешь кликнуть сюда два раза и скопировать код комментария. Также если что-то непонятно или остались вопросы по ревью, обязательно пиши.
#     
# </div>
#     
# Пожалуйста, не удаляй и не перемещай мои комментарии, чтобы не произошло путаницы, и я мог быстрее проверить проект.
# <br/>

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# **Общий вывод по ревью**
# 
# Хорошая работа. Ты умело пользуешься кодом для решения поставленных задач.
#     
# А твои выводы понятны и отражают результаты расчетов.
# 
# **Что нужно сделать, чтобы я мог принять проект**:
# 
# * Написать подробный финальный вывод, учитывающий все группы клиентов с процентными показателями и информацию о предобработке
# 
# **Успехов! Жду проект на повторное ревью!**

# <div class="alert alert-block alert-info">
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# Привет! Спасибо за ревью. Пардон, что поздно исправляю, отпуск и поздно заметила, что работа проверена. Надеюсь, успею всё нагнать :( 
#     
# </div>

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# **Общий вывод по ревью v2**
# 
# Cпасибо, что учла все рекомендации и замечания.
# 
# Очень качественно выполненный проект! Мне было приятно с тобой работать 🤝
# 
# Видно, что ты последовательна и вдумчива в своих выводах.
#     
# А проект написан аккуратно, поэтому его легко воспринимать.
# 
# Продолжай в том же духе и станешь крутым специалистом.
# 
# **Успехов в дальнейшем обучении!**

# # Исследование надежности заемщиков
# 

# Во второй части проекта вы выполните шаги 3 и 4. Их вручную проверит ревьюер.
# Чтобы вам не пришлось писать код заново для шагов 1 и 2, мы добавили авторские решения в ячейки с кодом. 
# 
# 

# ## Откройте таблицу и изучите общую информацию о данных

# **Задание 1. Импортируйте библиотеку pandas. Считайте данные из csv-файла в датафрейм и сохраните в переменную `data`. Путь к файлу:**
# 
# `/datasets/data.csv`

# In[1]:


import pandas as pd

try:
    data = pd.read_csv('/datasets/data.csv')
except:
    data = pd.read_csv('https://code.s3.yandex.net/datasets/data.csv')


# **Задание 2. Выведите первые 20 строчек датафрейма `data` на экран.**

# In[2]:


data.head(20)


# **Задание 3. Выведите основную информацию о датафрейме с помощью метода `info()`.**

# In[3]:


data.info()


# ## Предобработка данных

# ### Удаление пропусков

# **Задание 4. Выведите количество пропущенных значений для каждого столбца. Используйте комбинацию двух методов.**

# In[4]:


data.isna().sum()


# **Задание 5. В двух столбцах есть пропущенные значения. Один из них — `days_employed`. Пропуски в этом столбце вы обработаете на следующем этапе. Другой столбец с пропущенными значениями — `total_income` — хранит данные о доходах. На сумму дохода сильнее всего влияет тип занятости, поэтому заполнить пропуски в этом столбце нужно медианным значением по каждому типу из столбца `income_type`. Например, у человека с типом занятости `сотрудник` пропуск в столбце `total_income` должен быть заполнен медианным доходом среди всех записей с тем же типом.**

# In[5]:


for t in data['income_type'].unique():
    data.loc[(data['income_type'] == t) & (data['total_income'].isna()), 'total_income'] =     data.loc[(data['income_type'] == t), 'total_income'].median()


# ### Обработка аномальных значений

# **Задание 6. В данных могут встречаться артефакты (аномалии) — значения, которые не отражают действительность и появились по какой-то ошибке. таким артефактом будет отрицательное количество дней трудового стажа в столбце `days_employed`. Для реальных данных это нормально. Обработайте значения в этом столбце: замените все отрицательные значения положительными с помощью метода `abs()`.**

# In[6]:


data['days_employed'] = data['days_employed'].abs()


# **Задание 7. Для каждого типа занятости выведите медианное значение трудового стажа `days_employed` в днях.**

# In[7]:


data.groupby('income_type')['days_employed'].agg('median')


# У двух типов (безработные и пенсионеры) получатся аномально большие значения. Исправить такие значения сложно, поэтому оставьте их как есть.

# **Задание 8. Выведите перечень уникальных значений столбца `children`.**

# In[8]:


data['children'].unique()


# **Задание 9. В столбце `children` есть два аномальных значения. Удалите строки, в которых встречаются такие аномальные значения из датафрейма `data`.**

# In[9]:


data = data[(data['children'] != -1) & (data['children'] != 20)]


# **Задание 10. Ещё раз выведите перечень уникальных значений столбца `children`, чтобы убедиться, что артефакты удалены.**

# In[10]:


data['children'].unique()


# ### Удаление пропусков (продолжение)

# **Задание 11. Заполните пропуски в столбце `days_employed` медианными значениями по каждого типа занятости `income_type`.**

# In[11]:


for t in data['income_type'].unique():
    data.loc[(data['income_type'] == t) & (data['days_employed'].isna()), 'days_employed'] =     data.loc[(data['income_type'] == t), 'days_employed'].median()


# **Задание 12. Убедитесь, что все пропуски заполнены. Проверьте себя и ещё раз выведите количество пропущенных значений для каждого столбца с помощью двух методов.**

# In[12]:


data.isna().sum()


# ### Изменение типов данных

# **Задание 13. Замените вещественный тип данных в столбце `total_income` на целочисленный с помощью метода `astype()`.**

# In[13]:


data['total_income'] = data['total_income'].astype(int)


# ### Обработка дубликатов

# **Задание 14. Обработайте неявные дубликаты в столбце `education`. В этом столбце есть одни и те же значения, но записанные по-разному: с использованием заглавных и строчных букв. Приведите их к нижнему регистру.**

# In[14]:


data['education'] = data['education'].str.lower()


# **Задание 15. Выведите на экран количество строк-дубликатов в данных. Если такие строки присутствуют, удалите их.**

# In[15]:


data.duplicated().sum()


# In[16]:


data = data.drop_duplicates()


# ### Категоризация данных

# **Задание 16. На основании диапазонов, указанных ниже, создайте в датафрейме `data` столбец `total_income_category` с категориями:**
# 
# - 0–30000 — `'E'`;
# - 30001–50000 — `'D'`;
# - 50001–200000 — `'C'`;
# - 200001–1000000 — `'B'`;
# - 1000001 и выше — `'A'`.
# 
# 
# **Например, кредитополучателю с доходом 25000 нужно назначить категорию `'E'`, а клиенту, получающему 235000, — `'B'`. Используйте собственную функцию с именем `categorize_income()` и метод `apply()`.**

# In[17]:


def categorize_income(income):
    try:
        if 0 <= income <= 30000:
            return 'E'
        elif 30001 <= income <= 50000:
            return 'D'
        elif 50001 <= income <= 200000:
            return 'C'
        elif 200001 <= income <= 1000000:
            return 'B'
        elif income >= 1000001:
            return 'A'
    except:
        pass


# In[18]:


data['total_income_category'] = data['total_income'].apply(categorize_income)


# **Задание 17. Выведите на экран перечень уникальных целей взятия кредита из столбца `purpose`.**

# In[19]:


data['purpose'].unique()


# **Задание 18. Создайте функцию, которая на основании данных из столбца `purpose` сформирует новый столбец `purpose_category`, в который войдут следующие категории:**
# 
# - `'операции с автомобилем'`,
# - `'операции с недвижимостью'`,
# - `'проведение свадьбы'`,
# - `'получение образования'`.
# 
# **Например, если в столбце `purpose` находится подстрока `'на покупку автомобиля'`, то в столбце `purpose_category` должна появиться строка `'операции с автомобилем'`.**
# 
# **Используйте собственную функцию с именем `categorize_purpose()` и метод `apply()`. Изучите данные в столбце `purpose` и определите, какие подстроки помогут вам правильно определить категорию.**

# In[20]:


def categorize_purpose(row):
    try:
        if 'автом' in row:
            return 'операции с автомобилем'
        elif 'жил' in row or 'недвиж' in row:
            return 'операции с недвижимостью'
        elif 'свад' in row:
            return 'проведение свадьбы'
        elif 'образов' in row:
            return 'получение образования'
    except:
        return 'нет категории'


# In[21]:


data['purpose_category'] = data['purpose'].apply(categorize_purpose)


# ### Шаг 3. Исследуйте данные и ответьте на вопросы

# #### 3.1 Есть ли зависимость между количеством детей и возвратом кредита в срок?

# Создаём отдельную таблицу с информацией о детях и долгах, выводим её на экран со следующими столбцами: 
# * children: количество детей
# * count: количество задолженностей для данной категории 
# * sum: количество строк в данной категории
# 
# sum выводим для понимания, как много строк в каждой категории, чтобы видеть, репрезентативная ли выборка 

# In[22]:


data_pivot = data.pivot_table(index=['children'], values='debt', aggfunc=('sum', 'count'))
print(data_pivot)


# Переименуем столбцы таблицы, чтобы названия были более понятны интуитивно

# In[23]:


data_pivot = data_pivot.rename(columns={'sum':'debt_sum','count':'number_of_lines'})
print(data_pivot)


# Добавим новый столбец, в котором посчитаем процент "должников" по категориям как отношение количества "должников" к количеству строк (по сути - количеству заёмщиков в данной категории) 

#  <div class="alert alert-success">
# <h3> Комментарий ревьюера ✔️<a class="tocSkip"> </h3>
# 
#  Здорово, что переименовываешь столбцы. Это делает проект более простым для восприятия.
# </div>

# In[24]:


data_pivot['percent'] = round(data_pivot['debt_sum']/data_pivot['number_of_lines'], 4) * 100
print(data_pivot.sort_values(by = 'percent'))


# Видим, что записей о семьях с 5 детьми всего 9, их можно изучить на возможные неявные дубликаты, чтобы понять, репрезентативна ли выборка 

# In[25]:


print(data[data['children'] == 5])


# Неявных дубликатов в данных о семьях с 5 детьми не выявлено. 

# **Вывод:** 
# Семьи, в которых нет детей, возвращают кредиты в срок немного чаще остальных - это можно объяснить тем, что в семьях без детей ниже финансовая нагрузка. 
# 
# Семьи, в которых 1-2 ребёнка, имеют практически одинаковые показатели. 
# 
# В целом корелляция есть, но её сложно назвать сильной. 

# <div class="alert alert-warning">
#     <h3> Комментарий ревьюера ⚠️<a class="tocSkip"> </h3>
# 
# Вывод верный, но группы действительно несбалансированны по объёму. Поэтому стоило бы учитывать только клиентов с 0-2 детьми, потому что остальные группы составляют не более 2 % от всей выборки, что крайне мало для объективных выводов.
# </div>

# <div class="alert alert-block alert-info">
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# Принято, учла это в общем выводе   
# </div>

#  <div class="alert alert-success">
# <h3> Комментарий ревьюера v2 ✔️<a class="tocSkip"> </h3>
# 
#  Супер, вывод стал точнее!
# </div>

# #### 3.2 Есть ли зависимость между семейным положением и возвратом кредита в срок?

# Снова создадим отдельную таблицу для анализа информации, выделим семейное положение, количество строк и количество "должников" 

# In[26]:


data_pivot = data.pivot_table(index=['family_status'], values='debt', aggfunc=('sum', 'count'))
print(data_pivot)


# Перемменуем столбцы для удобства, создадим новый столбец percent для вывода процента "должников" в разрезе по семейному статусу, округлив значение до 2 знаков после запятой и выведем данные в порядке возрастания процента
# 

# In[27]:


data_pivot = data_pivot.rename(columns={'sum':'debt_sum','count':'number_of_lines'})
data_pivot['percent'] = round(data_pivot['debt_sum']/data_pivot['number_of_lines'], 4) * 100
print(data_pivot.sort_values(by = 'percent'))


# **Вывод:** 
# Здесь прослеживается, что чаще всего не возвращают кредиты в срок те, кто ещё ни разу не вступал в брак. Это может быть вызвано молодым возрастом, небольшим доходом. 
# 
# Самые "надёжные" заёмщики - те, кто уже вступал в брак, можно предположить, что это вызвано высоким уровнем ответственности, более зрелым возрастом. 
# 
# В целом, зависимость прослеживается. 

#  <div class="alert alert-success">
# <h3> Комментарий ревьюера ✔️<a class="tocSkip"> </h3>
# 
#  Верно, люди, когда-либо состоявшие в браке, в среднем, лучше возвращают кредиты.
# </div>

# #### 3.3 Есть ли зависимость между уровнем дохода и возвратом кредита в срок?

# Для расчёта этой информации поможет стоблец total_income_category, который создавался в задании 16, категории такие: 
#     
# - 0–30000 — 'E';
# - 30001–50000 — 'D';
# - 50001–200000 — 'C';
# - 200001–1000000 — 'B';
# - 1000001 и выше — 'A'.
# Снова создадим таблицу для анализа информации по количеству строк, количеству "должников" и уровню дохода и сразу переименуем столбцы. 

# In[44]:


data_pivot = data.pivot_table(index = [ 'total_income_category'], values = 'debt', aggfunc = {'count','sum'})
data_pivot = data_pivot.rename(columns={'count':'number_of_lines','sum':'debt_sum'})


# Добавим столбец percent, округлив его значение до 2 знаков после запятой, и выведем полученные данные, отсортировав по возрастанию процента 
# 

# In[45]:


data_pivot['percent'] = round(data_pivot['debt_sum']/data_pivot['number_of_lines'], 4) * 100
print(data_pivot.sort_values(by = 'percent'))


# **Вывод:**
# Люди с самым низким уровнем дохода имеют наиболее высокую вероятность не вернуть кредит в срок, это ожидаемо и в целом объясняется уровнем дохода. 
# Самые "надёжные" заёмщики - это люди с доходом от 30 до 50 тысяч, возможно, это можно объяснить тем, что суммы штрафов по просрочкам могут значительно подорвать бюджет, и копить просрочки очень невыгодно. 
# Также относительно надёжными заёмщиками являются люди с высоким уровнем дохода, от 200 тысяч, можно предположить, что это связано с высоким уровнем ответственности. 
# Довольно высок процент "должников" среди заёмщиков со средним уровнем дохода - возможно, это семейные люди с большим уровнем трат и несколькими кредитами. 
# Можно также отметить, что процент должников среди людей с самым высоким уровнем дохода довольно высок. 
# 
# В целом, корреляция есть. 

# <div class="alert alert-warning">
#     <h3> Комментарий ревьюера ⚠️<a class="tocSkip"> </h3>
# 
# Всё так, но обрати внимание, в этой таблице группы крайне несбалансированы. Поэтому стоит учитывать только две самые многочисленные - B и С, так как они включают примерно 98 процентов данных от общей выборки
# 
# Альтернативно, можно решить это задание через разделение выборки на равные по объёму части. Для этого подойдёт функция pd.qcut().
# 
# Даю ссылку:
#     
# * https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html
# 
# Метод qcut() делит числовой столбец на равные по объёму части на основании квантилей. Квантили — это статистические показатели, которые разделяют набор данных на равные части. Квантили включают квартили (25%, 50% и 75%), децили (каждые 10%) и процентили (каждые 1%). Приведу пример разделения на 3 равных отрезка, находящихся на отметках 33,3% и 66,7%.
#         
#     pd.qcut(data['column'], q=3, labels=['one', 'two', 'three'])
#         
# Можно не указывать названия отрезков с помощью labels. Тогда названия отрезкам присвоятся в численном виде.
# </div>

# <div class="alert alert-block alert-info">
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# Принято, учла это в общем выводе. В целом хотелось рассмотреть большее количество групп, потому что возможно, 2 группы сравнивать несерьёзно :) Но какие данные имеем, с теми и работаем 
# </div>

#  <div class="alert alert-success">
# <h3> Комментарий ревьюера v2 ✔️<a class="tocSkip"> </h3>
# 
#  Да, иногда приходится работать хоть с какими-то данными. 
# </div>

# #### 3.4 Как разные цели кредита влияют на его возврат в срок?

# In[46]:


data_pivot = data.pivot_table(index = ['purpose_category'], values = 'debt', aggfunc = {'count','sum'})
data_pivot = data_pivot.rename(columns={'count':'number_of_lines','sum':'debt_sum'})
data_pivot['percent'] = round(data_pivot['debt_sum']/data_pivot['number_of_lines'], 4) * 100
print(data_pivot.sort_values(by = 'percent'))


# **Вывод:** 
# Создав отдельную таблицу и посчитав процент "должников" по каждой категории, можно сделать следующие выводы: 
# 
# корреляция точно наблюдается. Примечательно, что наиболее "дорогая" категория - операции с недвижимостью - наиболее надёжна для банка, процент возвратов в срок по ней максимален. 
# Кредиты на менее "дорогие" цели же наименее надёжны, здесь пользователи допускают просрочку. Это может быть вызвано меньшей суммой кредита и в целом суммой средств, которые участвуют в сделке, для которой брался кредит. 
# 
# Премечательно также большое количество кредитов на свадьбу, можно предположить, что часть кредита возвращается непосредственно после свадьбы, когда молодожёны получили подарки. 

# <div class="alert alert-success">
# <h3> Комментарий ревьюера ✔️<a class="tocSkip"> </h3>
# 
# Вывод верный. Здорово, что стараешься описывать причины, которые могли привести к полученной картине. Для аналитика важно видеть смысл, который стоит за данными.
# </div>

# #### 3.5 Приведите возможные причины появления пропусков в исходных данных.

# *Ответ:* 
# В исходных данных были пропущены столбцы 
# 
# days_employed и total_income, при этом количество пропусков в этих столбцах одинаково. 
# Можно предположить, что при заполнении данных эти столбцы были необязательны. Пользователи могут не желать указывать общий доход, и если поле не обязательно, его оставляют пустым. 
# Что касается поля days_employed, можно предположить, что его заполнение зависит от заполнения поля total_income (заполнил общий доход - укажи стаж), и пользователи, не указавшие общий доход, не заполняли и стаж.  

# <div class="alert alert-warning">
#     <h3> Комментарий ревьюера ⚠️<a class="tocSkip"> </h3>
# 
# Верный пример, намеренное или ненамеренное сокрытие информации - это человеческий фактор. А какую ещё причину пропусков, не связанную напрямую с человеком, ты можешь назвать?
# </div>

# <div class="alert alert-block alert-info">
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# Баг, добавление вышеописанных полей в более свежей версии ПО, несоответствие версий фронта и бэка (пользователь вводит данные, но бэк не умеет их сохранять, потому что некуда, БД не доработана под новую версию) :) 
#     
# </div>

#  <div class="alert alert-success">
# <h3> Комментарий ревьюера v2 ✔️<a class="tocSkip"> </h3>
# 
#  Абсолютно верно. Вторая большая причина пропусков - это технические проблемы.
# </div>

# #### 3.6 Объясните, почему заполнить пропуски медианным значением — лучшее решение для количественных переменных.

# *Ответ:* 
# В целом при работе с количественными данными у нас есть два варианта - выбрать медиану и среднее арифметическое. Но среднее арифметическое может некорректно отобразить ситуацию, поскольку в данных могут быть большие разбросы. Медиана же как раз подходит для случаев, когда в данных может быть разброс (сверх-высокий доход и сверх-низкий), поэтому проставление медианного значения вместо пропусков - наилучшее решение. 

# <div class="alert alert-success">
# <h3> Комментарий ревьюера ✔️<a class="tocSkip"> </h3>
# 
# Абсолютно верно, такие сильно выделяющиеся значения ещё называют выбросами.
# </div>

# ### Шаг 4: общий вывод.

# В целом по выдвинутым гипотезам корреляция прослеживается, но её сложно назвать очень высокой. 
# Можем попробовать составить портрет надёжного и ненадёжного заёмщика. Относительно надёжный заёмщик не будет состоять в браке, но при этом будет иметь опыт брака, у него будет высокий доход и не будет детей. Целью кредита будет операция с недвижимостью. 
# Относительно ненадёжный заёмщик может иметь 4 детей, будет не женат или состоять в гражданском браке, будет иметь низкий доход. Целью кредита будет покупка автомобиля или получение образования. 
# При этом не обязательно эти факторы должны совпасть и не обязательно эти факторы предскажут нам поведение заёмщика, поэтому делать вывод о возможности выдачи кредита пользователю по таким параметрам не стоит, для этого существуют гораздо более подробные скоринговые системы в банках. 

# <div class="alert alert-danger">
#     <h3> Комментарий ревьюера ❌<a class="tocSkip"> </h3>
#     
# Все этапы исследовательской части рассмотрены. Но не хватает деталей.
#         
# Стоит учитывать, что твой потенциальный руководитель, в первую очередь, обратит внимание на общий вывод. Поэтому важно отразить в нём все основные результаты из всех шагов проекта в числах. А также описать проблемы, найденные на этапе предобработки, и пути их решения
#         
# Можно опираться на такую структуру финального вывода во всех проектах:
# * предобработка данных с описанием найденных проблем и путей их решения
# * ответы на цели проекта
# * рекомендации для заказчика
# 
# Чтобы лучше понимать, как оформлять комментарии в markdown-ячейках, советую изучить [краткое руководство по Маркдауну](https://paulradzkov.com/2014/markdown_cheatsheet/).
# 
# </div>

# <div class="alert alert-block alert-info">
# <h3> Комментарий студента  <a class="tocSkip"></h3>
#     
# **Выводы по проверенным гипотезам**  
# В целом по выдвинутым гипотезам корреляция прослеживается, но её сложно назвать очень высокой: 
# * есть небольшая зависимость между количеством детей и возвратом кредита в срок: исследовав наиболее многочисленные группы (без детей, 1 ребёнок и 2 ребёнка), можем сказать, что среди семей, в которых нет детей, процент "должников" (8.2%) ниже, чем среди семей, в которых 1 или 2 ребёнка (9.2 и 9.5 процентов соответственно). 
# * наблюдается зависимость возврата кредита в срок от семейного положения: люди, когда-либо состоявшие в браке (разведённые и вдовцы), чаще возвращают кредиты в срок: процент "должников" среди них 6.6 и 7.1 соответственно, тогда как наиболее высокий процент "должников" - среди тех, кто не женат, он составляет 9.8 
# * проверив наиболее многочисленные группы клиентов банка, можем сказать, что есть зависимость между дозодом и возвратом кредита в срок: клиенты, чей заработок составляет 50-200 тысяч, в среднем чаще допускали просрочки, чем клиенты с заработком 200-1000 тысяч: среди первых процент "должников" - 7.1, тогда как среди вторых - 8.5.
# * цели кредита также коррелируют с возвратом кредита в срок: задолженность по кредитам на жилплощадь наблюдалась в 7.26 процентов случаев, по кредитам на свадьбу - в 7.9 процентов, тогда так процент просрочек по кредитам на операции с автомобилями (9.3) и на обучение (9.6) ощутимо выше. 
#     
#     
# **Общий вывод по всем гипотезам**       
# Можем попробовать составить портрет надёжного и ненадёжного заёмщика. Относительно надёжный заёмщик не будет состоять в браке, но при этом будет иметь опыт брака, у него будет высокий доход и не будет детей. Целью кредита будет операция с недвижимостью. Относительно ненадёжный заёмщик может иметь 1-2 детей, будет не женат или состоять в гражданском браке, будет иметь низкий доход. Целью кредита будет покупка автомобиля или получение образования. При этом не обязательно эти факторы должны совпасть и не обязательно эти факторы предскажут нам поведение заёмщика, поэтому делать вывод о возможности выдачи кредита пользователю по таким параметрам не стоит, для этого существуют гораздо более подробные скоринговые системы в банках.
#     
#     
# **Общий вывод по проекту**  
# В рамках данного проекта мы проверили гипотезы о зависимости возврата кредита в срок от различных параметров, заметили явную и не очень явную корреляцию, а также обработали исходные данные и сделали вывод о портрете потенциального "нарушителя" правил выплаты кредита. 
#     
# </div>

# <div class="alert alert-success">
# <h3> Комментарий ревьюера v2 ✔️<a class="tocSkip"> </h3>
# 
# Теперь получился очень хороший структурированный вывод. Все категории клиентов учтены. И даны рекомендации для заказчика. Отличная работа!
#     
# </div>