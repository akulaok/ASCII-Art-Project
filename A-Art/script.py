import argparse
from main import ArtConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Путь до файла")
    parser.add_argument("-s", "--need_show", action="store_true",
                        help="Указать, если нужно только показать результат с возможностью сохранения")
    parser.add_argument("-f", "--font_size", type=int, default=12, help="Размер шрифта")
    arg = parser.parse_args()
    ArtConverter(arg.path, arg.need_show, arg.font_size).run()