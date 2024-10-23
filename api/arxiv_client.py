import arxiv

def get_papers(topic, max_results=100):
  Client = arxiv.Search(
    query = topic,
    max_results = max_results,
    sort_by = arxiv.SortCriterion.SubmittedDate
    
  )
  
  papers = []
  
  for results in Client.results():
    paper = {
      'title': results.title,
      'author': [author.name for author in results.authors], 
      'summary': results.summary,
      'published': results.published,
      'url': results.pdf_url
    }
    papers.append(paper)
    
  return papers

# Test the function
if __name__ == "__main__":
    query = "machine learning"
    max_results = 5
    papers = get_papers(query, max_results)
    
    for i, paper in enumerate(papers, 1):
        print(f"Paper {i}:")
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['author'])}")
        print(f"Published: {paper['published']}")
        print(f"Summary: {paper['summary']}.")  # Print first 500 chars of summary
        print(f"Link: {paper['url']}")
        print("\n" + "-"*80 + "\n")