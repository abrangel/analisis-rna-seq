# Análisis de Dianas Comunes de miRNAs y Rutas de Señalización

## 1. Resumen del Proyecto

Este proyecto realiza un análisis bioinformático para identificar **genes diana comunes** a un conjunto de 5 microARNs (miRNAs) y, posteriormente, determinar las **rutas de señalización y procesos biológicos** en los que estos genes comunes están involucrados.

El flujo de trabajo está automatizado mediante scripts de Python, garantizando la reproducibilidad y eficiencia del análisis.

---

## 2. Flujo de Trabajo del Análisis

El proyecto se divide en dos etapas principales:

1.  **Identificación de Genes Comunes:**
    -   El script `01_find_common_genes.py` lee las listas de genes diana predichos para cada uno de los 5 miRNAs.
    -   Calcula la **intersección** de todas las listas para encontrar aquellos genes que son regulados por todos los miRNAs simultáneamente.
    -   El resultado es una lista limpia de genes comunes que se guarda en `results/common_genes.txt`.

2.  **Análisis de Enriquecimiento de Rutas:**
    -   El script `02_pathway_analysis.py` toma la lista de genes comunes generada en el paso anterior.
    -   Se conecta a bases de datos públicas (a través de la API de Enrichr) para realizar un **análisis de enriquecimiento funcional**.
    -   Identifica si los genes comunes están sobrerrepresentados en rutas de señalización **KEGG** o en términos de **Gene Ontology (GO)**.
    -   El resultado es una tabla con las rutas y funciones más significativas, que se guarda en `results/pathway_enrichment_results.csv`.

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

1.  **Completar los Datos:** Asegúrate de que los 5 archivos `.txt` en la carpeta `data/raw/` contienen las listas de genes correctas. Especialmente, rellena el archivo `hsa-miR-106b-5p.txt` si está vacío.

2.  **Ejecutar el Script 1 (Encontrar Genes Comunes):**
    -   Abre una terminal y navega a la carpeta `scripts`.
    -   Ejecuta el siguiente comando:
        ```bash
        python 01_find_common_genes.py
        ```
    -   Verifica que el archivo `results/common_genes.txt` se ha creado.

3.  **Ejecutar el Script 2 (Análisis de Rutas):**
    -   En la misma terminal, ejecuta el segundo script:
        ```bash
        python 02_pathway_analysis.py
        ```
    -   Verifica que el archivo `results/pathway_enrichment_results.csv` se ha creado.

4.  **Analizar los Resultados:**
    -   Abre los archivos generados en la carpeta `results` para ver los genes comunes y las rutas de señalización enriquecidas.
