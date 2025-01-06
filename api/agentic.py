import arxiv_search
import json
import os
import time
from litellm import completion
from litellm.exceptions import RateLimitError

os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY

def analyze_and_tag(text):
    messages = [
        {
            "role": "system",
            "content": "You are a specialized agent responsible for analyzing academic papers and tagging them with relevant topics."
        },
        {
            "role": "user",
            "content": f"Analyze the following paper and provide a single, concise topic tag from the following list:\n- Natural Language Processing (NLP)\n- Computer Vision (CV)\n- Efficient AI/TinyML (TM)\n- Pure Machine Learning (ML)\n- Pure Deep Learning (DL)\n- Reinforcement Learning (RL),\n-Generative AI (GENAI), \n-Graph Neural Network(GNN)\n\nPaper Title: {text.split('\n')[0].replace('Title: ', '')}\nPaper Summary: {text.split('\n')[1].replace('Summary: ', '')}\n\nTopic:"
        }
    ]
    
    while True:
        try:
            response = completion(
                model="gemini/gemini-2.0-flash-exp",
                messages=messages,
                response_format={"type": "json_object"},
                topK=1
            )
            topic = response.choices[0].message.content.strip()
            try:
                topic_data = json.loads(topic)
                topic = topic_data.get("topic", "Unknown")
            except json.JSONDecodeError:
                print(f"Failed to parse JSON response for topic. Defaulting to 'Unknown'. Response: {topic}")
                topic = "Unknown"
            return topic
        except RateLimitError:
            print("Rate limit exceeded. Retrying in 60 seconds...")
            time.sleep(60)  # Wait for 60 seconds before retrying


def evaluate_paper(text, topic):
    messages = [
        {
            "role": "system",
            "content": f"You are an expert in {topic} and are responsible for evaluating academic papers."
        },
        {
            "role": "user",
            "content": f"- Relevance Check: Start by assessing whether the paper's title and abstract are clearly aligned with the field of {topic}. If the paper is irrelevant to NLP, assign a score of 0 and do not proceed further. \n- Innovation Assessment: If the paper is relevant, evaluate how innovative and impactful the research is within the NLP domain. Consider factors such as the novelty of the approach, contribution to existing methods, and potential significance to the field. \n- Based on your evaluation, provide a score between 0 and 10, with 0 for irrelevant papers and 10 for highly innovative work. \n\nPaper Title: {text.split('\n')[0].replace('Title: ', '')}\nPaper Summary: {text.split('\n')[1].replace('Summary: ', '')}\n\nScore:"
        }
    ]
    
    while True:
        try:
            response = completion(
                model="gemini/gemini-exp-1206",
                messages=messages,
                response_format={"type": "json_object"},
                topK=1
            )
            score = response.choices[0].message.content.strip()
            try:
                score_data = json.loads(score)
                score = float(score_data.get("score", 5.0))  # Default score if not found
            except json.JSONDecodeError:
                print(f"Failed to parse JSON response for score. Defaulting to 5.0. Response: {score}")
                score = 5.0
            return score
        except RateLimitError:
            print("Rate limit exceeded. Retrying in 60 seconds...")
            time.sleep(60) 