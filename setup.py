from distutils.core import setup

setup(
  name = 'codebuild-trigger',
  packages = ['codebuild-trigger'],
  version = '0.0.4',
  description = 'An AWS Lambda function to triggers CodeBuild on pushes to CodeCommit.',
  author = 'Tim Malone',
  author_email = 'tdmalone@gmail.com',
  url = 'https://github.com/tdmalone/codebuild-trigger',
  download_url = 'https://github.com/tdmalone/codebuild-trigger/archive/v0.0.4.tar.gz',
  keywords = ['aws', 'lambda', 'codebuild', 'codecommit'],
  classifiers = [],
)
