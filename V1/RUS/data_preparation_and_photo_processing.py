###########################################################
########### MIT license 2022 Vladimir Shalyapin ###########
###########            Python   v 3.8           ###########
###########################################################

# Импорт библиотек и модулей
from skimage.io import imread, imshow
import numpy as np

# Функция подготовки изображения и формирования массива данных

def gray_image(x):
    # Переводит все пиксели в оттенки серого
    image_gray = imread(x, as_gray=True)
    # Формирует массив данных (decimals = 1, 1 знак после запятой, decimals = 0, целое число)
    # Нам необходимо значение округленное до тысячных
    na_image_gray = np.around(image_gray, decimals = 3)
    return na_image_gray, image_gray

# Облегчение работы с единичными файлами путем оптимизации ввода названия файла
name_file = str('namefile')

# В функцию размещается обрабатываемое изображение 
na_image_gray, image_gray = gray_image(name_file + ".JPG")

# Формирует массив данных (1, 192) с интервалом значений от 0.01 до 0.99
r_na_image_gray = (na_image_gray.reshape(1, 192) / 1.02) + 0.01

# Округляем значения в массиве до сотых
data = np.around(r_na_image_gray, decimals = 2)

# Вводим целевую переменную в наши данных np.insert(np.append(data, []), 'позиция т.е первая'0, 'целевая и известная переменная, она же номер группы'0)
target_data = np.insert(np.append(data, []), 0, 0)

# Формируем лист (1, 193) для сохранения его в .csv файл
r_target_data = target_data.reshape(1, 193)
print(r_target_data.shape)

# Сохраняем полученные значения и смотрим что получилось 
save_target_data = np.savetxt(name_file + ".csv", r_target_data, delimiter=",", newline='\n', encoding='ANSI')
load_target_data = np.loadtxt(name_file + ".csv", delimiter=",")
print(load_target_data)
print(load_target_data.shape)
