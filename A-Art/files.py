import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fonts", type=str, default=None,
                        help="Путь до шрифта, который нужно переместить в общий каталог шрифтов (с расширением ttf)")
    parser.add_argument("-c", "--clean_output", action="store_true", help="Очистить папку с результатами")
    arg = parser.parse_args()
    font_path = arg.fonts
    if font_path is not None:
        # Проверка на наличие файла
        if not os.path.exists(font_path):
            raise Exception("Не найден шрифт для добавления в каталог")
        if "/" in font_path:
            print("Нежелательный символ '/' в пути, заменён на '\\'")
            path = font_path.replace("/", "\\")
        file_name = arg.fonts.split("\\")[-1]
        expansion = arg.fonts.split("\\")[-1].split(".")[1]
        # Проверка, что файл с расширением fft
        if expansion != "ttf":
            raise Exception("Ожидалось расширение ttf для добавляемого шрифта")
        os.replace(font_path, f"fonts\\{file_name}")
    if arg.clean_output:
        directory = 'output_images'
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))