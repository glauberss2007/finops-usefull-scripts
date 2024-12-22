import boto3
import csv
from datetime import datetime

def get_trusted_advisor_recommendations(accounts_file, output_file):
    with open(accounts_file, 'r') as f, open(output_file, 'w', newline='') as out_f:
        accounts = csv.reader(f)
        writer = csv.writer(out_f)
        writer.writerow(['Account ID', 'Check Name', 'Status', 'Resource ID', 'Description'])
        
        for account in accounts:
            account_id = account[0]
            
            # Assume role in the target account
            sts_client = boto3.client('sts')
            assumed_role = sts_client.assume_role(
                RoleArn=f'arn:aws:iam::{account_id}:role/CrossAccountTARole',
                RoleSessionName='TASession'
            )
            
            # Create a Support client with the assumed role credentials
            support_client = boto3.client(
                'support',
                aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
                aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
                aws_session_token=assumed_role['Credentials']['SessionToken']
            )
            
            # Get Trusted Advisor check results
            checks = support_client.describe_trusted_advisor_checks(language='en')
            for check in checks['checks']:
                result = support_client.describe_trusted_advisor_check_result(
                    checkId=check['id'],
                    language='en'
                )
                if result['result']['status']
                 if result['result']['status'] != 'ok':
                    for resource in result['result'].get('flaggedResources', []):
                        writer.writerow([
                            account_id,
                            check['name'],
                            result['result']['status'],
                            resource.get('resourceId', 'N/A'),
                            resource.get('metadata', ['N/A'])[-1]
                        ])
            
            print(f"Processed recommendations for account {account_id}")

get_trusted_advisor_recommendations('accounts.csv', 'ta_recommendations.csv')
