# ⚙️ Python Automation Scripts

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

## 📋 Descripción

Colección de scripts de automatización en Python para tareas DevOps y de infraestructura.

## ✨ Características

- 🔄 **Automatización de Tareas**: Scripts reutilizables para operaciones comunes
- 🐳 **Docker Ready**: Ejecuta scripts en contenedores aislados
- 📊 **Logging**: Logging estructurado con rotación de archivos
- ⚙️ **Configurable**: Totalmente configurable via variables de entorno
- 🔒 **Security**: Escaneo automático de vulnerabilidades con Grype
- 📈 **CI/CD**: GitHub Actions para linting, testing y security scanning

## 🚀 Instalación

### Local

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar
cp .env.example .env
```

### Con Docker

```bash
docker build -t python-automation .
docker run --env-file .env python-automation
```

## 📁 Estructura del Proyecto

```
python-automation/
├── main.py              # Punto de entrada
├── requirements.txt
├── .env.example
├── .dockerignore
├── Dockerfile
├── docker-compose.yaml
├── health_check.py
├── setup.sh
└── test_api.py          # Tests de la API/scripting
```

## 🚀 Uso

```bash
# Ejecutar todos los scripts de automatización
python main.py

# Ejecutar script específico
python main.py --task NombreTarea

# Ver ayuda
python main.py --help
```

### Tareas Disponibles

| Tarea | Descripción |
|-------|-------------|
| `cleanup` | Limpia archivos temporales y logs antiguos |
| `backup` | Crea backups de archivos importantes |
| `report` | Genera reporte de estado del sistema |
| `healthcheck` | Ejecuta health checks de servicios |

## 🧪 Testing

```bash
pytest test_api.py -v
```

## 🤝 Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md).

## 📝 Licencia

MIT - vea [LICENSE](LICENSE)
