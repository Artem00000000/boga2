# boga2
## Описание игры
Boga II — компьютерная игра, в которой нужно искать богу — вымышленное животное или мифического зверя из семейства Хёрклов. Он прячется на сетке с размерами до 20 на 20 клеток.
В игре есть подсказки, которые указывают, в каком направлении двигаться, чтобы найти богу. При этом он сам ищет игрока. Угадывания продолжаются поочерёдно, пока один из игроков, человек или бога, не найдёт другого. 
Перед началом игры есть возможность увидеть инструкции к игре.

![image](https://github.com/user-attachments/assets/f6f7eeca-9216-455a-b70a-0132f995f5dc)

В инструкции говорится: "БОГА ПРЯЧЕТСЯ НА СЕТКЕ (ВЫ УКАЗЫВАЕТЕ ДЛИНУ И ШИРИНУ). ПОПРОБУЙТЕ УГАДАТЬ ЕГО ПОЛОЖЕНИЕ, ИСПОЛЬЗУЯ ПОДСКАЗКИ, КОТОРЫЕ Я ВАМ ДАЮ. КАЖДАЯ ОТГАДКА - ЭТО ДВА ЧИСЛА, РАЗДЕЛЕННЫЕ ЗАПЯТОЙ. ПОЖАЛУЙСТА, ИМЕЙТЕ В ВИДУ, ЧТО БОГА ТАКЖЕ ИЩЕТ ВАС!!!!"
Далее нужно ввести размер игрового поля, и при необходимости можно отобразить полученную сетку.

![image](https://github.com/user-attachments/assets/1cb33402-36d1-4ccc-8e9b-530f3526d70f)

Затем игрок выбирает свою стартовую позицию на поле, и игра начинается.

![image](https://github.com/user-attachments/assets/f964c586-1c3c-4c20-8546-bd1f99147a67)

Теперь игрок должен посещать по одной клетке за ход, чтобы найти позицию боги.
После каждой неудачной попытки игра подсказывает игроку, в каком направлении ему нужно двигаться.
Затем бога также посещает какую-то клетку, чтобы найти позицию игрока.

![image](https://github.com/user-attachments/assets/77cf3e9b-3c40-456b-8511-e28ee24195dd)

Игра продолжается до тех пор, пока не произойдёт одно из следующих событий:
1) Бога найдёт позицию игрока;
2) Игрок найдёт позицию боги;
3) Закончатся попытки (10 попыток).

![image](https://github.com/user-attachments/assets/9367c354-84bc-4057-adb2-f25ce8ca3fc0)

Далее игра предлагает сыграть снова. При этом игра начнётся с момента выбора размера сетки. В ином случае игра завершается.

## Описание проекта
Данный проект посвящён портированию оригинальной игры boga2, написанной на языке VISUAL BASIC, на язык ptthon. После этого необходимо проестировать игру, проверив, что она работает в точности также как и оригинал. Затем игра должна быть адаптирована под 3 платформы: Windows, Linux и Web.

## Тестирование
Для автоматизированного тестирования была написана программа, в которой создаются два параллельных субпроцесса: в одном запускается файл игры на VISUAL BASIC, в другом её адаплтация на python. Подавая на вход в оба процесса одинаковые данные, введённые пользователем, программа читает данные, полученные на выхде и сравнивает их. Если данные различаются, выводятся оба фрагмента, иначе - только один.
Так как в игре используется функция для генерации случайных чисел для определения начальной позиции боги, что препятствовало бы правильному тестированию, она была заменена на константое число.

![image](https://github.com/user-attachments/assets/28840405-3fc4-4afa-83c6-7b49b7ebb1bd)
![image](https://github.com/user-attachments/assets/5c397d52-4a3b-4b76-93a0-57b1d29318ca)
![image](https://github.com/user-attachments/assets/ef7424a4-d193-47bd-a48e-4706a77f3062)

На следующем скрине показан формат вывода в случае обнаружения различий в выводе программ.

![image](https://github.com/user-attachments/assets/866564f7-cdf9-444b-816d-e0279605bedb)

## Запуск на платформе Windows
Для проверки работоспособности игры на платформе Windows игра запускается в командной строке.

![image](https://github.com/user-attachments/assets/52cb755c-2ec1-49a8-be17-0a9b045b7407)
![image](https://github.com/user-attachments/assets/c94fdcbf-ba2d-4a42-bf1a-410a33d598b9)
![image](https://github.com/user-attachments/assets/7b61b5eb-0928-465a-bc2a-cae576b78005)

##Запуск на платформе Linux
Для проверки работоспособности игры на платформе Linux игра запускается в WSL.

![image](https://github.com/user-attachments/assets/a99303a5-2477-415a-9c1d-0fae6e5ba610)
![image](https://github.com/user-attachments/assets/94914157-b119-4950-b5ae-b47cf2e12839)

## Запуск в web-браузере
Для портирования игры под web был использован brython.

![image](https://github.com/user-attachments/assets/534d4375-f86b-4c02-b0d0-51f730fba322)
![image](https://github.com/user-attachments/assets/0d6c17a9-27e4-443a-906e-b2bd3b517421)
