numbers = [1,2,3,4,5,6, 7, 8, 100]
# result = []
# for number in numbers:
#     if number>3:
#         print(number)

# result = [number for number in numbers if number > 3]
# print(result)

# names = ['leo', 'max', 'kate', 'mag']
# names_upper = [name.upper() for name in names]
# print(names_upper)
#
# names_m = [name for name in names if name[0] == 'm']
# print(names_m)
# resu = [}
# for i in numbers:
#     if i < 5:
#         resu.append(0)
#     elif i > 5:
#         resu.append(1)
# print(resu)
# res = {random.randint(1,100) for i in range(100)}
# print(res)
import hashlib
hash_object = hashlib.md5(b'Hello world')
print(hash_object.hexdigest())