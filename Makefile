
test:
	docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION --rm -v "${PWD}":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler '{"Records":[{"customData":"'${CODEBUILD_PROJECT}'","codecommit":{"references":[{"commit":"abcdefg12345"}]}}]}'
