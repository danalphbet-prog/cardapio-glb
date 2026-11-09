#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parent
models=root/'models'
items=[{'file':p.relative_to(models).as_posix(),'bytes':p.stat().st_size} for p in sorted(models.rglob('*')) if p.is_file() and p.suffix.lower()=='.glb']
(root/'catalogo.json').write_text(json.dumps({'models':items},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Catálogo atualizado: {len(items)} modelo(s)')
