# Definimos la función principal para manejar las operaciones requeridas
def gestionar_calificaciones(calificaciones, calificacion_especifica):
    # Paso 2: Calculo del promedio
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Paso 3: Determinación de la calificación máxima y mínima
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)
    
    # Paso 4: Ordenar las calificaciones de mayor a menor
    calificaciones_ordenadas = sorted(calificaciones, reverse=True)
    
    # Paso 5: Verificar si una calificación específica está por encima del promedio
    def esta_por_encima_del_promedio(calificacion, promedio):
        return calificacion > promedio

    resultado = esta_por_encima_del_promedio(calificacion_especifica, promedio)
    
    # Imprimir los resultados
    print("Calificaciones ingresadas:", calificaciones)
    print("Promedio de las calificaciones:", promedio)
    print("Calificación máxima:", calificacion_maxima)
    print("Calificación mínima:", calificacion_minima)
    print("Calificaciones ordenadas de mayor a menor:", calificaciones_ordenadas)
    print(f"La calificación {calificacion_especifica} está por encima del promedio:", resultado)
    return {
        "promedio": promedio,
        "maxima": calificacion_maxima,
        "minima": calificacion_minima,
        "ordenadas": calificaciones_ordenadas,
        "especifica": resultado
    }

# Datos de ejemplo para probar el programa
calificaciones = [85, 90, 78, 92, 88]
calificacion_especifica = 90

# Llamamos a la función con los datos de ejemplo
gestionar_calificaciones(calificaciones, calificacion_especifica)
