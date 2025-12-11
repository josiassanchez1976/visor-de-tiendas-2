"""Manejo de la memoria de tiendas guardadas."""

import json
import subprocess


def cargar_memoria():
    """Load saved shops from disk if the file exists."""

    try:
        with open("memoria.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_memoria(memoria):
    with open("memoria.json", "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=2)


def ya_existe(tienda, memoria):
    for t in memoria:
        misma_direccion = (
            t["Dirección"].strip().lower()
            == tienda["Dirección"].strip().lower()
        )
        if misma_direccion:
            return comparar_nombres(t["Nombre"], tienda["Nombre"])
    return False


def comparar_nombres(n1, n2):
    prompt = (
        "¿Los siguientes nombres son el mismo negocio? Nombre 1: "
        f"{n1} Nombre 2: {n2}. Responde solo sí o no."
    )
    try:
        res = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True,
            timeout=25,
        )
        return "sí" in res.stdout.lower() or "yes" in res.stdout.lower()
    except (subprocess.SubprocessError, FileNotFoundError):
        return False
