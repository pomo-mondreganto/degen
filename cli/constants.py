from pathlib import Path

BASE_DIR = Path(__file__).resolve().absolute().parents[1]
SERVICE_DIR = BASE_DIR / 'service'
SERVICE_REQUIREMENTS = SERVICE_DIR / 'requirements.txt'
GENERATED_PATH = SERVICE_DIR / 'generated.py'
MODELS_SRC = BASE_DIR / 'models.py'
MODELS_DST = SERVICE_DIR / 'models.py'
