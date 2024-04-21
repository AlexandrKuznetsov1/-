immutable_var_ = 'кортеж-the tuple', 2024, 35.5, 'tuple_',
print(immutable_var_)
immutable_var1_ = immutable_var_, 'списки', 2026
print(immutable_var1_)
print('Объект кортеж предназначен для хранения не изменяемых данных. При создании кортежа все внесенные в него данные получают свой индекс, для возможности быстрого обращения к ним, в том числе другие кортежи')
mutable_list = ['значения элементов в списках можно менять', 42,]
print(mutable_list)
mutable_list.append('значения элементов в кортеже изменить нельзя')
print(mutable_list)
mutable_list.extend("Urban")
print(mutable_list)
mutable_list.remove(42)
print(mutable_list)
print(mutable_list[0])