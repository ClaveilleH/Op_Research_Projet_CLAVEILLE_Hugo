#!/bin/bash

# Vérifie qu'un argument est fourni
if [ -z "$1" ]; then
  echo "Usage: $0 <nom_du_fichier_sans_extension>"
  exit 1
fi

FILENAME=$1

# Génération et ouverture de l'image
dot -Tjpg "output/${FILENAME}.dot" -o "output/img/${FILENAME}.jpg" && \
xdg-open "output/img/${FILENAME}.jpg"