# NeuroDrug-Discovery
# NeuroDrug-Discovery: In Silico Design of Novel Therapeutics 💊🧠

## 🟢 Project Status: Active / Phase 2 (Structural Modeling)

### 🎯 Target Identification
*   **Organism:** *Acinetobacter baumannii* (MDR-TJ Strain)
*   **Target Protein ID:** `WP_001256719.1`
*   **Annotation:** Hypothetical Protein (Unknown Function)
*   **Discovery Method:** Subtractive Genomics (Non-homologous to Human/Gut Flora).

### 📊 Module 1: Physicochemical & Evolutionary Characterization
We have successfully isolated a promising drug target. The initial characterization reveals:

#### 1. Physical Properties
*   **Molecular Weight:** 13,138.29 Da (Small size, druggable).
*   **Isoelectric Point (pI):** 9.10 (Basic/Cationic).
*   **GRAVY Index:** -0.60 (Hydrophilic/Soluble).
    *   *Interpretation:* The protein is likely cytoplasmic. Its high pI suggests positive surface charge, potentially aiding interaction with negatively charged bacterial membranes.

#### 2. Evolutionary Analysis (Phylogeny)
*   **Specificity:** The phylogenetic tree (FastTree/MAFFT) confirms the protein is **exclusive to the *Acinetobacter* genus**.
*   **Safety:** No close homologs were found in *Homo sapiens* or common gut microbiota (*E. coli*, etc.), suggesting low toxicity risk.

#### 3. Domain Scanning (InterProScan/CDD)
*   **Result:** ⚠️ **NO CONSERVED DOMAINS FOUND.**
*   **Significance:** The protein represents a **structurally novel target**. It lacks known functional motifs, classifying it as "biological dark matter."

### 🛠 Tools & Tech Stack
*   **Language:** Python 3.9 (Biopython, Pandas)
*   **Environment:** Conda (Mamba)
*   **Bioinformatics:** 
    *   NCBI BLAST+ (Remote API)
    *   MAFFT (Alignment)
    *   FastTree (Phylogenetics)
    *   InterProScan (Domain Search)
    *   ESMFold (3D Structure Prediction)

---
*Repository maintained by EsnaulAI. 2024.*