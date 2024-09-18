def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

def ingresar_lista():
    while True:
        entrada = input("Ingresa números separados por espacios: ")
        try:
            nums = list(map(int, entrada.split()))
            k = remove_duplicates(nums)
            print(f"Número de elementos únicos: {k}")
            print(f"Lista de números únicos: {nums[:k]}")
            break
        except ValueError:
            print("Error: Solo ingresa números enteros separados por espacios.")

ingresar_lista()