# TODO Найдите количество книг, которое можно разместить на дискете
symbol = 4    #хранение кода одного символа
symbol_in_line = 25    #число символов в строке
line_on_page = 50    #число строк на странице
pages_in_book = 100    #число страниц в книге

one_book_memory = symbol * symbol_in_line * line_on_page * pages_in_book


kb_to_byte = 1024    #перевод килобайта в байты
mb_to_kb = 1024    #перевод мегабайта в килобайты
disk_volume = 1.44 * kb_to_byte * mb_to_kb    #расчёт объёма диска

books_at_disk = disk_volume / one_book_memory    #количество книг на диске

print("Количество книг, помещающихся на дискету:", int(round(books_at_disk, 0)))
