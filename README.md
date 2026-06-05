# Sistem Pendukung Keputusan Penerimaan Universitas

Repositori ini berisi analisis eksplorasi data (EDA), contoh dashboard Streamlit, dan skrip bantu untuk pra-pemrosesan serta pemodelan data penerimaan.

## Panduan cepat

1. Buat dan aktifkan virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. (Opsional) Pasang kernel IPython agar Jupyter mengenali environment ini:

```powershell
python -m ipykernel install --user --name university-admission-dss --display-name "Python (University Admission DSS)"
```

## Notebook

- Buka dan jalankan [notebooks/01_eda.ipynb](notebooks/01_eda.ipynb).
- Notebook menggunakan `pathlib` untuk menemukan `data/raw/MBA.csv`. Pastikan file CSV berada di `data/raw/`.
- Untuk menyimpan hasil EDA, notebook akan menulis ke `data/processed/` (folder dibuat otomatis jika belum ada). Perhatikan bahwa `data/processed/` diabaikan oleh Git secara default.

Contoh potongan kode untuk menyimpan hasil di notebook:

```python
from pathlib import Path
out_dir = Path.cwd() / "data" / "processed"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "eda_output.csv"
df.to_csv(out_path, index=False)
print(f"EDA dataset saved to {out_path}")
```

## Dashboard (Streamlit)

Folder `dashboard/` berisi aplikasi Streamlit sederhana. Jalankan lokal dengan:

```powershell
pip install streamlit
streamlit run dashboard/Main.py
```

## Struktur proyek

- `data/raw/` — data sumber (dikomit)
- `data/processed/` — data hasil olahan (diabaikan oleh Git)
- `data/sample_inputs/` — contoh input
- `models/` — artefak model terlatih
- `notebooks/` — notebook Jupyter (analisis & eksperimen)
- `reports/` — gambar dan laporan hasil ekspor
- `src/` — modul dan skrip yang dapat digunakan ulang
- `dashboard/` — aplikasi Streamlit dan asetnya

## Penanganan data dan Git

- Secara default `.gitignore` mengecualikan `data/processed/*` agar file hasil olahan tidak dikomit.
- Jika Anda benar-benar ingin melacak file tertentu di `data/processed/`, ubah `.gitignore` atau tambahkan pengecualian seperti `!data/processed/eda_output.csv` (tidak disarankan untuk file besar).

## Dependensi

Daftar dependensi utama ada di `requirements.txt`. Paket penting antara lain:

- `pandas`, `numpy` — manipulasi data
- `matplotlib`, `seaborn`, `plotly` — visualisasi
- `scikit-learn` — pemodelan
- `jupyter`, `ipykernel` — notebook
- `streamlit` — runtime dashboard (opsional)
