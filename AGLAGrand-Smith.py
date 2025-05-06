import numpy as np
def gram_schmidt(vectors):
    nvectors = [] #хранилище веторов

    for v in vectors:
        nvector = np.array(v, dtype=float) #вычисление ветора и закидывание его ко всем
        nvectors.append(nvector) 
    basis = [] #базисы
    for v in vectors:
        summ = np.zeros_like(v, dtype=np.float64) #если не уточнить тип, то оно ломается, а там сумм = 0 вектор чтобы потом они нормально скаладывалисб
        for b in basis:
            projection = np.dot(v, b) / np.dot(b, b) * b #вычисление проекции и суммы проекций
            summ += projection
        w = v - summ
        w_normalized = w / np.linalg.norm(w) #вычисление нормированного вектора
        if not np.allclose(w, 0): #если вектрор не нулевой
            basis.append(w_normalized) #добавляем нормированный базис мариноваться к остальным
            
    return basis

#вот тут их надо менять
vectors = [
    [1, 7, 8, 1],
    [1, 2, 5, 6],
    [3, 4, 9, 16],
    [2, 7, 0, 1],
    [0, 1, 8, 7]
]

orthogonal_basis = gram_schmidt(vectors)

print("Ортогональный базис:") # переюор векторов с 1
for i, vec in enumerate(orthogonal_basis, 1):
    print(f"Вектор {i}: {np.round(vec, 2)}") # выводим вектора и чуть-уть округляем, если хочется больше циферок то трогать двойку!!
