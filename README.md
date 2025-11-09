# Análisis de Dianas Comunes de miRNAs y Rutas de Señalización

## 1. Resumen del Proyecto

Este proyecto realiza un análisis bioinformático para identificar **genes diana comunes** a un conjunto de 5 microARNs (miRNAs) y, posteriormente, determinar las **rutas de señalización y procesos biológicos** en los que estos genes comunes están involucrados.

El flujo de trabajo está automatizado mediante scripts de Python, garantizando la reproducibilidad y eficiencia del análisis, desde la obtención de los datos hasta la interpretación biológica de los resultados.

---

## 2. Metodología

### Obtención de Datos

Las listas de genes diana para cada uno de los 5 miRNAs se obtuvieron de la base de datos **TargetScanHuman 8.0**. Esta base de datos proporciona predicciones de dianas de miRNAs basadas en la conservación de la secuencia y otros parámetros.

-   **Fuente de Datos:** [TargetScanHuman - v8.0](https://www.targetscan.org/vert_80/)
-   **miRNAs Analizados:**
    -   `hsa-miR-106b-5p`
    -   `hsa-miR-144-3p`
    -   `hsa-miR-33a-5p`
    -   `hsa-miR-33b-5p`
    -   `hsa-miR-758-3p`

*Nota: Se asumió que las dianas de `hsa-miR-33a-5p` son equivalentes a las de `hsa-miR-33b-5p` debido a que pertenecen a la misma familia, para resolver una discrepancia en los datos iniciales.*

### Flujo de Trabajo del Análisis

El proyecto sigue un flujo de trabajo automatizado de dos pasos, como se ilustra en el siguiente diagrama:

```mermaid
graph TD;
    A[<B>Paso 1: Obtención de Datos</B><br>5 Listas de Genes de TargetScan] --> B{<B>Script 1:</B><br>01_find_common_genes.py};
    B -- <B>Calcula la intersección</B> --> C[<B>Resultado 1:</B><br>common_genes.txt<br>(5 genes comunes)];
    C --> D{<B>Script 2:</B><br>02_pathway_analysis.py};
    D -- <B>Análisis de Enriquecimiento<br>(GO & KEGG)</B> --> E[<B>Resultado 2:</B><br>pathway_enrichment_results.csv];
```

---

## 3. Estructura del Repositorio

```
.
├── 📁 data/
│   └── 📁 raw/
│       ├── 📄 hsa-miR-106b-5p.txt
│       ├── 📄 hsa-miR-144-3p.txt
│       ├── 📄 hsa-miR-33a-5p.txt
│       ├── 📄 hsa-miR-33b-5p.txt
│       └── 📄 hsa-miR-758-3p.txt
├── 📁 notebooks/
│   └── (Aquí se pueden añadir Jupyter Notebooks para análisis exploratorio)
├── 📁 results/
│   ├── 📄 common_genes.txt
│   └── 📄 pathway_enrichment_results.csv
├── 📁 scripts/
│   ├── 🐍 01_find_common_genes.py
│   └── 🐍 02_pathway_analysis.py
├── 📄 .gitignore
└── 📖 README.md
```

---

## 4. Instrucciones de Uso

### Prerrequisitos

-   Python 3.x
-   Las librerías de Python `pandas` y `gseapy`. Se pueden instalar con el siguiente comando:
    ```bash
    pip install pandas gseapy
    ```

### Pasos para la Ejecución

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/abrangel/analisis-rna-seq.git
    cd analisis-rna-seq
    ```

2.  **Ejecutar el Flujo de Análisis Completo:**
    -   Navega a la carpeta `scripts` y ejecuta los scripts en orden:
        ```bash
        cd scripts
        python 01_find_common_genes.py
        python 02_pathway_analysis.py
        ```

3.  **Analizar los Resultados:**
    -   Los archivos finales se encuentran en la carpeta `results`. Puedes abrirlos con un editor de texto o un programa de hojas de cálculo.
