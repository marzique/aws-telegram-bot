import os

from aws_cdk import Stack, aws_lambda as lambda_, aws_lambda_python_alpha
from constructs import Construct


class BotInfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Layers
        self.dependencies_layer = aws_lambda_python_alpha.PythonLayerVersion(
            self, "DependenciesLayer",
            entry="../",  # Path to the directory containing requirements.txt file
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            description="A layer with dependencies",
        )

        # Lambdas:
        self.bot_lambda = lambda_.Function(
            self, 'SendTelegramMessageLambda',
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset('handlers'),
            handler='telegram_handlers.send_telegram_message',
            layers=[self.dependencies_layer],
            environment={  # Environment variables
                'BOT_TOKEN': os.environ.get('BOT_TOKEN'),
            }
        )


