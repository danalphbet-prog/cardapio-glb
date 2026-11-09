# Biblioteca GLB para cardápio AR

Site estático para publicar modelos `.glb` e copiar URLs HTTPS pelo GitHub Pages.

## Publicação

1. Copie seus `.glb` para `models/` (evite espaços e acentos nos nomes).
2. Rode `python3 atualizar_catalogo.py`.
3. Envie as alterações para a branch `main`.
4. No GitHub, abra **Settings > Pages > Build and deployment > Source > GitHub Actions**.
5. Aguarde o workflow **Publicar GLB no GitHub Pages** ficar verde.

URL típica: `https://SEU_USUARIO.github.io/cardapio-glb/models/prato.glb`

O repositório é público; qualquer pessoa com o link pode baixar os modelos.

### Atualizações no Termux

```sh
cd ~/cardapio-glb
cp /sdcard/Download/*.glb models/  # caso seus arquivos estejam nessa pasta
python3 atualizar_catalogo.py
git add models catalogo.json
git commit -m 'Adicionar modelos 3D'
git push
```

**Não use Git LFS:** arquivos LFS não são servidos diretamente pelo GitHub Pages. Evite arquivos acima de 100 MiB. O GitHub Pages não é indicado como hospedagem de ativos de um SaaS comercial. Consulte os limites e termos oficiais.
