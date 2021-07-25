from urllib.parse import urljoin
import scrapy

class AttractionsSpider(scrapy.Spider):
    name = 'attractions'
    
    country_id = {
        "istanbul":35100,
        "florence":381000
    }

    def start_requests(self):
        urls = [ 
                f'https://www.lonelyplanet.com/europe/attractions?page={page}' for page in range(1,2)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'handle_httpstatus_list': [301]})  #meta={'dont_redirect': True}
            
        
    def parse(self, response):
        for post in response.css("div.mb-32"):   #.lg:mr-32
            top_choice = post.css('p.jsx-2276123283 span.jsx-2276123283.mr-4::text').get()
            title = post.css('h2.text-xl.text-primary.font-medium.leading-tight.mb-8::text').get()
            #description = post.css('p.text-sm.text-primary.font-light.leading-relaxed::text').get()
            link = post.css('a.jsx-2276123283.flex.flex-col.items-center::attr(href)').get()
            
            link_split = link.split("/")
            
            data = { 
                   'top_choice'     : top_choice, 
                   'title'          : title, 
                   #'desc'           : description, 
                   'link'           : link,
                   'country'        : link_split[1],
                   'city'           : link_split[2],
                   'country_id'    : AttractionsSpider.country_id.get(link_split[2])
            }
            
            yield  scrapy.Request(url = response.urljoin(link), callback = self.parse_detail, meta= data)
            
           
            
    def parse_detail(self,response):
        #website = response.css("li.jsx-1718619389.flex.mt-8:nth-child(2) a::attr(href)").get()
        website = None
        address = None
        price = None
        for detail_html in response.css("li.jsx-1718619389.flex"):
            #print(detail_html.css("span::text"))
            if detail_html.css("span::text").get() == "Website":
                #get == extract_first
                #website = detail_html.css("a::attr(href)").get()
                website = detail_html.css("a::attr(href)").extract_first()
                
            elif detail_html.css("span::text").get() == "Address":
                address = detail_html.css(":not(span)::text").extract_first()
                
            elif detail_html.css("span::text").get() == "Price":
                price = detail_html.css(":not(span)::text").extract_first()

        
        desc = ""
        for p_detail in response.css("section.jsx-3858112237.body.mt-16 p"):
            desc += p_detail.css("::text").get()
            
            
        yield{
            "website"       : website,
            "address"       : address,
            "price"         : price,
            "top_choice"    : response.meta['top_choice'],
            "title"         : response.meta['title'],
            "desc"          : desc,
            "link"          : response.meta['link'],
            "country"       : response.meta['country'],
            "city"          : response.meta['city'],
            "country_id"    : response.meta['country_id'],
        }


