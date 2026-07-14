import os
import csv

def cargar_y_validar_logs(ruta_archivo):
 
    if not os.path.exists(ruta_archivo):
        print(f" Error crítico: El archivo '{ruta_archivo}' no existe.")
        return None

    logs_limpios = []

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)


        columnas_requeridas = [
            "Cliente",
            "Tiempo de respuesta (ms)",
            "Código de estado",
        ]
        if not all(col in lector_csv.fieldnames for col in columnas_requeridas):
            print(
                f" Error de formato: El CSV debe contener las columnas {columnas_requeridas}"
            )
            return None

        for num_fila, fila in enumerate(lector_csv, start=2):
            try:
                
                registro = {
                    "Cliente": fila["Cliente"].strip(),
                    "Tiempo de respuesta (ms)": int(
                        fila["Tiempo de respuesta (ms)"]
                    ),
                    "Código de estado": int(fila["Código de estado"]),
                }
                logs_limpios.append(registro)
            except ValueError:
                print(
                    f" Advertencia: Fila {num_fila} ignorada por datos corruptos."
                )

    return logs_limpios

def desplegar_reporte_ejecutivo(reporte_final):
   
    print("\n" + "=" * 85)
    print(
        f"{'CLIENTE':<18} | {'PETICIONES':<12} | {'LATENCIA PROMEDIO':<18} | {'ERRORES 5xx':<12} | {'ESTADO'}"
    )
    print("=" * 85)

    
    UMBRAL_LATENCIA_MS = 2500 
    UMBRAL_ERRORES_CRITICOS = 3  

    for cliente, metricas in reporte_final.items():
        promedio_formateado = f"{metricas['Promedio_Tiempo']:.2f} ms"

       
        if (
            metricas["Promedio_Tiempo"] > UMBRAL_LATENCIA_MS
            or metricas["Errores_5xx"] > UMBRAL_ERRORES_CRITICOS
        ):
            estado_alerta = "🚨 CRÍTICO (SLA en riesgo)"
        elif metricas["Errores_5xx"] > 0:
            estado_alerta = "⚠️ ADVERTENCIA"
        else:
            estado_alerta = "✅ ESTABLE"

        
        print(
            f"{cliente:<18} | {metricas['Peticiones']:<12} | {promedio_formateado:<18} | {metricas['Errores_5xx']:<12} | {estado_alerta}"
        )

    print("=" * 85 + "\n")