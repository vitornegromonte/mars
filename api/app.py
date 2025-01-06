from arxiv_search import get_papers
from agentic import analyze_and_tag 
from agentic import evaluate_paper
import json
import os
import time
from litellm import completion
from litellm.exceptions import RateLimitError


def main():
    topic = "Computer Vision"
    max_results = 3

    papers = get_papers(topic, max_results)

    for i, paper in enumerate(papers, 1):
        text = f"Title: {paper['title']}\nSummary: {paper['summary']}"
        print(f"Processing paper {i}/{len(papers)}: {paper['title']}")
        topic = analyze_and_tag(text)
        score = evaluate_paper(text, topic)
        if score >= 7:
            print(f"Paper {i}:")
            print(f"Title: {paper['title']}")
            print(f"Authors: {', '.join(paper['authors'])}")
            print(f"Published: {paper['published']}")
            print(f"Summary: {paper['summary'][:500]}...")  # Print first 500 chars of summary
            print(f"Link: {paper['url']}")
            print(f"Topic: {topic}")
            print(f"Score: {score}")
            print("\n" + "-"*80 + "\n")
        else:
            print(f"Paper {i} is not highly innovative in the {topic} domain. Skipping...\n")


if __name__ == "__main__":
    main()