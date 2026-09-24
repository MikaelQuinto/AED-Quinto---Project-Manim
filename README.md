# Proyecto 1 - Animando Estructuras de Datos

Visualización de algoritmos y estructuras de datos con Manim Community.

## Requisitos

- Python 3.13 (recomendado para contar con binarios precompilados en Windows)
- Git

Manim y sus demás dependencias se instalan dentro de un entorno virtual local.

## Configuración en Windows

Desde PowerShell, en la raíz del repositorio:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En VS Code, selecciona `.venv\Scripts\python.exe` mediante el comando
`Python: Select Interpreter`. El repositorio también incluye tareas de VS Code
para renderizar la escena con calidad de prueba o calidad final.

## Ejecutar la escena de prueba

Con el entorno virtual activado:

```powershell
manim -pql scenes\intro.py EscenaInicial
```

`-ql` produce un render rápido de baja calidad para trabajar. Para generar la
versión final en alta calidad, usa:

```powershell
manim -pqh scenes\intro.py EscenaInicial
```

Los videos generados quedan en `media/`, una carpeta que Git ignora porque se
puede regenerar desde el código fuente.

## Estructura

```text
assets/       Recursos usados por las animaciones
scenes/       Escenas escritas con Manim
media/        Videos e imágenes generados (no se suben a Git)
```
