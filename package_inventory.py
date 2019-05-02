import os
import json


inventory = os.listdir("pkg-inv/")
inventory.sort()

flagged_packages = ["tomcat", "tomcat8", "tomcat7"]
flagged_versions = ["8.0.41", '8.0.15', "7.0.68"]
found_versions = []
host_results = []

for file in inventory:
    with open(os.path.join("pkg-inv", file)) as json_inventory:
        json_packages = json.load(json_inventory)
        for package in json_packages:
            if package in flagged_packages:
                for key in json_packages[package]:
                    pkg_version = key["version"]
                    if pkg_version not in found_versions:
                        found_versions.append(pkg_version)
                    if pkg_version in flagged_versions:
                        host_results.append(file)

print("Versions Found:")
for version in found_versions:
    print("\t - " + version)

for host in host_results:
    print(host)
