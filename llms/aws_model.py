import boto3
from botocore.config import Config
import json


class AWSModel:
    def __init__(self, name):
        self.name = name

        config = json.load(open("config.json"))
        self.region = config["llms"]["aws"]["region"]

        self.client = boto3.client(
            service_name="bedrock-runtime", config=Config(region_name=self.region)
        )

        self.hparams = config["hparams"]
        self.hparams.update(config["llms"]["aws"].get("hparams") or {})

    def make_request(self, conversation, add_image=None, max_tokens=None):
        messages = [
            {
                "role": "user" if i % 2 == 0 else "assistant",
                "content": [{"text": content}],
            }
            for i, content in enumerate(conversation)
        ]

        kwargs = {
            "modelId": self.name,
            "messages": messages,
            "inferenceConfig": self.hparams,  # Changed from inferenceConfiguration to inferenceConfig
        }

        if max_tokens:
            kwargs["inferenceConfig"]["maxTokens"] = max_tokens

        try:
            response = self.client.converse(**kwargs)
            return response["output"]["message"]["content"][0]["text"]
        except Exception as e:
            raise Exception(f"Error making request: {str(e)}")


if __name__ == "__main__":
    q = "What's your name?"
    print(
        q + ":", AWSModel("anthropic.claude-3-sonnet-20240229-v1:0").make_request([q])
    )
