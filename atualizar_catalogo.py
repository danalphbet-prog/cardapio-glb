#!/usr/bin/env python3
import json
from pathlib import Path
base=Path(__file__).resolve().parent
files=sorted((base/"models").glob("*.glb"),key=lambda p:p.name.lower())
data=[{"name":p.name,"url":"models/"+p.name,"bytes":p.stat().st_size} for p in files]
(base/"catalogo.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Catálogo atualizado: {len(data)} modelos")
