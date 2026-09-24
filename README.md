# Proyecto 1 - Animando Árbol Binario de Búsqueda con Manim

Animación paso a paso de un árbol binario de búsqueda (BST) hecha con [Manim Community](https://docs.manim.community/).

- **Autor:** Mikael Quinto Ramos
- **Video:** [ver video](https://drive.google.com/drive/folders/1bxBfLRXfsJxnfUJLOstIfWPSkt13iab9?usp=sharing)

## Requisitos

- Python 3.13
- Git

## Instalación (Windows, PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecución

**Desde VS Code (opción más simple):** abre la carpeta del repositorio en VS Code, presiona `Ctrl+Shift+P`, elige `Tasks: Run Task` y selecciona `Manim: render final` (calidad alta) o `Manim: render rápido` (vista previa rápida).

**Desde la terminal** (con el entorno virtual activado):

```powershell
manim -pqh scenes\binary_search_tree.py
```

Usa `-pql` para una vista previa rápida. El video queda en `media/`.
