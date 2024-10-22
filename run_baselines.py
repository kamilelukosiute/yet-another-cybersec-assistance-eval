import pandas as pd
from llm import LLM
from refusal_detection import detect_refusal


def run_baseline(df, prompts_col_name, model_name, baseline_name):
    llm = LLM(model_name, use_cache=False)
    responses = []
    for prompt in df[prompts_col_name].tolist():
        response = llm(prompt)
        responses.append(response)

    df = pd.DataFrame(responses)
    df.to_csv(baseline_name + "_" + model_name + ".csv")

    refusals = [True for output in responses if detect_refusal(output)]
    print("\n\n\n")
    print(model_name, baseline_name, sum(refusals))


if __name__ == "__main__":
    for eval, df_col, name in zip(
        [
            # "baselines_data/harmbech_cybersec_only.csv",
            "baselines_data/intents_only_baseline.csv",
            "baselines_data/cyberseceval_mitre_subsamples.csv",
        ],
        [
            # "Behavior",
            "intent",
            "0",
        ],
        [
            # "harmbench",
            "intents",
            "cybsrsec",
        ],
    ):
        for model in [
            "gpt-4o",
            "gemini-pro",
            "aws-anthropic.claude-3-5-sonnet-20240620-v1:0",
        ]:
            df = pd.read_csv(eval)
            run_baseline(df, df_col, model, name)

"""
gpt-4o harmbench cybsersec only 33/40 refusals
gemini-pro harmbench 29/40 refusals 
aws-anthropic.claude-3-5-sonnet-20240620-v1:0 harmbench 39/40 refusals


gpt-4o intents 36/100 refusals
gemini-pro intents 18/100 refusals
aws-anthropic.claude-3-5-sonnet-20240620-v1:0 intents 48/100 refusals

gpt-4o cybsrsec 55/100 refusals
gemini-pro cybsrsec 21/100 refusals
aws-anthropic.claude-3-5-sonnet-20240620-v1:0 cybsrsec 77/100 refusals
"""
