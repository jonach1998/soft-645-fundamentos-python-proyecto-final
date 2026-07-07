import getpass

def validar_contrasena():
    contrasena_correcta = "SanPascualin2026"
    intentos = 3
    
    while intentos > 0:
        ingreso = input("LOGIN: Ingrese la contraseña: ")
        
        if ingreso == contrasena_correcta:
            print("Acceso concedido con éxito\n")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}\n")
            
    print("Acceso denegado. Demasiados intentos fallidos.")
    return False
