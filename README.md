# Juridex AI — Analyse automatique de contrats (FastAPI + Gemini + OCR)

LexiScan est un micro-service d’analyse automatique de documents PDF avec :
- OCR avancé (pdf2image + Tesseract)
- Extraction intelligente basée sur Gemini (Google AI)
- API FastAPI professionnelle
- Déploiement 100% gratuit sur Render

## 🚀 Fonctionnalités
- Upload d’un PDF
- OCR automatique
- Extraction :
  - Titre
  - Date
  - Parties
  - Obligations
  - Risques
- JSON normalisé validé par Pydantic

## 🛠️ Technologies utilisées
- FastAPI
- Python 3.11
- Google Gemini API
- Tesseract OCR
- Render (déploiement gratuit)

## 📦 Installation locale

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
