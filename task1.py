# Напишите алгоритм поиска в глубину (DFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать DFS (Depth-First Search) — обход графа в глубину.
# 2.Вернуть список вершин в порядке их посещения.

# Пример входных данных
# Пример выходных данных
# [1, 2, 4, 3, 5]  # Возможен и другой порядок, зависящий от реализации DFS
graph = {
1: [2, 3],
2: [1, 4],
3: [1, 5],
4: [2],
5: [3]}
first = 1
Suda=[first]
Already=set() #посещнные
Result=[] #это показываем
while Suda:
    now=Suda.pop() #извлекаем с конца
    if now not in Already:
        Already.add(now)
        Smeshznie = graph.get(now, []) #соседи рассматриваемой (добавляем в обратном порядке чтобы сначала посмотреть двойку)
        #print(Smeshznie)
        Result.append(now)
        #print(now)
        for Smeshznie in reversed(Smeshznie):
            if Smeshznie not in Already: #непосещенные соседи
                Suda.append(Smeshznie)
print(Result)


