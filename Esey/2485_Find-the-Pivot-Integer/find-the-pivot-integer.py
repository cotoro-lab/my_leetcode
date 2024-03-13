# 2485. Find the Pivot Integer
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        rtn_int = -1
        in_array = [i for i in range(1, n + 1)]

        for i in range(1, n + 1):
            wk_array = in_array[(-1 * i):]
            tale_sum = sum(wk_array)
            head_sum = sum(x for x in range(1, wk_array[0] + 1))

            if head_sum == tale_sum:
                rtn_int = in_array[n - i]
                break

        return rtn_int

    # Best solution
    def pivotInteger_best(self, n: int) -> int:
        # 1からnまでの自然数の和（等差数列の和）を2で割った値の平方根を計算している。
        x = math.sqrt(n*(n+1)/2)
        converted = int(x)
        return converted if converted == x else -1