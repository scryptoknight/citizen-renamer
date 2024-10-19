# shadow of doubt citizen-renamer

## ru:

Приложение для переименования горожан в Shadow of Doubt.
Работает только с городами, в сохранении нельзя переименовать,
т.е. придется начинать новую игру.

Как работает:
В самой игре:
Новая игра -> Песочница -> Сгенерировать город
После генерации города в окне создания персонажа - > Настройки игры
и так выключаем "Сжатие игровых сохранений" и "Сжатие данных о городе".
Далее начинаем новую игру, чтобы у нас сгенерировался город и выходим.

Далее переходим к `citizen-renamer`.
1) Распаковываем архив, куда угода.
2) Открываем SoD Citizens `Renamer\dist\main.exe`
3) В открывшееся окно вставляем путь до города.
Пример: `C:\Users\<username>\AppData\LocalLow\ColePowered Games\Shadows of Doubt\Cities\<cityname>.cit`
4) В открывшемся окне переименовываем горажан посредством ввода новых имен и нажатие кнопки `Rename`.
5) Нажимаем кнопку `Save`.

У нас сохранится файл рядом с `main.exe`. Его переносим по пути, откуда брали исходный город.

Внимание!
1) Я не уверен, что это не поломает сохранения.
2) Сам `citizen-renamer` тормозит из за перевода из str в json и обратно, поэтому может немного "тупить".
3) GUI сделано криво.
4) Новый файл города будет весить чуть больше, опять же из-за перевода str в json и обратно.

## eng:

An application for renaming citizens in Shadow of Doubt.

Works only with cities; renaming in an existing save is not possible,

thus requiring a new game to be started.

How it Works:

In the game itself:
New Game -> Sandbox Mode -> Generate City
After generating the city, in the character creation window -> Game Settings
turn off "Game Saves Compression" and "City Data Compression".
Then start a new game, generate the city, and exit.

Next, proceed to `citizen-renamer`.
1) Unzip the archive wherever you prefer.
2) Open SoD Citizens Renamer\dist\main.exe
3) In the opened window, insert the path to the city.
Example: `C:\Users&lt;username>\AppData\LocalLow\ColePowered Games\Shadows of Doubt\Cities&lt;cityname>.cit`
4) In the opened window, rename citizens by entering new names and clicking the `Rename` button.
5) Click the `Save` button.

A file will be saved next to main.exe. Move it back to the location where you took the original city.

Attention!

1) I am not sure this won't break your saves.
2) The citizen-renamer itself slows down due to the conversion from str to json and back, so it may "lag" a bit.
3) The GUI is poorly made.
4) The new city file will weigh slightly more due to the str to json conversion and vice versa.
