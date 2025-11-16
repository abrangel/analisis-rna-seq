# Análisis de Dianas Comunes de miRNAs y Rutas de Señalización

## Integrantes
- Alanis Rafaela Jarre Moreano  
- Claudia Melissa Alvarado Cantos  
- Andrés Darío Ñauñay Puente  
- Cesar Abrahan Manzo Carvajal  
- Ana Belén Mejía Pérez  

## 1. Objetivo del Proyecto

Realizar un análisis bioinformático para identificar **genes diana comunes** a un conjunto de 5 microARNs (miRNAs) y, posteriormente, determinar las **rutas de señalización y procesos biológicos** en los que estos genes comunes están involucrados.

El flujo de trabajo está automatizado mediante scripts de Python, garantizando la reproducibilidad y eficiencia del análisis, desde la obtención de los datos hasta la interpretación biológica de los resultados.
## 1.1 Proposito del Proyecto
Caracterizar la función molecular de cada uno de los cinco genes comunes para identificar sus roles en procesos biológicos fundamentales.

Determinar los pathways (rutas metabólicas o de señalización) enriquecidos en el conjunto de genes compartidos por los miRNAs.

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

#### Guía paso a paso para la obtención de datos en TargetScan

Para replicar la obtención de datos manuales originales, se siguieron estos pasos en la plataforma TargetScan:

1.  **Búsqueda del miRNA:** Seleccionar la especie "Human" e ingresar el nombre del microARN deseado (por ejemplo, `hsa-miR-33-5p`) en el campo de búsqueda correspondiente.
    ![Búsqueda de miRNA en TargetScan] <img width="880" height="538" alt="image" src="https://github.com/user-attachments/assets/81aebb00-bc17-4bef-bd66-962230a77b1f" />

2.  **Acceso a la Tabla de Resultados:** Una vez generada la lista de transcritos predichos, localizar el enlace **[Download table]** situado sobre la tabla de resultados a la derecha.
    ![Ubicación del enlace de descarga] <img width="882" height="214" alt="image" src="https://github.com/user-attachments/assets/db43e59b-2e23-4cb1-af3f-a164d6ea3f99" />

3.  **Descarga del Archivo:** Al hacer clic, se abrirán las opciones de descarga. Se selecciona el formato de texto (`.txt`) para su posterior procesamiento en los scripts de análisis.
    ![Opciones de descarga de dianas]<img width="333" height="47" alt="image" src="https://github.com/user-attachments/assets/5a34973e-cc34-43bb-bef5-14f4d528d201" />
9.png)

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
│   ├── 📄 ABCA1 Pathway.png
│   ├── 📄 KPNA3 Pathway.png
│   ├── 📄 SCNA1 Pathway.png
│   ├── 📄 SNTB2 Pathway.png
│   ├── 📄 common_genes.txt
│   ├── 📄 go_network_plot.png
│   ├── 📄 pathway_enrichment_results.csv
│   └── 📄 venn_result19894.png
├── 📁 scripts/
│   ├── 🐍 01_find_common_genes.py
│   └── 🐍 02_pathway_analysis.py
├── 📄 .gitignore
└── 📖 README.md
```

---

## 4. Instrucciones de Uso
### Pre-requisitos
#### Instalar git, use el siguiente comando:
1.  **instalar git:**
    ```bash
    winget install --id Git.Git -e --source winget
    ```

#### Python 3.x
#### Las librerías de Python `pandas` y `gseapy`. Se pueden instalar con el siguiente comando:
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
  
## 5. Verificación de 5 genes en comun con Venn
<img width="300" height="400" alt="image" src="https://github.com/abrangel/analisis-rna-seq/blob/main/results/venn_result19894.png" />

### Análisis de verificación de los 5 genes en común
#### ABCA1
        Destaca en el presente caso clínico. Al utilizar ATP genera la translocación de fosfolípidos desde la monocapa citoplasmática a la extracelular de la membrana, de este modo participa en la transferencia de fosfolípidos a las apolipoproteínas para formar lipoproteínas de alta densidad (HDL). Además, podría participar en la liberación de colesterol intracelular hacia las apolipoproteínas.
#### KPNA3 
        Participa en la importación de proteínas nucleares como proteína adaptadora del receptor nuclear KPNB1.
#### SCN1A
        Regula la permeabilidad de los iones sodio dependiente del voltaje en membranas excitables, que adoptan conformaciones abiertas o cerradas, en respuesta al voltaje. 
#### TSC22D2 
        Se encarga de la represión de la transcripción de la ciclina CCND1 y la reducción del crecimiento celular. 
#### SNTB2
        Puede conectar varios receptores al citoesqueleto y al complejo de glicoproteínas de distrofina, incluso podría mediante su interacción con PTPRN desempeñar un papel en la regulación de gránulos secretores.

### Lista de genes/proteínas de humano y realiza el análisis de anotación seleccionando:

#### Gene Ontology (GO) biological process.
<p align="center">
  <img src="https://raw.githubusercontent.com/abrangel/analisis-rna-seq/refs/heads/main/results/GO_BP.png" width="600">
</p>

El análisis de enriquecimiento basado en ontología génica (GO BP) mostró que los genes identificados se agrupan en procesos biológicos diferenciados. ABCA1 se encuentra asociado principalmente con rutas relacionadas con el metabolismo y transporte de lipoproteínas, incluyendo regulación de la formación de partículas de lipoproteína de alta densidad (HDL), señalización mediada por apolipoproteína A-I, secreción de péptidos, metabolismo de esfingolípidos y respuesta a vitamina B3. SCN1A aparece vinculado a procesos de señalización neuronal, mientras que KPNA3 se asocia con mecanismos celulares implicados en la penetración viral al núcleo del huésped. La distribución de los términos indica que ABCA1 concentra la mayor parte de las anotaciones funcionales, sugiriendo un papel central en el metabolismo lipídico y la homeostasis celular, mientras que los otros genes participan en funciones más específicas y no solapadas.

#### Kyoto Encyclopedia of Genes and Genomes (KEGG) pathways.

<p align="center">
  <img src="https://raw.githubusercontent.com/abrangel/analisis-rna-seq/refs/heads/main/results/KEGG.png" width="600">
</p>

El análisis de enriquecimiento funcional realizado en GeneCodis utilizando la base de datos KEGG mostró que cada uno de los genes identificados se asocia de manera específica a una única vía biológica. ABCA1 se vincula principalmente con rutas relacionadas con el metabolismo lipídico, incluyendo metabolismo del colesterol, transportadores ABC y digestión de lípidos. KPNA3 se asocia con el transporte núcleo-citoplasma, SCN1A con la sinapsis dopaminérgica y SNTB2 con patologías cardiacas como miocarditis viral y distintas formas de cardiomiopatía. Esto indica que los genes analizados participan en procesos biológicos distintos, sin solapamiento entre rutas, lo que sugiere funciones especializadas dentro del contexto molecular evaluado.

#### Reactome

<p align="center">
  <img src="https://raw.githubusercontent.com/abrangel/analisis-rna-seq/refs/heads/main/results/Reactome.png" width="600">
</p>

El análisis de enriquecimiento funcional basado en Reactome mostró que el gen ABCA1 se asocia con múltiples rutas relacionadas con el metabolismo y transporte de colesterol, incluyendo ensamblaje de HDL, señalización mediada por NR1H2/NR1H3, desórdenes de transportadores ABC y el fenotipo patológico causado por mutaciones en ABCA1. SCN1A se relaciona con procesos eléctricos celulares, particularmente con la fase 0 de despolarización rápida y la interacción entre moléculas L1 y anquirinas, lo que sugiere un papel en la excitabilidad neuronal. Por su parte, KPNA3 se vincula con mecanismos antivirales mediados por ISG15 y con la modulación de rutas celulares inducida por proteínas virales como NS1. En conjunto, los resultados indican que los genes analizados participan en rutas Reactome funcionalmente distintas, destacando el papel central de ABCA1 en el metabolismo lipídico, mientras que SCN1A y KPNA3 se asocian a procesos específicos de excitabilidad celular y respuesta antiviral, respectivamente.
## Pathways
### Metabolismo del Colesterol
<img width="600" height="400" alt="image" src="https://github.com/abrangel/analisis-rna-seq/blob/main/results/ABCA1%20Pathway.png" />

#### ABCA1 (ATP-Binding Cassette Subfamily A Member 1)
    Actúa como un transportador de eflujo de colesterol y fosfolípidos. En los tejidos periféricos y hepatocitos, bombea colesterol libre (FC) y fosfolípidos hacia afuera de la célula para cargarlos en ApoA-I no lipidada, iniciando la formación de HDL naciente. Este proceso es fundamental para el transporte inverso del colesterol (eliminar el exceso de colesterol de los tejidos).
    
### Cardiomiopatía Ventricular Derecha Arritmogénica
<img width="600" height="400" alt="image" src="https://github.com/abrangel/analisis-rna-seq/blob/main/results/SNTB2%20Pathway.png" />

#### SNTB2 (Beta-2-Sarcoglicano)	
    Forma parte del complejo de la sarcoglicana (junto con SGCA, SGCB, y SGCD), que a su vez se integra en el complejo de la distrofina-glicoproteína. Este complejo es crucial para anclar el citoesqueleto de actina (sarcomero) a la matriz extracelular (ECM) a través de la laminina, asegurando la integridad estructural de la célula muscular cardíaca.
    
### Transporte Nucleocitoplasmático
<img width="600" height="400" alt="image" src="https://github.com/abrangel/analisis-rna-seq/blob/main/results/KPNA3%20Pathway.png" />

#### KPNA3 (Importina-alfa 3)	
    Es una proteína adaptadora de importación nuclear (miembro de la familia de las carioferinas o importinas). Reconoce y se une a la Secuencia de Localización Nuclear (NLS) de las proteínas que deben ingresar al núcleo. Luego, se asocia con una importina-beta (como KPNB1/Importin) para ser transportada a través del NPC hacia el núcleo.
    
### Sinapsis Dopaminérgica
<img width="600" height="400" alt="image" src="https://github.com/abrangel/analisis-rna-seq/blob/main/results/SCN1A%20Pathway.png" />

#### SCN1A (Canal de Sodio dependiente de voltaje, Subunidad alfa 1)
    Codifica la subunidad alfa del canal de sodio, un canal iónico crucial para la generación y propagación del potencial de acción en las neuronas. Aunque no está directamente en el ciclo de la dopamina, estos canales son vitales para la excitabilidad neuronal. En la vía se muestra que su actividad regula la excitabilidad que puede modular la liberación o respuesta en la sinapsis, afectando indirectamente la señalización dopaminérgica.
    
#### Gen TSC22D2 
    TSC22D2 es un factor de transcripción putativo y se ha demostrado que es un regulador de crecimiento celular negativo. Su mecanismo de acción principal conocido es la interacción con la enzima glucolítica PKM2 (Pyruvate Kinase Isoform M2) y la subsiguiente represión de la transcripción de Ciclina D1. Aunque no figura como un componente de una vía enzimática o de señalización clásica, su papel como regulador maestro en el control del ciclo celular y la proliferación lo convierte en un gen de alta relevancia biológica.

