import boto3

# Get AWS cost for the months of 2023 may
client = boto3.client('ce', region_name='us-east-1')
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2023-05-01',
        'End': '2023-05-31'
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)


