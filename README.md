# ⚙️ Python Automation Scripts

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

## 📋 Descripción

Colección de scripts de automatización en Python para tareas DevOps e infraestructura.

## ✨ Características

- 🔄 **Automatización de Tareas**: Scripts reutilizables para operaciones comunes
- 🐳 **Docker Ready**: Ejecuta scripts en contenedores aislados
- 📊 **Logging**: Logging estructurado con rotación de archivos
- ⚙️ **Configurable**: Totalmente configurable via variables de entorno
- 🔒 **Security**: Escaneo de vulnerabilidades con pip-audit
- 🧪 **Testing**: Suite de tests con pytest

## 🚀 Instalación

### Local

```bash
# Clonar el repositorio
git clone https://github.com/alexkore12/python-automation-20260323.git
cd python-automation-20260323

# Ejecutar setup
chmod +x setup.sh
./setup.sh

# O manual:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Con Docker

```bash
docker build -t python-automation .
docker run --env-file .env python-automation
```

### Con Docker Compose

```bash
docker-compose up -d
```

## 📁 Estructura del Proyecto

```
python-automation/
├── main.py              # Punto de entrada principal
├── requirements.txt     # Dependencias Python
├── .env.example         # Plantilla de variables de entorno
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── health_check.py      # Script de verificación de salud
├── setup.sh             # Script de inicialización
├── test_api.py          # Suite de tests
├── SECURITY.md          # Política de seguridad
└── README.md
```

## 🚀 Uso

```bash
# Ejecutar con tarea por defecto (healthcheck)
python main.py

# Ejecutar tarea específica
python main.py --task cleanup    # Limpia archivos temporales
python main.py --task backup     # Crea backups
python main.py --task report    # Genera reporte de sistema
python main.py --task healthcheck  # Health checks

# Ver ayuda
python main.py --help

# Verbose
python main.py --task healthcheck --verbose
```

## ⚙️ Configuración

Edita `.env` (copiado de `.env.example`):

| Variable | Descripción | Default |
|----------|-------------|---------|
| `BACKUP_DIR` | Directorio para backups | `/tmp/backups` |
| `BACKUP_DIRS` | Lista de directorios a respaldar (separados por coma) | _(vacío)_ |
| `HEALTHCHECK_SERVICES` | Servicios a verificar (host:puerto, separados por coma) | `localhost` |
| `LOG_LEVEL` | Nivel de logging | `INFO` |

## 🧪 Testing

```bash
# Instalar dependencias de test
pip install pytest pytest-cov httpx

# Ejecutar tests
pytest test_api.py -v

# Con coverage
pytest test_api.py --cov=. --cov-report=html
```

## 🔒 Verificación de Salud

```bash
# Verificar que el ambiente está listo
python health_check.py
```

## 🛡️ Seguridad

Ver [SECURITY.md](SECURITY.md) para política de reporte de vulnerabilidades y mejores prácticas.

## 📝 Licencia

MIT - vea [LICENSE](LICENSE)
