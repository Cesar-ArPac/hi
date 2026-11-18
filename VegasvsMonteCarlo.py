import random
import time

PI_REAL = 3.14159
R = 0.5


def monte_carlo(N):
    dentro = 0

    inicio = time.perf_counter()

    for i in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if x*x + y*y < R*R:
            dentro += 1

    pi_estimado = 4 * (dentro / N)

    tiempo = time.perf_counter() - inicio
    error = abs(PI_REAL - pi_estimado)

    return pi_estimado, error, tiempo


def las_vegas(K):
    dentro = 0
    total = 0

    inicio = time.perf_counter()

    while dentro < K:
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        total += 1

        if x*x + y*y < R*R:
            dentro += 1

    pi_estimado = 4 * (K / total)

    tiempo = time.perf_counter() - inicio
    error = abs(PI_REAL - pi_estimado)

    return pi_estimado, error, tiempo, total


print("======================================")
print("       ESTIMACION DEL NUMERO PI")
print("======================================")

valores_N = [1000, 10000, 100000, 1000000]
valores_K = [785, 7854, 78540, 785398]

print("\n========== MONTE CARLO ==========")

for N in valores_N:
    pi, error, tiempo = monte_carlo(N)

    print(f"\nN = {N}")
    print(f"Pi estimado: {pi:.6f}")
    print(f"Diferencia: {error:.6f}")
    print(f"Tiempo: {tiempo:.6f} segundos")


print("\n========== LAS VEGAS ==========")

for K in valores_K:
    pi, error, tiempo, total = las_vegas(K)

    print(f"\nK = {K}")
    print(f"Puntos generados: {total}")
    print(f"Puntos dentro: {K}")
    print(f"Pi estimado: {pi:.6f}")
    print(f"Diferencia: {error:.6f}")
    print(f"Tiempo: {tiempo:.6f} segundos")


print("\n======================================")
print(f"Valor real de PI: {PI_REAL}")
print("======================================")