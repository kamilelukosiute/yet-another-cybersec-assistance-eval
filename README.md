
# Yet Another Cybsersecurity Assistance Evaluation

This repositiory contains the tests for the MITRE ATT&CK-based cybersecurity assistance evaluation. 
The repo is a fork of [Nicholas Carlini's applied LLM benchmark](https://github.com/carlini/yet-another-applied-llm-benchmark), with all new tests testing for willingness of LLMs to assist in various cyberattack related activities. 

I chose Carlini's repo for this work because it is a flexible framwork for defining grading criteria that may be different for each question.
Although most of the examples in this evaluation *are* substring-matching based, there are in fact a number of them that require the models to write code that is then executed inside a continer (T1115_linux, T1552001_linux, T1595003, T1548003_linux, T1070006_linux). 

Recreate results by running:
```
python main.py --run-tests --model aws-anthropic.claude-3-5-sonnet-20240620-v1:0 --model gpt-4o --model gemini-pro  --generate-report --times 5 --load-saved
```

See config files for the models supported by *this* repo. For AWS Bedrock, cofigure sso and specify region (Claude 3.5 Sonnet might still be only available in us-east-1 idk).

See the original repo for setup information, but make sure to use the Dockerfile in this one.



