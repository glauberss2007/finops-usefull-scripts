# finops-usefull-scripts

# AWS FinOps Scripts

This repository contains a collection of Python scripts to automate various FinOps tasks in AWS.

## Scripts

### 1. Set Budget Alerts for Multiple Accounts

**Description:**
This script automates the process of setting up budget alerts across multiple AWS accounts. It reads account information from a CSV file and creates a monthly budget with an alert for each account. The script uses AWS Organizations and assumes a role in each account to set up the budget.

**Key features:**
- Sets a monthly budget for each account
- Configures an alert when the actual spend reaches a specified threshold
- Sends email notifications to a designated address
- Processes multiple accounts from a CSV file

### 2. Get Trusted Advisor Recommendations for Multiple Accounts

**Description:**
This script retrieves Trusted Advisor recommendations for multiple AWS accounts and compiles them into a single CSV file. It focuses on checks that are not in the "ok" status, providing valuable insights into potential cost savings, performance improvements, and security enhancements across your AWS organization.

**Key features:**
- Collects Trusted Advisor recommendations from multiple accounts
- Filters for checks that require attention (not in "ok" status)
- Outputs results to a CSV file for easy analysis
- Includes account ID, check name, status, affected resource, and description

### 3. Configure Cost Anomaly Detection for Multiple Accounts

**Description:**
This script sets up AWS Cost Anomaly Detection for multiple accounts in your organization. It creates an anomaly monitor and subscription for each account, allowing you to receive alerts when unexpected spending patterns are detected.

**Key features:**
- Creates a dimensional anomaly monitor for each account, focusing on service-level anomalies
- Sets up a daily anomaly subscription with a specified threshold
- Configures email notifications for detected anomalies
- Processes multiple accounts from a CSV file


