from Bio import SeqIO
import os

# --- CONFIGURACIÓN ---
# Asegúrate de que este nombre coincida EXACTAMENTE con tu archivo en data/raw
nombre_archivo_entrada = "hypothetical_abaumannii.fasta" 

# Rutas dinámicas (funcionan en cualquier PC)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(base_dir, "data", "raw", nombre_archivo_entrada)
output_path = os.path.join(base_dir, "data", "processed", "candidates.fasta")

candidates = []

print(f"Leyendo archivo desde: {input_path}")

try:
    # Leemos el archivo FASTA
    for record in SeqIO.parse(input_path, "fasta"):
        
        # FILTRO 1: Longitud (Length)
        # Menos de 100aa es muy pequeño (pueden ser péptidos o errores).
        # Más de 350aa es muy complejo para empezar a modelar.
        if 100 <= len(record.seq) <= 350:
            
            # FILTRO 2: Calidad (Quality)
            # La 'X' significa que el secuenciador no supo qué aminoácido era.
            # No queremos huecos en nuestra información.
            if 'X' not in record.seq:
                candidates.append(record)

    print(f"------------------------------------------------")
    print(f"Total procesados: {len(list(SeqIO.parse(input_path, 'fasta')))}")
    print(f"Candidatos viables encontrados: {len(candidates)}")
    print(f"------------------------------------------------")

    if len(candidates) > 0:
        # Guardamos los resultados
        SeqIO.write(candidates, output_path, "fasta")
        print(f"¡Éxito! Archivo guardado en: {output_path}")
        
        # Mostramos el ID del primer candidato para que lo uses luego
        print(f"\nTU PRIMER CANDIDATO PARA BLAST ES: {candidates[0].id}")
    else:
        print("No se encontraron candidatos con esos filtros. Intenta ampliar el rango de longitud.")

except FileNotFoundError:
    print(f"\n[ERROR] No se encuentra el archivo: {input_path}")
    print("Verifica que el nombre en la línea 6 del script sea igual al de tu archivo en data/raw/")