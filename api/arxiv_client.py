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
