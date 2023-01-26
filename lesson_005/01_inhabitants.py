# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1
import room_2

print('В комнате 1 живут: ' + ", ".join(room_1.folks))
print('В комнате 2 живут: ' + ", ".join(room_2.folks))
