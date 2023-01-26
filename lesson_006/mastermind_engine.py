from random import randint

_num = []
_anim_dict = {}


# загадыватель оптимальный но недоделанный
# def guess_v05():
#     for i in range(4):
#         _num.append(randint(0, 9))
#     if _num[0] == 0:
#         _num[0] = randint(1, 9)

# загадыватель неоптимальный, но рабочий
def func_guess():
    row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    place_1 = randint(1, 9)
    _num.append(row[place_1])
    del row[place_1]
    for x in (8, 7, 6):
        place_2_3_4 = randint(0, x)
        _num.append(row[place_2_3_4])
        del row[place_2_3_4]
    return _num


def check(user_guess):
    global _anim_dict
    _anim_dict = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_guess[i] == _num[i]:
            _anim_dict['cows'] += 1
        if user_guess[i] in _num:
            _anim_dict['bulls'] += 1
    _anim_dict['bulls'] = _anim_dict['bulls'] - _anim_dict['cows']
    return _anim_dict
