***Пользовательские сценарии к проекту «Веб-сервис для садоводов и огородников»***

**[ Сценарий 1 - Регистрация пользователя ]**
<li>Пользователь вводит логин, с которым он будет заходить в систему
<li>Пользователь вводит пароль, с которым он будет заходить в систему
<li>Пользователь вводит адрес электронной почты, который будет использоваться в системе
<li>Если логин уже занят, система даёт рекомендации по придумыванию уникального логина
<li>Если пароль содержит менее 6 символов, система сообщает, что пароль должен быть от 6 до 30 символов и пользователь должен придумать новый пароль
<li>Если введённый адрес электронной почты не соответствует формату, то система выводит сообщение об ошибке и просит ввести адрес ещё раз
<li>Если все введённые данные соответствуют требованиям регистрации, то система отправляет на почту письмо для подтверждения почты
<li>После завершения регистрации переход к Сценарию 2

**[ Сценарий 2 - Запрос местоположения ]**
<li>Перед пользователем окно в котором запрашивается разрешение на взятие данных о местоположении
<li>При разрешении приложение благодарит за успешную регистрацию и переходит к работе
<li>При отказе приложение предупреждает каких возможностей лишится пользователь и запрашивает еще раз
<li>При повторном отказе приложение полностью закрывает окно и переходит к работе

**[ Сценарий 3 - Настройка параметров формы объекта участка ]**
<li>Перед пользователем главная страница и кнопка "Добавить объект"
<li>После нажатия открываются настройки для объекта
<li>Пользователь вводит названия объекта (Пример:"Клумба за домом")
<li>Пользователь выбирает форму объекта(круг или прямоугольник)
<li>Если форма объекта не соответствует ни одной из предложенных форм, пользователю предлагается написать сообщение разработчику с одним словом(форма какой фигуры)
<li>На этом завершается настройка формы объекта и переход к настройкам содержимого объекта

**[ Сценарий 4 - Настройка параметров объекта ]**
<li>После захода на страницу объекта перед пользователем кнопки "Добавить растение","Удалить растение","Удалить весь объект","Изменить название объекта"
<li>При нажатии "Добавить растение" пользователь выбирает точку на объекте, дает название растению и переход к Сценарию 5
<li>При нажатии "Удалить растение" пользователь выбирает растение, которое нужно удалить и после подтверждения растение исчезает с карты
<li>При нажатии "Удалить весь объект" удаляется объект и исчезает из списка всех объектов участка пользователя
<li>При нажатии "Изменить название объекта" открывается поле, куда нужно ввести новое название

**[ Сценарий 5 - Настройка параметров растений объекта ]**
<li>Перед пользователем объект, параметры растений которого он хочет изменить
<li>Нажатие на растение и открывается страница где можно добавить и убрать функции к растению
<li>При нажатии на "+" открывается окно куда нужно внести название функции и временные промежутки когда ее нужно выполнять
<li>При нажатии на "-" в соответствующем блоке удаляется функция
<li>После нажатия на кнопку "Сохранить" все изменения будут сохранены и откроется текущий объект

**[ Сценарий 6 - Страница уведомлений ]**
<li>Перед пользователем главная страница и кнопка "Уведомления"
<li>После нажатия открывается список всех растений, с которыми нужно произвести функции, зарегистрированные в Сценарии 5
<li>В поле растения будут указаны следующие данные: название объекта, название растения, функция для растения, ближайшее время, к которому нужно выполнить функцию
<li>Чем раньше время истечет для функции, тем выше растения находится в списке
<li>По истечении срока из списка удаляется верхняя функция

**[ Сценарий 7 - Данные о погоде ]**
<li>Перед пользователем главная страница и кнопка "Анализ почвы"
<li>Если пользователь после регистрации отказал в разрешения предоставить данные о местоположении, то эта страница для него будет пуста
<li>После нажатия открывается страница, где изображены все данные
<li>Текущая температура, наличие осадков, а также возможные рекомендации
<li>Пример рекомендации: "Сегодня утром был дождь, значит земля достаточно увлажнена и поливать не закрытые крышей растения не обязательно"
















