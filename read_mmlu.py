# read in and display one by one each of the mmlu questions, formatted
# with the answer choices and the correct answer

# file is a jsonl with the following fields:
# {"question_id": "mmlu_computer_security_99", "system": "You are a computer security expert answering real-world cybersecurity certification exam questions. Based on your understanding of fundamental and applied security principles, technical knowledge, and mechanisms underlying secure systems, vulnerabilities, threat mitigation, and modes of defense, answer the following multiple-choice question. Select one correct answer from A to D. Base your answer on current best practices and standards referenced in cybersecurity guidelines.", "question": "Question: Three of the following are classic security properties; which one is not?\nOptions:\n(A) Confidentiality\n(B) Availability\n(C) Correctness\n(D) Integrity", "answer": "Explanation:\nPLACEHOLDER\n\nAnswer: (B)"}


# waits for user input to continue
import json

with open('mmlu_cybersec.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        print(data['question'])
        print(data['answer'])
        print("\n\n")
        input("Press Enter to continue...")