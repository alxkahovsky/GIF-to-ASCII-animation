Простой проект для преобразования GIF-анимации в анимированные ASCII-арты.

В корне проекта находится файл script.py, запустив который мы разбиваем gif-анимацию на кадры, а после
преобразуем в ASCII-арты формата txt. На основе артов формируем HTML-документ при помощи шаблонизатора jinja2.
Анимация внутри HTML документа реализована на JS.

Инструкция по запуску (windows):
0. Загружаем и устанавливаем Python https://www.python.org/downloads/
1. Загружаем репозиторий командой git clone https://github.com/alxkahovsky/GIF-to-ASCII-animation.git или
скачиваем .zip архив https://github.com/alxkahovsky/GIF-to-ASCII-animation и распаковываем;
2. Создаем виртуальное окружение. выполняем команды:
    pip install virtualenv
    pip install virtualenvwrapper-win
    mkvirtualenv [path-to-project\venv]  (mkvirtualenv C:\Users\Admin\Desktop\GIF-to-ASCII-animation-master\venv)
    venv\Scripts\activate
Подробнее об этом можно прочитать тут: https://habr.com/ru/post/491916/
3. Запускаем script.py командой python script.py
4. После запуска интерпритатор попросит указать путь к gif-файлу и количество кадров на которые следует разбить анимацию
Количество кадров зависит от длительности анимации, в тестах я указывал от 6 до 20 кадров и опытным путем выяснил,
что 10-12 кадров это оптимальное количество. При повторном запуске убедитесь, что вы удалили старые кадры.
5. JPG и TXT кадры будут созранены в каталоге media/img_frames/имя-файла и  media/ascii_frames/имя-файла соответственно
6. Переходим в папку web_page и запускаем имя-файла.html

PS можно изменять частоту смены кадров в файле web_page/static/cript.js, и стили в файле web_page/static/style.css
PSS в папке bonus Гендальф качает головой под музыку
