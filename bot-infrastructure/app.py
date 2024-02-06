#!/usr/bin/env python3
import os

import aws_cdk as cdk

from bot_infrastructure.bot_infrastructure_stack import BotInfrastructureStack

from dotenv import load_dotenv


load_dotenv()

app = cdk.App()
BotInfrastructureStack(
    app, "BotInfrastructureStack",
        # If you don't specify 'env', this stack will be environment-agnostic.
        # Account/Region-dependent features and context lookups will not work,
        # but a single synthesized template can be deployed anywhere.
        env=cdk.Environment(account='731117259466', region='eu-central-1'),
    )

app.synth()
