import subprocess

def install_pip():
    try:
        subprocess.check_call(['sudo', 'apt', 'update'])
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y','python3-tk'])
        # Install pip
        subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3-pip'])
        print("Installed pip successfully!")

    except subprocess.CalledProcessError:
        print("Failed to install pip.")

def install_package_with_pip(package_name):
    try:
        # Install package 
        subprocess.check_call(['sudo', 'pip3', 'install', package_name])
        print(f"Package '{package_name}' installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Failed to install package '{package_name}'.")

# Usage example
install_pip()
package_list = ['numpy', 'pandas', 'regex', 'nltk', 'scikit-learn', 'seaborn', 'matplotlib', 'psutil']
for package in package_list:
    install_package_with_pip(package)

print("Successfully installed all required packages")

