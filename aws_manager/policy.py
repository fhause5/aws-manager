import boto3
iam = boto3.client('iam')

def Create_custom_policy(region):
    try:
        region_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "*",
                    "Effect": "Allow",
                    "Resource": "*",
                    "Condition": {
                        "StringEquals": {
                            "ec2:Region": region
                        }
                    }
                }
            ]
        }
        creating = iam.create_policy(
          PolicyName='Full_access_to_a_region',
          PolicyDocument=json.dumps(region_policy)
        )
        #print(creating)
    except:
        print("DEBUG: [The policy has already created]")
