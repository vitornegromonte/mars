@tool
def arxiv_search(topic: str, max_results: int = 100) -> list:
  """ Collects papers from arXiv based on a given topic. 
  
  Args:
    topic (str): The topic to search for.
    max_results (int): The maximum number of papers to return.
  
  Returns:
    list: A list of dictionaries containing the title, author, summary, published date, and URL of each paper.
    
  """
  
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

@tool
def store_papers(papers: list) -> None:
  """
  Stores the papers in a database.
  
  Args:
    papers (list): A list of dictionaries containing the title, author, summary, published date, and URL of each paper.
  
  Returns:
    None
  """
  # Code to store the papers in a database
  
  pass

# Check the papers in the database to see if they are already present or not, if they are not present, store them, and then return the papers
@tool
def papers_filter (papers: list) -> list:
  """
  Filters the papers to check if they are already present in the database. If not, stores them in the database.
  
  Args:
    papers (list): A list of dictionaries containing the title, author, summary, published date, and URL of each paper.
  
  Returns:
    list: A list of dictionaries containing the title, author, summary, published date, and URL of each paper.
  """
  # Code to check if the papers are already present in the database
  
  store_papers(papers)
  
  return papers