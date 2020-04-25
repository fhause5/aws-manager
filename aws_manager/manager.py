import boto3
import json
import click
import sys

from .create import Create_user
from .policy import Create_custom_policy
from .attach import Attach_custom_policy
from .attach import Attach_default_policy
from .delete import Delete_user

iam = boto3.client('iam')

# Configure arguments and help
@click.command()
@click.option("--username", "-u", default=None, help="IAM user for AWS")
@click.option("--password", "-p", default=None, help="Password for IAM user")
@click.option("--region", "-r", default=None, help="Region for IAM Policy")
@click.option("--accountid", "-id", default=None, help="Enter you account ID")
@click.option("--deleting", "-d", default=None, help="USE ALL arguments for deleting [EXAMPLE: python aws_python/awsmanaging.py -u user -r eu-west-1 -p admin -id 587426783467 -d delete]")

def manager(username, password, region, accountid, deleting):
    if deleting == 'delete':
        Delete_user(username)
    else:
        Create_user(username, password)
        Create_custom_policy(region)
        Attach_custom_policy(username, accountid)
        Attach_default_policy(username)

manager()
