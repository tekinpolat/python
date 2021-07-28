import scrapy


class CoreyMsSpider(scrapy.Spider):
    name            = 'corey-ms'
    allowed_domains = ['coreyms.com']
    start_urls      = ['https://coreyms.com/']

    def parse(self, response):
        #print(response)
        #print(dir(response))
        #articles_html = response.css("article.post-1670.post.type-post.status-publish")
        
        ## get() == extract_first()
        articles_html = response.css("article.category-python.entry")
        for article_html in articles_html:
            
            yield{
                "title"      : article_html.css("a.entry-title-link::text").get(),
                "desciption" : article_html.css("div.entry-content p::text").get(),
                "author"     : article_html.css("span.entry-author-name::text").extract_first(),
                "link"       : article_html.css("a.entry-title-link::attr(href)").extract_first()
            }