#! /bin/sh

## Actualizando desde repositorio
cd "/home/jsalmoralp/Proyectos/Python-DiscordBot-Apuntes"
git pull

## Instalando proyecto
cd "/home/jsalmoralp/Proyectos/Python-DiscordBot-Apuntes/Apuntes DiscordBot"
pipenv install

## Abriendo entorno virtual y ejecutando archivo principal del proyecto
pipenv shell | python3.9 src/index.py