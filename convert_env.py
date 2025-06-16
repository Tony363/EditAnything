import yaml

def extract_pip_dependencies(yml_file, output_file="requirements.txt"):
    with open(yml_file, 'r') as f:
        environment_data = yaml.safe_load(f)

    pip_dependencies = []
    if 'dependencies' in environment_data:
        for dep in environment_data['dependencies']:
            if isinstance(dep, dict) and 'pip' in dep:
                pip_dependencies.extend(dep['pip'])

    if pip_dependencies:
        with open(output_file, 'w') as f:
            for package in pip_dependencies:
                f.write(package + '\n')
        print(f"Pip dependencies extracted to {output_file}")
    else:
        print("No pip dependencies found in the YAML file.")

if __name__ == "__main__":
    extract_pip_dependencies("/teamspace/studios/this_studio/EditAnything/environment.yaml")
