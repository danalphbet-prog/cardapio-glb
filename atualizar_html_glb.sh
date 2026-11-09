#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$HOME/cardapio-glb" || exit 1
cp /sdcard/Download/index_glb_visualizador_v3.html index.html
printf '\nInterface atualizada localmente.\n'
git add index.html
git commit -m "Atualizar HTML com visualizador 3D" || true
git push origin main
echo "Verifique o workflow: gh run list --limit 5"
