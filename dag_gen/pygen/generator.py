import argparse


def generate_python_file(config_path, output_path=None):
    code_lines = [
        'import yaml',
        '',
        f'with open(r"{config_path}", "r") as f:',
        '    config = yaml.safe_load(f)',
        'print(config)'
    ]
    import os
    # Always resolve DAG_GEN/generated files relative to the fixed project root
    project_root = r"c:\Users\navee\deg_gen_repo\dag_gen"
    output_dir = os.path.join(project_root, 'DAG_GEN', 'generated files')
    os.makedirs(output_dir, exist_ok=True)
    output_file = output_path or 'print_config.py'
    # If output_file is not an absolute path, save it in DAG_GEN/generated files
    if not os.path.isabs(output_file):
        output_file = os.path.join(output_dir, output_file)
    with open(output_file, 'w') as f:
        f.write('\n'.join(code_lines))
    print(f'Generated {output_file}')


def main():
    parser = argparse.ArgumentParser(description='Generate Python code from config file')
    parser.add_argument('config', help='Path to config JSON file')
    parser.add_argument('--output', help='Output Python file path', default=None)
    args = parser.parse_args()
    generate_python_file(args.config, args.output)


if __name__ == '__main__':
    main()
