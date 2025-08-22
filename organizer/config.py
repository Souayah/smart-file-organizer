import json
import yaml
import os

def load_config(config_path=None):
    default_config = {
        "Documents": ["pdf", "doc", "docx", "txt", "odt"],
        "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff"],
        "Archives": ["zip", "rar", "7z", "tar", "gz"],
        "Videos": ["mp4", "mov", "avi", "mkv"],
        "Audio": ["mp3", "wav", "aac", "flac"]
    }

    if config_path:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        try:
            with open(config_path, 'r') as f:
                if config_path.endswith(('.yaml', '.yml')):
                    return yaml.safe_load(f)
                elif config_path.endswith('.json'):
                    return json.load(f)
                else:
                    raise ValueError("Unsupported configuration file format. Use .json, .yaml, or .yml")
        except (json.JSONDecodeError, yaml.YAMLError, Exception) as e:
            raise ValueError(f"Error loading configuration from {config_path}: {e}")
    return default_config


