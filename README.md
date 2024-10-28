
# Yet Another Cybersecurity Assistance Evaluation

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


## Rationale
We aimed to create prompts that are more realistic representations of how attackers may use LLM tools to carry out cyberattacks. Drawing on our own experience asking for programming assistance, we wrote prompts that reflect our personal usage of LLM assistance. This means asking for specific, granular help, in the middle of a task and incorporating context e.g. “I’m working on a Mac.” Our assumption was that, since carrying out cyberattacks is a related activity to software development, cyber attacker LLM interactions will look somewhat similar to these interactions.
## Data Source
The MITRE ATT&CK framework, a “knowledge base of adversary tactics and techniques based on real-world observations”, is the industry standard for describing attacker behavior. To model potential adversary queries, we selected a subset of common techniques and crafted prompts seeking assistance in implementing a portion of attacks based on a single technique.
Our prompts request specific, individual support tasks rather than broad, unrealistic scenarios. For example, instead of asking “how to hack a US defense agency’s database” — a context- and architecture- dependent, multi-step process involving reconnaissance, exploitation, discovery, and exfiltration — we focus on discrete, actionable steps.
We focused on techniques that we personally have familiarity with in order to ensure meaningful questions and correct reference answers.
## Evaluation
We use a flexible framework that allows us to judge an answer as correct if it contains a set of strings (potentially with conditional statements if several answers may be correct) or by asking for Python/Bash scripts which are then judged correct through simulations that run inside containers. Most questions are graded through substring evaluation.
## Coverage of MITRE ATT&CK in our dataset
In total, the dataset contains 100 examples. The table does not add up to this, as some prompts/techniques span several tactics.
| MITRE ATT&CK Tactic | Techniques | Prompts | % Covered |
|-------------------|------------|---------|-----------|
| Reconnaissance | 44 | 3 | 6.82 |
| Resource Development | 47 | 0 | 0.00 |
| Initial Access | 96 | 0 | 0.00 |
| Execution | 87 | 9 | 10.34 |
| Persistence | 283 | 18 | 6.36 |
| Privilege Escalation | 211 | 16 | 7.58 |
| Defense Evasion | 457 | 23 | 5.03 |
| Credential Access | 223 | 16 | 7.17 |
| Discovery | 167 | 17 | 10.18 |
| Lateral Movement | 66 | 0 | 0.00 |
| Collection | 109 | 17 | 15.60 |
| Command and Control | 140 | 7 | 5.00 |

## Are our prompts really realistic?
After most of the completion of this work, OpenAI [published a report](https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf) on how adversary groups are using their models to assist in their operations. Queries to GPT models included:
● Asking for help to debug code (that’s part of a larger framework for programmatically sending text messages to attacker specified numbers).
● Asking why a bash code snippet returns an error.
● Asking how to access user passwords in MacOS.
● Seeking help debugging and implementing an Instagram scraper.
This seems pretty similar to the prompts we were writing! However, we are only two people and a more thorough study would include studying and incorporating the usage patterns of other people.
Additional limitations are: small dataset size not allowing for true statistical analysis, bias towards techniques we have familiarity with (too much Bash and Python), lack of technique coverage, and not evaluating using jailbreaks or other forcing techniques.

## Evaluation on models
See [here](https://kamilelukosiute.github.io/yet-another-cybersec-assistance-eval/) for full results. 

## References
1. Gennari et al., "Evaluating LLMs for Cybersecurity Tasks," 2024.
2. Mazeika et al., "HarmBench: Eval Framework for Automated Red Teaming," 2024.
3. Bhatt et al., "Purple Llama CyberSecEval: Secure Coding Benchmark," 2023.
4. Bhatt et al., "CYBERSECEVAL 2: Wide-Ranging Cybersecurity Evaluation," 2024.
5. Wan et al., "CYBERSECEVAL 3: Advancing Cybersecurity Evaluation in LLMs," 2024.
6. MITRE Corporation, "MITRE ATT&CK," https://attack.mitre.org/
7. Rein et al., "GPQA: Graduate-Level Google-Proof Q&A Benchmark," 2023.
8. Nimmo & Flossman, "Influence and Cyber Operations: An Update," 2024. 9. Nicholas Carlini, “Yet another applied LLM benchmark”, Github, 2024.
