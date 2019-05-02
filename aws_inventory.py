#!/usr/bin/python3

# Generates AWS host inventory for Ansible

import boto3

session = boto3.Session(profile_name='default')
ec2 = session.client('ec2', region_name='us-west-2')

response = ec2.describe_instances()
instance_list = []

for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        for network_interface in instance["NetworkInterfaces"]:
            instance_list.append(instance["PrivateIpAddress"])
            

# Write hosts out to inventory file for Ansible.
with open("aws_hosts", "w") as hosts_file:
    # Set the newline char to blank string to avoid \n at start of file
    newline = ""
    for instance in instance_list:
        hosts_file.write(newline + instance)
        newline = "\n"  # Set newline char to \n so the rest of the file is properly separated
