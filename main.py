from dis import Instruction
from openai import OpenAI
from typing import List, Dict
import json
import os

client = OpenAI(
    api_key=os.environ['api']
)

# --------------------------
# 1. Define a small benchmark dataset
# --------------------------
benchmark = [
    {"task": "random", "question": "How many r's are there in the word strawberry?", "answer": "3"},
    {"task": "math", "question": "What is 17 + 26?", "answer": "43"},
    {"task": "math", "question": "If a train leaves at 3PM and travels for 2 hours, what time does it arrive?", "answer": "5PM"},
    {"task": "qa", "question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"task": "qa", "question": "What is the capital of Japan?", "answer": "Tokyo"},
]

nbme_questions = json.load(open("nbme_questions.json"))

# --------------------------
# 2. Model wrapper (example: OpenAI GPT models)
# --------------------------
def query_model(prompt: str, model_name: str) -> str:
    """Send a prompt to a model and return its text output."""
    response = client.responses.create(
        instructions="Answer A. B. C. D. or E. depending on the question.",
        model=model_name,
        input=prompt,
        # max_tokens=100,
        # temperature=0
    )
    content = response.output[0].content[0].text
    return content if content is not None else ""

# --------------------------
# 3. Evaluation function
# --------------------------
def evaluate_model(model_name: str, dataset: List[Dict]) -> Dict:
    correct = 0
    results = []
    
    for item in dataset:
        model_output = query_model(item["content"] + "\n" + "\n".join(item["all_content"]), model_name)
        
        # simple exact match scoring
        is_correct = item["correct_answers"][0].split(" ")[0].lower() in model_output.lower()
        results.append({
            "question": item["content"] + "\n" + "\n".join(item["all_content"]),
            "expected": item["correct_answers"],
            "model_output": model_output,
            "correct": is_correct
        })
        
        if is_correct:
            correct += 1
    
    accuracy = correct / len(dataset)
    return {"model": model_name, "accuracy": accuracy, "details": results}

# --------------------------
# 4. Run benchmark on two models
# --------------------------
if __name__ == "__main__":
    models_to_test = ["gpt-4o-mini", "gpt-3.5-turbo"]  # swap with any available
    for model in models_to_test:
        results = evaluate_model(model, nbme_questions)
        print(f"\nModel: {results['model']}")
        print(f"Accuracy: {results['accuracy']*100:.1f}%")
        for r in results["details"]:
            print(f"Q: {r['question']}")
            print(f"Expected: {r['expected']}")
            print(f"Model Output: {r['model_output']}")
            print(f"Correct: {r['correct']}\n")
