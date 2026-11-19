from funciones_interfaz import*

def ingresar_productos():
    """Pide precios al usuario hasta escribir 'fin' o '0'. Retorna el subtotal."""
    print("REGISTRO DE VENTAS")
    subtotal = 0.0
    while True:
        entrada = input("Ingrese precio (o 'fin' para terminar): ")
        if entrada == "0" or entrada.lower() == "fin":
            return subtotal
        
        try:
            precio = float(entrada)
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
            else:
                subtotal += precio
        except ValueError:
            print("Error: Ingrese un número válido o 'fin' para terminar.")

def seleccionar_metodo_pago():
    """Valida y retorna '1' (Efectivo) o '2' (Tarjeta)."""
    imprimir_separador()
    print("--- Método de pago ---")
    while metodo_pago not in ["1", "2"]:
        metodo_pago = input("1. Efectivo\n2. Tarjeta\nOpción: ")
        if metodo_pago not in ["1", "2"]:
            print("Opción inválida. Seleccione 1 o 2.")

    return metodo_pago
    pass

def calcular_totales(subtotal, metodo_pago):
    """Calcula IVA, descuento y total final. Retorna el total_final."""
    monto_iva = subtotal_cliente * 0.19
    total_iva_cliente = subtotal_cliente + monto_iva


    if metodo_pago == "1":
        descuento = total_iva_cliente*0.05
    imprimir_separador()
    if metodo_pago == "1":
        descuento = total_iva_cliente*0.05
        print("Descuento por efectivo (5%): ", descuento)
    return total_iva_cliente
    pass

def procesar_venta():
    """Orquesta el flujo completo de una venta y retorna el monto final."""
    subtotal = ingresar_productos()
    if subtotal == 0:
        print("Venta cancelada (monto $0).")
        return 0.0
    
    metodo = seleccionar_metodo_pago()
    total_venta = calcular_totales(subtotal, metodo)
    return total_venta
