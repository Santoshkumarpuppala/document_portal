import yaml

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(config)
    return config

load_config("/Users/santoshkumarpuppala/Documents/Learnings/Agentic AI and Gen AI/LLMOPS/Projects/Project 1 Document Portal/config/config.yaml")