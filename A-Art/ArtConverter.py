import cv2
from PIL import Image, ImageDraw, ImageFont
import os
from math import ceil
from AsciiSorter import AsciiSorter


class ArtConverter:
    """Этот клас читает изображение и создаёт новое с помощью ASCII-символов"""

    def __init__(self, path, font_size, ascii_palette, need_sort_palette, variable_space, font_name):
        """Конструктор класса"""
        # Проверка на наличие токого файла
        if not os.path.exists(path):
            raise Exception("По данному пути ничего не найдено")
        if font_size <= 0:
            raise Exception("Размер шрифта не может быть меньше или равен нулю")
        if not os.path.exists(f"fonts\\{font_name}.ttf"):
            raise Exception("Шрифта с таким именем нет в каталоге")
        if "/" in path:
            print("Нежелательный символ '/' в пути, заменён на '\\'")
            path = path.replace("/", "\\")
        # Путь до файла
        self.path = path
        # Имя файла
        self.file_name = path.split("\\")[-1].split(".")[0]
        # Расширение файла
        self.expansion = path.split("\\")[-1].split(".")[1]
        # Проверка, что входной файл подходт по расширению
        if self.expansion not in ["jpg"]:
            raise Exception(f"Расширение {self.expansion} не обрабатывается")
        # Получаем изображение как спсисок списков, состояших из номеров цвета пикселей
        self.image = self.get_image()
        # Получаем размеры изображения
        self.res = self.width, self.height = self.image.shape[0], self.image.shape[1]
        # Заготовка для изображения PIL
        self.pil_image = Image.new("RGB", (self.width, self.height), "black")
        # Палитра ascii-символов  (Можно поэксперементировать)
        self.ascii_chars = list(ascii_palette)
        # Обозначение пути до шрифта
        self.font_path = f"fonts\\{font_name}.ttf"
        # Размер шрифта
        self.font_size = font_size
        # Добавление пробельного символа
        if variable_space:
            self.ascii_chars = [" "] + self.ascii_chars
        # Сортировка выбранной палитры ascii-символов
        if need_sort_palette:
            sorter = AsciiSorter(self.font_size, self.ascii_chars, self.font_path)
            self.ascii_chars = sorter.sort_ascii_chars()
        if len(list(self.ascii_chars)) >= 256:
            raise Exception("В палитре не может быть больше 255 разных символов")
        # Средство для определения, какой символ писать
        self.ascii_coefficient = ceil(255 / (len(self.ascii_chars)))
        # Константа, взятая, чтобы размеры изображений совпадали
        self.char_step = int(self.font_size * 0.6)
        # Определение шрифта для PIL и проверка того, что с ним можно работать
        try:
            self.font = ImageFont.truetype(self.font_path, self.font_size)
        except Exception:
            raise Exception("Возникла ошибка при работе со шрифтом, пожалуйста, выберите другой")

    def get_image(self):
        """Этот метод переводит изображение в список списков пикслей"""
        # Получение изображения в виде высота-[ ширина-[ пиксель(3 цвета)-[],[],[] ],[ [][][] ],[ [][][] ] ]
        cv2_image = cv2.imread(self.path)
        # Транспонирование матрицы () иначе изображение перевёрнутое
        transposed_image = cv2.transpose(cv2_image)
        # Покраска пикселей в серый цвет (от 0 до 255)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def draw_converted_image(self):
        """Формирование ascii-изображения"""
        # Присвоение пикселю соответствующую ему букву палитры ascii-символов
        char_indices = self.image // self.ascii_coefficient
        # Стандартная процедура для начала рисования PIL
        draw = ImageDraw.Draw(self.pil_image)
        # Обход излбражения с нужным шагом и зарисовка нужных символов для PIL
        for x in range(0, self.width, self.char_step):
            for y in range(0, self.height, self.char_step):
                draw.text((x, y), self.ascii_chars[char_indices[x, y]], font=self.font, fill="white")
        # Сохранение изображения
        self.pil_image.save("output_images\\" + self.file_name + "_converted." + self.expansion)
