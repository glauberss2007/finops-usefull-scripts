import boto3
import csv

def set_budget_alerts(accounts_file, budget_amount, alert_threshold):
    with open(accounts_file, 'r') as f:
        accounts = csv.reader(f)
        for account in accounts:
            account_id = account[0]
            
            # Assume role in the target account
            sts_client = boto3.client('sts')
            assumed_role = sts_client.assume_role(
                RoleArn=f'arn:aws:iam::{account_id}:role/CrossAccountBudgetRole',
                RoleSessionName='BudgetSession'
            )
            
            # Create a Budgets client with the assumed role credentials
            budgets_client = boto3.client(
                'budgets',
                aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
                aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
                aws_session_token=assumed_role['Credentials']['SessionToken']
            )
            
            # Create budget with alert
            budgets_client.create_budget(
                AccountId=account_id,
                Budget={
                    'BudgetName': 'MonthlyBudget',
                    'BudgetLimit': {
                        'Amount': str(budget_amount),
                        'Unit': 'USD'
                    },
                    'TimeUnit': 'MONTHLY',
                    'BudgetType': 'COST'
                },
                NotificationsWithSubscribers=[
                    {
                        'Notification': {
                            'NotificationType': 'ACTUAL',
                            'ComparisonOperator': 'GREATER_THAN',
                            'Threshold': alert_threshold,
                            'ThresholdType': 'PERCENTAGE'
                        },
                        'Subscribers': [
                            {
                                'SubscriptionType': 'EMAIL',
                                'Address': 'finance@yourcompany.com'
                            }
                        ]
                    }
                ]
            )
            print(f"Budget alert set for account {account_id}")

set_budget_alerts('accounts.csv', 1000, 80)
