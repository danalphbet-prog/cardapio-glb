# Biblioteca GLB para GitHub Pages

Copie arquivos de `/sdcard/models/` para `models/`, execute `python3 atualizar_catalogo.py` e faça `git push`.

A página `index.html` oferece busca, visualização 3D, controles de órbita, cópia de links e estatísticas de malhas, triângulos, vértices, materiais e texturas.

Os dados são estimativas calculadas no navegador. A contagem de triângulos soma geometrias únicas e não multiplica instâncias. Texturas são contadas como objetos carregados, não como arquivos externos.

Requer conexão com internet para carregar Three.js via CDN. O site usa HTTPS do GitHub Pages.
