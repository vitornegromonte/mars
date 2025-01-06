import arxiv

def get_papers(topic, max_results=100):
    client = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    papers = []
    
    for result in client.results():
        paper = {
            'title': result.title,
            'authors': [author.name for author in result.authors],
            'summary': result.summary,
            'published': result.published.isoformat(),
            'url': result.pdf_url
        }
        papers.append(paper)
    
    return papers