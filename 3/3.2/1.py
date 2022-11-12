x = lambda v: 1 if v == "А" else sum(
    x(n) for n in [a for a, b in set("АБ АВ АГ БВ БД ВД ВЕ ВЗ ВЖ ГВ ГЖ ДЕ ЕЗ ЖЗ".split()) if b == v])
