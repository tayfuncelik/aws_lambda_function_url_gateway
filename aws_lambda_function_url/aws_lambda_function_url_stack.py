from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda
)
from constructs import Construct


class AwsLambdaFunctionUrlStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            # Code loaded from the "lambda" directory
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',  # file is "hello", function is "handler"
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )
