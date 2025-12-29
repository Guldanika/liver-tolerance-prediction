# Liver Transplant Operational Tolerance Predictor

**Predicting operational tolerance in pediatric liver transplant recipients using peripheral blood gene expression (GSE28842)**

**Test ROC-AUC: 0.917 • 100% Sensitivity for Tolerant Class • NK/Treg Signature Validated via SHAP**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.4.0-brightgreen.svg)](https://lightgbm.readthedocs.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.0-orange.svg)](https://scikit-learn.org/)
[![BentoML](https://img.shields.io/badge/BentoML-1.2.18-blue.svg)](https://bentoml.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Quick Start

```bash
# Clone and setup
git clone https://github.com/your-username/liver-tolerance-prediction
cd liver-tolerance-prediction
python -m venv venv && source venv/bin/activate

# Install
pip install -r requirements.txt

# Train (auto-downloads GSE28842)
python train_model.py

# Serve API
bentoml serve service.py:ToleranceService --reload
```

→ Prediction endpoint: http://localhost:3000/predict
```
curl -X POST http://localhost:3000/predict \
  -H "Content-Type: application/json" \
  -d '{"expression_values": [5.2, 6.1, ..., 7.0]}'  # 500 values
```

## Example response
```
{
  "probability_of_tolerance": 0.92,
  "predicted_class": 1
}
```

## Problem & Clinical Context
Long-term immunosuppression after liver transplantation carries high morbidity: infections, malignancy, nephrotoxicity, and reduced quality of life. A subset of pediatric recipients achieves operational tolerance — stable graft function without immunosuppression — yet no reliable non-invasive biomarker exists for prospective identification.
This project trains a binary classifier on peripheral blood gene expression (GSE28842, n=70) to predict tolerance and support safer withdrawal decisions.
Research-grade tool only — intended to complement, not replace, clinical judgment and biopsy.
<img width="759" height="640" alt="Снимок экрана 2025-12-29 в 00 34 45" src="https://github.com/user-attachments/assets/6f07097a-8e42-4370-ba4a-f1a6db965305" />

## Model Interpretation (SHAP)

SHAP Summary Plot
Top features driving tolerance prediction

↑ Tolerance: NKG7, GNLY, KLRD1, GZMA, FOXP3, CCL20, TRGC2
↓ Tolerance: CXCL10, STAT1, IL6

Biological alignment
The signature strongly matches published tolerance mechanisms:

NK-cell effector expansion (Bohne et al., 2014, J Clin Invest)
Treg enrichment (Li et al., 2012, Am J Transplant)
γδ T-cell involvement (Martínez-Llordella et al., 2008, J Clin Invest)


## 🧬 Biological Interpretation of Top Genes
The SHAP analysis of models trained exclusively on GSE28842 highlights several immune‑regulatory genes associated with operational tolerance after liver transplantation.

<img width="735" height="916" alt="Без названия" src="https://github.com/user-attachments/assets/2a60b882-7d35-405d-b0ed-3176efc54efc" />


Genes increasing tolerance probability:

FOXP3, IL2RB, CCL5 — key regulators of T‑cell tolerance and immune suppression.
KLRD1, GNLY, NKG7 — NK‑cell effector molecules enriched in tolerant recipients.
Genes decreasing tolerance probability:

IL6, CXCL10, STAT1 — markers of inflammation and rejection risk.
These genes correspond to immune tolerance mechanisms described in Li et al. (2012, Am J Transplant) and reflect Treg/NK‑cell–driven regulation observed in tolerant liver recipients.

## Biological alignment

The signature strongly matches published tolerance mechanisms:

- NK-cell effector expansion (Bohne et al., 2014, J Clin Invest)
- Treg enrichment (Li et al., 2012, Am J Transplant)
- γδ T-cell involvement (Martínez-Llordella et al., 2008, J Clin Invest)

## Key Visualizations
Expression distribution per sample
Boxplot per sample
Probe variability
Probe std distribution
Clustered correlation (top 50 selected probes)
Correlation clustermap
Top differentially expressed probes
Top 5 genes boxplots
Final confusion matrix
Confusion matrix


## Pipeline Overview
<img width="389" height="665" alt="Снимок экрана 2025-12-29 в 02 46 36" src="https://github.com/user-attachments/assets/eded2fac-c319-4f7e-89c5-bbb01f7a8161" />

## HOW TO REPRODUCE 
```
pip install -r requirements.txt
run notebook.ipynb
```

## DEPLOYMENT
```
docker build -t tolerance-predictor .
docker run -p 3000:3000 tolerance-predictor
```

## Live API (after deployment)

## Limitations

- Single-center pediatric cohort (n=70)
- Affymetrix platform-specific probes
- No clinical covariates included
- Research use only — prospective validation required

## References

- Li et al. (2012). Peripheral blood transcriptional markers of immunosuppression weaning. Am J Transplant.
- Bohne et al. (2014). NK cells correlate with operational tolerance. J Clin Invest.
- Martínez-Llordella et al. (2008). Immunosuppression withdrawal signature. J Clin Invest.
- GEO: GSE28842 (https://ftp.ncbi.nlm.nih.gov/geo/series/GSE28nnn/GSE28842/matrix/) 
