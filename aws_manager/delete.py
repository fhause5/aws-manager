import boto3
iam = boto3.client('iam')

def get_access_keys(username):
    response = iam.list_access_keys(
        UserName=username
    )
    full_response = response['AccessKeyMetadata']
    keysName = full_response[0]['AccessKeyId']
    return keysName

def Delete_user(username):
    custom_policy_name = 'arn:aws:iam::587428383467:policy/Full_access_to_a_region'
    delete_policy = iam.detach_user_policy(
        UserName=username,
        PolicyArn=custom_policy_name

    )
    default_policy_name = 'arn:aws:iam::aws:policy/IAMUserChangePassword'
    delete_policy = iam.detach_user_policy(
        UserName=username,
        PolicyArn=default_policy_name

    )

    access_key = iam.delete_access_key(
        UserName=username,
        AccessKeyId=get_access_keys(username)
    )
    delete_login = iam.delete_login_profile(
        UserName=username
    )
    user_to_delete = iam.delete_user(
        UserName=username
    )
    print("The user has deleted")
