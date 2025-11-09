import os
import gseapy as gp
import pandas as pd

def read_gene_list(filepath):
    """Reads a file containing one gene per line and returns a list of genes."""
    with open(filepath, 'r') as f:
        return [line.strip().upper() for line in f if line.strip()]

def main():
    """
    Performs GO and KEGG pathway enrichment analysis on a list of common genes.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(script_dir, '..', 'results')
    common_genes_path = os.path.join(results_dir, 'common_genes.txt')

    if not os.path.exists(common_genes_path):
        print(f"ERROR: No se encontró el archivo ''common_genes.txt'' en la carpeta ''results''.")
        print("Por favor, ejecuta primero el script ''01_find_common_genes.py'' para generar este archivo.")
        return

    print(f"Leyendo la lista de genes comunes desde ''{common_genes_path}''...")
    genes = read_gene_list(common_genes_path)
    print(f"Se encontraron {len(genes)} genes comunes para el análisis.")

    if not genes:
        print("La lista de genes comunes está vacía. No se puede realizar el análisis de enriquecimiento.")
        return

    # Gene sets to query for enrichment
    # KEGG is for pathways, GO has three different aspects
    gene_sets = [
        'KEGG_2021_Human',
        'GO_Biological_Process_2023',
        'GO_Molecular_Function_2023',
        'GO_Cellular_Component_2023'
    ]

    print("\n--- Realizando Análisis de Enriquecimiento de Rutas (GO & KEGG) ---")
    print("Esto puede tardar uno o dos minutos, dependiendo de la conexión a internet...")

    try:
        enr = gp.enrichr(gene_list=genes,
                         gene_sets=gene_sets,
                         organism='Human',
                         outdir=None,
                         cutoff=0.05)
    except Exception as e:
        print(f"\nERROR: Ocurrió un error durante el análisis de enriquecimiento: {e}")
        print("Esto puede deberse a un problema de red o a que el servicio Enrichr no está disponible.")
        return

    if enr and hasattr(enr, 'results') and not enr.results.empty:
        print("\nAnálisis de enriquecimiento completado.")
        
        results_df = enr.results
        results_df = results_df.sort_values(by='P-value', ascending=True)
        
        output_path = os.path.join(results_dir, 'pathway_enrichment_results.csv')
        results_df.to_csv(output_path, index=False)
        
        print(f"\nLos resultados completos del análisis de rutas han sido guardados en: ''{output_path}''")
        
        print("\n--- Top 10 Rutas y Procesos Biológicos Más Significativos ---")
        print(results_df.head(10).to_string())
    else:
        print("\nNo se encontraron rutas de señalización o procesos biológicos significativamente enriquecidos para la lista de genes comunes.")

if __name__ == "__main__":
    main()
