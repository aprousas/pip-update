import subprocess
import json

def main():
	outdated_packages = find_oudated_packages()

	if not outdated_packages:
		print("All packages are up-to-date.")
		return

	print(str(len(outdated_packages))+" packages to be updated.")	
	for package in outdated_packages:
		pip_upgrade_package(package['name'])

def find_oudated_packages():
	process = subprocess.Popen(['pip','list','--outdated', '--format', 'json'], stdout=subprocess.PIPE)
	outdated_packages_json = process.stdout.read()
	return json.loads(outdated_packages_json)

def pip_upgrade_package(package_name):
	subprocess.call(['pip','install', '--upgrade', package_name])

if __name__ == "__main__":
	main()
