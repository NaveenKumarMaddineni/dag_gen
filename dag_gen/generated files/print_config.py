import yaml

with open(r"sample_config.yaml", "r") as f:
    config = yaml.safe_load(f)
print(config)