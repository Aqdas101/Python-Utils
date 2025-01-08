
# dependency: ! pip install ultimate-sitemap-parser

from usp.tree import sitemap_tree_for_homepage

website_name = 'https://www.techmazone.com/'
tree = sitemap_tree_for_homepage(website_name)
urls = [page.url for page in tree.all_pages()]
print(urls)
