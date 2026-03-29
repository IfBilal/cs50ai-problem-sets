import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    ans = dict()
    if not corpus[page]:
        val = 1 / len(corpus)
        return {x : val for x in corpus}
    for x in corpus[page]:
        ans[x] = damping_factor / len(corpus[page]) + (1 - damping_factor) / len(corpus)
    for x in corpus:
        if x not in ans:
            ans[x] = (1 - damping_factor) / len(corpus)
    return ans


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    ans  =  { x : 0 for x in corpus }
    currentPage = random.choice(list(corpus.keys()))
    for x in range(n):
        ans[currentPage] += 1
        next = transition_model(corpus,currentPage,damping_factor)
        currentPage = random.choices(population = list(next.keys()), weights = list(next.values()), k = 1)[0]
    for x in ans:
        ans[x] = ans[x] / n
    return ans


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ans = { x : 1 / len(corpus) for x in corpus }
    while True:
        new_ranks = {}
        for x in corpus:
            new_ranks[x] = (1-damping_factor) / len(corpus)
            for y in corpus:
                if x in corpus[y]:
                    new_ranks[x] += damping_factor * (ans[y] / len(corpus[y]))
                elif not corpus[y]:
                    new_ranks[x] += damping_factor * (ans[y] / len(corpus))
        doBreak = all(abs(ans[x] - new_ranks[x]) < 0.001 for x in new_ranks)
        if doBreak:
            break
        for x in ans:
            ans[x] = new_ranks[x]
    return ans

if __name__ == "__main__":
    main()
