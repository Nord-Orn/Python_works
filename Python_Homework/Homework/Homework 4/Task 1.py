# Вычислить число c заданной точностью d
# Пример:  - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d = input('введите d, где d < 1, 10^{-1} ≤ d ≤10^{-10} ')
count = -2
for i in d:count += 1
print(round(math.pi, count))