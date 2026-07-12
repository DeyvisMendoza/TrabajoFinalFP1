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
                # Validar y parsear tipos de datos
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

    return logs_limpios#comentario1
