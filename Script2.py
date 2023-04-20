VLAN = 0

VLAN = int(input("Ingrese el número de VLAN deseada: "))

if VLAN >= 1 and VLAN <= 1005:
    print(VLAN, "corresponde al rango normal")

else:
    if VLAN >= 1006 and VLAN <= 4095:
        print(VLAN, "corresponde al rango extendida")

    else:
        if VLAN >= 4096:
            print("El valor de la VLAN es incorrecto.")
         

