<<<<<<< HEAD
import boto3

region_name = 'us-east-1'
aws_access_key_id = ''
aws_secret_access_key = ''

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
#    endpoint_url=endpoint_url,		# live
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# This will return $10,000.00 in the MTurk Developer Sandbox
print(client.get_account_balance()['AvailableBalance'])


MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJFU72LV4N3HLGFLQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)
print ("I have $"+mturk.get_account_balance()['AvailableBalance']+" in my Sandbox account")
=======
import boto3

region_name = 'us-east-1'
aws_access_key_id = 'AKIAJFU72LV4N3HLGFLQ'
aws_secret_access_key = '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'

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
#    endpoint_url=endpoint_url,		# live
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# This will return $10,000.00 in the MTurk Developer Sandbox
print(client.get_account_balance()['AvailableBalance'])


MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJFU72LV4N3HLGFLQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)
print ("I have $"+mturk.get_account_balance()['AvailableBalance']+" in my Sandbox account")
>>>>>>> [2020.04.10] merge
