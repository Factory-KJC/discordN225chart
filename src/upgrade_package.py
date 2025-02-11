import subprocess

def upgrade_package(package_name):
    try:
        # Run pip install --upgrade command
        result = subprocess.run(
            ['pip', 'install', '--upgrade', package_name],
            capture_output=True,
            text=True
        )

        # Check the output for success message
        if "Successfully installed" in result.stdout:
            print(f'{package_name} has been successfully upgraded.')
        elif "Requirement already satisfied" in result.stdout:
            print(f'{package_name} is already up-to-date.')
        else:
            print(f'Failed to upgrade {package_name}.')
            print(result.stdout)
            print(result.stderr)

    except Exception as e:
        print(f'An error occurred while upgrading {package_name}: {e}')
