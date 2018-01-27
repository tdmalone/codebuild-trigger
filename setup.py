from distutils.core import setup

setup(
  name = 'code-build-trigger',
  packages = ['code-build-trigger'],
  version = '0.0.1',
  description = 'An AWS Lambda function to triggers CodeBuild on pushes to CodeCommit.',
  author = 'Tim Malone',
  author_email = 'tdmalone@gmail.com',
  url = 'https://github.com/tdmalone/code-build-trigger',
  download_url = 'https://github.com/tdmalone/code-build-trigger/archive/0.1.tar.gz',
  keywords = ['aws', 'lambda', 'codebuild', 'codecommit'],
  classifiers = [],
)
