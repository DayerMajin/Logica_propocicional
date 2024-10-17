def tabla_verdad_not():
    print("A\tNOT A")
    print("----------------")
    for A in [0, 1]:
        resultado = not A
        print(f"{A}\t{int(resultado)}")

tabla_verdad_not()
