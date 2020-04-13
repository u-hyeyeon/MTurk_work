# url : https://blog.mturk.com/tutorial-how-to-verify-crowdsourced-training-data-using-a-known-answer-review-policy-85596fb55ed
# pricing : https://requester.mturk.com/pricing
#   $0 amount : Manage tab에서 bonus worker 버튼을 누르고 금액을 입력하고 ID 입력? 
#               https://blog.mturk.com/paying-for-non-submitted-hits-245c6c3323bb
import boto3
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "",
   aws_secret_access_key = "+",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)
# Read in the questions.xml file saved in the same directory
# AssignmentReviewPolicy : Known Answer
#   PolicyName is always 'ScoreMyKnownAnswers/2011–09–01'
#   parameter :
#       AnswerKey : Known Answers
#       ApproveIfKnownAnswerScoreIsAtLeast : Known Answer을 하나 이상 올바르게 작성할 경우 자동 승인
#       RejectIfKnownAnswerScoreIsLessThan  : Known Answer를 하나 미만을 경우 자동 거부, RejectReason 도 있어야 한다.
#       ExtendIfKnownAnswerScoreIsLessThan : Known Answer를 틀렸을 경우 자동 추가 
#       additional parameters guide : https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_AssignmentReviewPolicies.html
question = open('questions.xml','r').read()
new_hit = mturk.create_hit(
    Title = 'Do these images contain birds in them?',
    Description = 'Please review these 3 images and mark whether any of them contain a picture of a bird',
    Keywords = 'images, quick, labeling',
    Reward = '0.15',
    MaxAssignments = 1,
    LifetimeInSeconds = 172800,
    AssignmentDurationInSeconds = 600,
    AutoApprovalDelayInSeconds = 14400,
    Question = question,
    AssignmentReviewPolicy={
    'PolicyName':'ScoreMyKnownAnswers/2011-09-01',
    'Parameters':[
        {'Key':'AnswerKey', 'MapEntries':[{'Key': 'question_2', 'Values':['yes']}]},
        {'Key': 'ApproveIfKnownAnswerScoreIsAtLeast', 'Values':['1']},
        {'Key': 'RejectIfKnownAnswerScoreIsLessThan', 'Values':['1']},{'Key': 'RejectReason', 'Values':['Sorry, we could not approve your submission as you did not correctly identify the image containing the Flamingo.']},
        {'Key': 'ExtendIfKnownAnswerScoreIsLessThan','Values':['1']}
    ]
})
print ("A new HIT has been created. You can preview it here:")
print ("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=


"""
Known Answers Message :
    There was a problem submitting your results for this HIT.
    This HIT is still assigned to you. To try this HIT again, refresh the page. If this problem persists, you can contact the Requester for this HIT by clicking "HIT Details" above and then clicking "Contact This Requester" at the bottom of the pop up.
    
    To return this HIT and continue working on other HITs, click the "Return" button on the top or bottom of the right side of the page.
"""
