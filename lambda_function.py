"""
A simple AWS Lambda function designed to trigger CodeBuild on pushes to CodeCommit.
Because for some reason, that's not possible by default!

Based heavily on this:
https://www.linkedin.com/pulse/use-aws-codecommit-lambda-trigger-codebuild-container-trevor-sullivan/
"""

import boto3

def lambda_handler( event, context ):

  cb = boto3.client( 'codebuild' )

  build = {
    'projectName': event['Records'][0]['customData'],
    'sourceVersion': event['Records'][0]['codecommit']['references'][0]['commit']
  }

  print( 'Starting build for project {0} from commit ID {1}...'.format( build['projectName'], build['sourceVersion'] ) )
  cb.start_build( **build )
  print( 'Successfully launched build.' )

  return 'Success.'
