from PIL import ImageFont, ImageDraw, Image


class AsciiSorter:
    """Этот класс предназначен для сортировки палитры ascii-символов"""

    def __init__(self, font_size, ascii_palette):
        """Конструктор класса"""
        # Палитра ascii-символов с удалением дублей (Можно поэксперементировать)
        self.ascii_chars = list(set(ascii_palette))
        # Обозначение пути до шрифта
        self.font_path = r"fonts\Roboto-BoldItalic.ttf"
        # Размер шрифта
        self.font_size = font_size

    def sort_ascii_chars(self):
        """Этот сортирует ascii-символы по 'яркости' """
        # Удаление дублей
        self.ascii_chars = list(set(self.ascii_chars))
        # Словарь: символ - его яркость
        chars_dict = {}
        # новая палитра
        sorted_ascii_chars = ""
        # Определение 'яркости' для каждого символа
        for char in self.ascii_chars:
            square = self.get_char_square(char)
            while square in chars_dict.keys():
                square += 1
            chars_dict[square] = char
        # Составление новой палитры ascii-символов
        for i in sorted(list(chars_dict.keys())):
            sorted_ascii_chars += chars_dict[i]
        print(f"Отсортированная палитра ascii-символов: {sorted_ascii_chars}")
        return sorted_ascii_chars

    def get_char_square(self, char: str):
        """Этот метод определяет, сколько пикселей занимает символ"""
        # Кол-во пикселей в символе
        square = 0
        # Обозначение шрифта для PIL
        font = ImageFont.truetype(self.font_path, self.font_size)
        # Создание изображения по размерам символа
        img = Image.new("RGB", font.getsize(char))
        # Подготовка к рисованию текста
        draw = ImageDraw.Draw(img)
        # Написание символа char в координатах (0, 0)
        draw.text((0, 0), char, font=font, fill="#ffffff")
        # Получение таблицы пикселей по написанному символу
        pixel_table = img.load()
        # Подсчёт кол-ва, занимаемого символом пикселей
        for j in range(img.size[0]):
            for k in range(img.size[1]):
                pixel = pixel_table[j, k]
                if pixel != (0, 0, 0):
                    square += 1
        # Для избежания ошибок, на всякий случай, закрытие изображения
        img.close()
        return square
