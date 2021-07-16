import scrapy


class LonelPlanetSpider(scrapy.Spider):
    name = 'attractionspider'
    #page = 2
    #start_urls = ['https://www.lonelyplanet.com/europe/attractions']
    
    
    def start_requests(self):
        urls = [ f'https://www.lonelyplanet.com/europe/attractions?page={page}' for page in range(1,101)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        

        for post in response.css("div.mb-32"):   #.lg:mr-32
            top_choice = post.css('p.jsx-2276123283 span.jsx-2276123283.mr-4::text').get()
            title = post.css('h2.text-xl.text-primary.font-medium.leading-tight.mb-8::text').get()
            description = post.css('p.text-sm.text-primary.font-light.leading-relaxed::text').get()
            link = post.css('a.jsx-2276123283.flex.flex-col.items-center::attr(href)').get()
            
            yield { 'top_choice' : top_choice, 'title':title, 'desc': description, 'link':link}
            
        
