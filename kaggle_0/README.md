# Kaggle 0. Предсказание стоимости подержанного автомобиля

## Оглавление  
[0. Ссылка на файл с исходными данными](https://www.kaggle.com/competitions/sf-dst-predict-car-price/overview)   
[1. Описание проекта](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Этапы-работы-над-проектом)  
[5. Результаты](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Результаты)    
[6. Выводы](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Выводы) 

### Описание проекта    
Соревнование по предсказанию стоимости подержанного автомобиля.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


### Какой кейс решаем?    
Создадим baseline для предсказания адекватной стоимости машины по ее характеристикам из объявления на основе библиотеки LightAutoML (LAMA).

**Метрика качества**     
Метрикой в данном соревновании является MAE - среднее абсолютное отклонение (mean absolute error).

**Что практикуем**     
1. Знакомимся с платформой Kaggle. 
2. Знакомимся с возможностями библиотеки LightAutoML.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


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
  
:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


### Этапы работы над проектом:  
1. Знакомство с данными, подготовка данных для LightAutoML.
2. Настройка параметров LightAutoML.
3. Обучение тренировочной и валидационной выборок.
4. Изучение важности признаков при построении модели.
5. Предсказание на тестовых данных, подготовка сабмита. 

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


### Результаты:  
1. Благодаря LightAutoML удалось получить score 1747.31421, не прилагая усилий к подготовке датасета (не пришлось очищать данные от пропусков, удалять дубликаты и так далее).
2. Получил первый опыт работы с платформой Kaggle.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


### Выводы:  
Библиотека LightAutoML позволяет автоматически строить модели машинного обучения для различных задач. Этот инструмент позволяет сосредоточиться на важных задачах машинного обучения — генерации признаков, выборе метрик, определении целевой переменной и так далее.

:arrow_up: [К оглавлению](https://github.com/alpisarev/sf_data_science/tree/main/kaggle_0/#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️