# pygen

A simple Python package to generate Python files from a JSON config.

## Usage

1. Prepare a config file (see `pygen/sample_config.json` for an example):

```
{
    "class_name": "SampleClass",
    "methods": [
        {
            "name": "hello",
            "body": "print('Hello from generated code!')"
        }
    ]
}
```

2. Run the generator:

```
python -m pygen.generator pygen/sample_config.json --output generated_sample.py
```

Or, after installing as a package:

```
pygen-generator pygen/sample_config.json --output generated_sample.py
```

This will create a new Python file based on the config.
