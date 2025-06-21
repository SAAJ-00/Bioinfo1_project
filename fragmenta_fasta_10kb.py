import sys
from Bio import SeqIO

def dividir_secuencia_multifasta(archivo_entrada, tamaño_max_kb=10, archivo_salida="fragmentos.fasta"):
    tamaño_max_bytes = tamaño_max_kb * 1024

    try:
        with open(archivo_entrada, "r") as archivo:
            registro = next(SeqIO.parse(archivo, "fasta"))  # Tomamos el único registro
            secuencia = str(registro.seq)
            id_secuencia = registro.id
            
            tamaño_fragmento = tamaño_max_bytes // 2  # Ajustamos el tamaño en función de caracteres
            num_fragmentos = (len(secuencia) // tamaño_fragmento) + 1

            with open(archivo_salida, "w") as salida:
                for i in range(num_fragmentos):
                    inicio = i * tamaño_fragmento
                    fin = min((i + 1) * tamaño_fragmento, len(secuencia))
                    fragmento = secuencia[inicio:fin]
                    
                    salida.write(f">{id_secuencia}_fragmento_{i+1}\n{fragmento}\n")
            
            print(f"Proceso completado con éxito. Se generó el archivo multifasta '{archivo_salida}' con {num_fragmentos} fragmentos.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe. Verifica la ruta.")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python fragmenta_fasta_10kb.py <archivo.fasta>")
        sys.exit(1)

    archivo_fasta = sys.argv[1]
    dividir_secuencia_multifasta(archivo_fasta)
