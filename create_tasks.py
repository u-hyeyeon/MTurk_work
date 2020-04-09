<<<<<<< HEAD
import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJFU72LV4N3HLGFLQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

question = open('questions.xml','r').read()
new_hit = mturk.create_hit(
    Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
    Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
    Keywords = 'text, quick, labeling',
    Reward = '0.15',
    MaxAssignments = 1,
    LifetimeInSeconds = 172800,
    AssignmentDurationInSeconds = 600,
    AutoApprovalDelayInSeconds = 14400,
    Question = question,
)
print ("A new HIT has been created. You can preview it here:")
print ("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
print ("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")
# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=

# A new HIT has been created. You can preview it here:
# https://workersandbox.mturk.com/mturk/preview?groupId=3HL3WX654CPRBBE4VSYM9ISRFC0PQO
# HITID = 386659BNTL9Z1QSRBMJ7JXWXZX301J (Use to Get Results)
=======
# url : https://blog.mturk.com/tutorial-a-beginners-guide-to-crowdsourcing-ml-training-data-with-python-and-mturk-d8df4bdf2977
# source bin/activate (windows) call Script/activate.bat
import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJFU72LV4N3HLGFLQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

question = open('questions.xml','r').read()
new_hit = mturk.create_hit(
    Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
    Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
    Keywords = 'text, quick, labeling',
    Reward = '0.15',
    MaxAssignments = 1,
    LifetimeInSeconds = 172800,
    AssignmentDurationInSeconds = 600,
    AutoApprovalDelayInSeconds = 14400,
    Question = question,
)
print ("A new HIT has been created. You can preview it here:")
print ("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
print ("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")
# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=

# A new HIT has been created. You can preview it here:
# https://workersandbox.mturk.com/mturk/preview?groupId=3HL3WX654CPRBBE4VSYM9ISRFC0PQO
# HITID = 386659BNTL9Z1QSRBMJ7JXWXZX301J (Use to Get Results)
>>>>>>> [2020.04.10] merge
