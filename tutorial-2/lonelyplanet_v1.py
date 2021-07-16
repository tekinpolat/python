import scrapy


class LonelPlanetSpider(scrapy.Spider):
    name = 'attractionspider'
    
    start_urls = ['https://www.lonelyplanet.com/europe/attractions']
    
    def parse(self, response):
        
        #topic = response.css("h1.my-20.text-xl.font-medium::text").get()
        #print(topic)
        #yield {'topic':topic}
        
        for post in response.css("div.mb-32"):   #.lg:mr-32
            top_choice = post.css('p.jsx-2276123283 span.jsx-2276123283.mr-4::text').get()
            title = post.css('h2.text-xl.text-primary.font-medium.leading-tight.mb-8::text').get()
            description = post.css('p.text-sm.text-primary.font-light.leading-relaxed::text').get()
            link = post.css('a.jsx-2276123283.flex.flex-col.items-center::attr(href)').get()
            
            yield { 'top_choice' : top_choice, 'title':title, 'desc': description, 'link':link}
            
        for next_page in response.css('svg.jsx-2420936032.lm-icon.jsx-3750009544'):
            print("next page")
            yield response.follow(next_page, self.parse)
            
            
        #jsx-3750009544 lm-pill pill