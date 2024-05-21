data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
d_s1 = []


def calculate_structure_sum(*args):
    #print(data_structure)
    new_data_structure = []
    int_res = []
    int_res2 = []
    int_res1 = []
    for i in data_structure:
        if isinstance(i, tuple):  # если элемент является кортежем
            a = list(i)
            new_data_structure.append(a)
        if isinstance(i, str):
            d = len(list(i))
            int_res.append(d)

        if isinstance(i, list):
            b = i
            int_res.append(b)
        if isinstance(i, dict):
            b = list(dict.values(i))
            c = len(dict.keys(i))
            int_res.append(b)
            int_res.append(c)
    for j in new_data_structure:
        if isinstance(j, list):
            for k in j:
                if isinstance(k, dict):
                    h = list(dict.values(k))
                    p = dict.keys(k)
                    int_res.append(h)
                    int_res2.append(list(p))
                    #print(h)
                    #print(p)
                if isinstance(k, int):
                    int_res.append(k)
                if isinstance(k, list):
                    for t in k:
                        if isinstance(t, set):
                            for z in t:
                                if isinstance(z, tuple):
                                    for x in z:
                                        if isinstance(x, int):
                                            int_res.append(x)
                                        if isinstance(x, str):
                                            int_res.append(len(x))
                                        if isinstance(x, tuple):
                                            for m in x:
                                                if isinstance(m, int):
                                                    int_res.append(m)
                                                if isinstance(m, str):
                                                    int_res2.append(m)
    for n in int_res2:
        if isinstance(n, list):
            for u in n:
                if isinstance(u, str):
                    v = u
                    int_res.append(len(v))
        if isinstance(n, str):
            int_res.append(len(n))
    for w in int_res:

        if isinstance(w, list):
            int_res1.append(sum(w))
        if isinstance(w, int):
            l = w
            int_res1.append(l)
    result = sum(int_res1)
    print(result)
    #print(new_data_structure)
    #print(int_res)
    #print(int_res1)

result = calculate_structure_sum(data_structure)
print(result)