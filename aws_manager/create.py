import boto3
iam = boto3.client('iam')

def Create_user(username, password):
# Create user

        created_user = iam.create_user(
            UserName=username,
            Tags=[ # adding tags to identify that user in IAM
                {
                    'Key': 'Env',
                    'Value': 'Test'
                }
            ]
            )
# Create AceessKey and SecretKey
        keys = iam.create_access_key(
            UserName=username
        )
        full = keys['AccessKey']
        AccesskeyName = full['AccessKeyId']
        print('Here is the user AccessKey:  '+full['AccessKeyId'])
        print('Here is the user SecretAccessKey:  '+full['SecretAccessKey'])
# Create console management access with password
        create_login_ui = iam.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
            )
