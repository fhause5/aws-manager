import boto3
iam = boto3.client('iam')

def Attach_custom_policy(username, accountid):

    attach_to_user = iam.attach_user_policy(
    UserName = username, #Name of user
    PolicyArn = 'arn:aws:iam::'+accountid+':policy/Full_access_to_a_region'
        # Policy ARN which you want to asign to user
    )
    #print(attach_to_user)

def Attach_default_policy(username):

    attach_to_user = iam.attach_user_policy(
    UserName = username, #Name of user
    PolicyArn = 'arn:aws:iam::aws:policy/IAMUserChangePassword'
        # Policy ARN which you want to asign to user
    )
    #print(attach_to_user)
