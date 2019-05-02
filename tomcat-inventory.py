import os
import json


inventory = os.listdir("labs/")
inventory.sort()

flagged_packages = ["tomcat", "tomcat8",]
found_versions = []
host_results = []

for file in inventory:
    with open(os.path.join("labs", file)) as json_inventory:
        json_packages = json.load(json_inventory)
        for package in json_packages:
            if package in flagged_packages:
                print("Hostname: " + file)
                for key in json_packages[package]:
                    version = key["version"]
                    print("Version: " + package + "-" + version + "\n")
