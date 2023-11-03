import argparse
from ArtConverter import ArtConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Путь до файла")
    parser.add_argument("-n", "--need_preview", action="store_true",
                        help="Указать, если нужно только показать результат с возможностью сохранения")
    parser.add_argument("-f", "--font_size", type=int, default=12, help="Размер шрифта")
    parser.add_argument("-p", "--ascii_palette", type=str, default=' .,"-~+*:;!vxnm#W&8@',
                        help="Палитра ascii-символов")
    parser.add_argument("-s", "--need_sort_palette", action="store_true",
                        help="Указать, если нужна сортировка палитры ascii-символов по яркости")
    parser.add_argument("-v", "--variable_space", action="store_false",
                        help="Добавление пробела в палитру ascii-символов")
    arg = parser.parse_args()
    ArtConverter(arg.path, arg.need_preview, arg.font_size, arg.ascii_palette, arg.need_sort_palette,
                 arg.variable_space).run()
