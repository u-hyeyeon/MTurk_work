<<<<<<< HEAD
import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   aws_access_key_id = "",
   aws_secret_access_key = "",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict
# Use the hit_id previously created
hit_id = '386659BNTL9Z1QSRBMJ7JXWXZX301J'
# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed
worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])

if worker_results['NumResults'] > 0:
   for assignment in worker_results['Assignments']:
      xml_doc = xmltodict.parse(assignment['Answer'])
      
      print("Worker's answer was:")
      if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
         # Multiple fields in HIT layout
         for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
            print ("For input field: " + answer_field['QuestionIdentifier'])
            print ("Submitted answer: " + answer_field['FreeText'])
      else:
         # One field found in HIT layout
         print ("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
         print ("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
else:
=======
# url : https://blog.mturk.com/tutorial-a-beginners-guide-to-crowdsourcing-ml-training-data-with-python-and-mturk-d8df4bdf2977
# answer monitor
import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAJFU72LV4N3HLGFLQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict
# Use the hit_id previously created
hit_id = '386659BNTL9Z1QSRBMJ7JXWXZX301J'
# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed
worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])

if worker_results['NumResults'] > 0:
   for assignment in worker_results['Assignments']:
      xml_doc = xmltodict.parse(assignment['Answer'])
      
      print("Worker's answer was:")
      if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
         # Multiple fields in HIT layout
         for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
            print ("For input field: " + answer_field['QuestionIdentifier'])
            print ("Submitted answer: " + answer_field['FreeText'])
      else:
         # One field found in HIT layout
         print ("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
         print ("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
else:
>>>>>>> [2020.04.10] merge
   print ("No results ready yet")
