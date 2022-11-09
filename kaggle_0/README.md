# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Этапы-работы-над-проектом)  
[5. Результаты](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Результаты)    
[6. Выводы](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Выводы) 

### Описание проекта    
Соревнование по предсказанию стоимости подержанного автомобиля.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Оглавление)


### Какой кейс решаем?    
Строим модель для предсказания адекватной стоимости машины по ее характеристикам из объявления при помощи библиотеки LightAutoML (LAMA).

**Метрика качества**     
Метрикой в данном соревновании является MAE - среднее абсолютное отклонение (mean absolute error).

**Что практикуем**     
1. Создаём свою первую модель, основанную на алгоритмах машинного обучения. 
2. Знакомимся с возможностями библиотеки LightAutoML.


### Краткая информация о данных
Автомобили описываются 15 признаками:
* row_id - ID объявления
* vehicle_manufacturer - марка автомобиля
* vehicle_model - модель автомобиля
* vehicle_category - тип машины
* current_mileage - текущий пробег
* vehicle_year - год выпуска
* vehicle_gearbox_type - тип коробки передач
* doors_cnt - количество дверей
* wheels - левый/правый руль
* vehicle_color - цвет машины
* vehicle_interior_color - цвет салона машины
* car_vin - VIN номер автомобиля
* car_leather_interior - флаг наличия кожаного салоона
* deal_type - тип объявления: продажа или аренда
* *final_price - стоимость машины (Целевая переменная)*
  
:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Оглавление)


### Этапы работы над проектом:  
1. Знакомство с данными, подготовка данных для LightAutoML.
2. Настройка гиперпараметров LightAutoML.
3. Обучение тренировочной и валидационной выборок.
4. Изучение важности признаков при построении модели.
5. Предсказание на тестовых данных, подготовка сабмита. 

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Оглавление)


### Результаты:  
1. Благодаря LightAutoML удалось получить score 1747.31421, не прилагая усилий к подготовке датасета (не пришлось очищать данные от пропусков, удалять дубликаты и так далее).

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Оглавление)


### Выводы:  
Библиотека LightAutoML позволяет автоматически строить модели машинного обучения для различных задач. Этот инструмент позволяет сосредоточиться на важных задачах машинного обучения — генерации признаков, выборе метрик, определении целевой переменной и так далее.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️