import boto3
import csv

def configure_cost_anomaly_detection(accounts_file, threshold_amount):
    with open(accounts_file, 'r') as f:
        accounts = csv.reader(f)
        for account in accounts:
            account_id = account[0]
            
            # Assume role in the target account
            sts_client = boto3.client('sts')
            assumed_role = sts_client.assume_role(
                RoleArn=f'arn:aws:iam::{account_id}:role/CrossAccountCERole',
                RoleSessionName='CESession'
            )
            
            # Create a Cost Explorer client with the assumed role credentials
            ce_client = boto3.client(
                'ce',
                aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
                aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
                aws_session_token=assumed_role['Credentials']['SessionToken']
            )
            
            # Create anomaly monitor
            monitor_arn = ce_client.create_anomaly_monitor(
                MonitorName=f'Account-{account_id}-AnomalyMonitor',
                MonitorType='DIMENSIONAL',
                MonitorDimension='SERVICE'
            )['MonitorArn']
            
            # Create anomaly subscription
            ce_client.create_anomaly_subscription(
                SubscriptionName=f'Account-{account_id}-AnomalySubscription',
                Threshold=threshold_amount,
                Frequency='DAILY',
                MonitorArnList=[monitor_arn],
                Subscribers=[
                    {
                        'Type': 'EMAIL',
                        'Address': 'finance@yourcompany.com'
                    }
                ]
            )
            
            print(f"Cost anomaly detection configured for account {account_id}")

configure_cost_anomaly_detection('accounts.csv', 100)
