# TODO Найдите количество книг, которое можно разместить на дискете
disk_storage = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
symbol_size = 4
res = int(disk_storage / (pages * lines * symbols * symbol_size))
print("Количество книг, помещающихся на дискету:", res)
