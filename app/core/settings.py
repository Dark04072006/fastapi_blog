import yaml
import pathlib

from app.core.parse_dataclasses import AppConfig, ServerConfig, DatabaseConfig


BASE_DIR = pathlib.Path(__file__).parent.parent.parent
config_path = BASE_DIR / "config" / "config.yaml"


def get_config(path):
    with open(path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        return AppConfig(
            application=ServerConfig(**yaml_data['application']['server']),
            database=DatabaseConfig(**yaml_data['database'])
        )


config = get_config(config_path)

