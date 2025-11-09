import os

def read_gene_list(filepath):
    """Reads a file containing one gene per line and returns a set of genes."""
    with open(filepath, 'r') as f:
        return {line.strip().upper() for line in f if line.strip()}

def main():
    """
    Finds and saves common genes from multiple miRNA target lists.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data', 'raw')
    results_dir = os.path.join(script_dir, '..', 'results')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    mirna_files = [
        'hsa-miR-106b-5p.txt',
        'hsa-miR-144-3p.txt',
        'hsa-miR-33a-5p.txt',
        'hsa-miR-33b-5p.txt',
        'hsa-miR-758-3p.txt'
    ]
    
    all_gene_sets = []
    print("--- Reading Gene Lists ---")
    for filename in mirna_files:
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            gene_set = read_gene_list(filepath)
            # A quick check to see if the file is just a placeholder
            if len(gene_set) < 2 and any("pega aquí la lista" in s.lower() for s in gene_set):
                 print(f"AVISO: El archivo ''{filename}'' parece ser un placeholder. Se omitirá del análisis.")
                 continue
            all_gene_sets.append(gene_set)
            print(f"Leídos {len(gene_set)} genes únicos de ''{filename}''.")
        else:
            print(f"ERROR: No se encontró el archivo ''{filename}''. Asegúrate de que exista en la carpeta ''data/raw''.")
            return

    if len(all_gene_sets) < len(mirna_files):
        print("\nAnálisis detenido. No se encontraron todos los archivos de datos necesarios o algunos son placeholders.")
        return

    print("\n--- Encontrando Genes Comunes ---")
    common_genes = set.intersection(*all_gene_sets)
    
    print(f"\nSe encontraron {len(common_genes)} genes en común en las {len(all_gene_sets)} listas.")
    
    if common_genes:
        sorted_common_genes = sorted(list(common_genes))
        
        print("Genes comunes encontrados:")
        for gene in sorted_common_genes:
            print(f"- {gene}")
            
        output_path = os.path.join(results_dir, 'common_genes.txt')
        with open(output_path, 'w') as f:
            for gene in sorted_common_genes:
                f.write(f"{gene}\n")
        print(f"\nLa lista de genes comunes ha sido guardada en: ''{output_path}''")
    else:
        print("No se encontraron genes comunes entre todas las listas proporcionadas.")

if __name__ == "__main__":
    main()
