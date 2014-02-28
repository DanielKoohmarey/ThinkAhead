from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from class_scraper.items import CourseInfoItem

class UCBClassSpider(Spider):
    name = "ucbclasses"
    allowed_domains = ["bulletin.berkeley.edu"]
    start_urls = [
        "http://bulletin.berkeley.edu/courses/"
    ]

    def parse(self, response):
       """ Parse is initially called by default on the response(s) from start_urls """
       sel = Selector(response)
       
       #Iterate over all the markets, get the ids associated with a given market
       majors = sel.xpath('//div[@class="sitemap"]/ul/li')
       for major in majors:
           yield Request(response.url+major.xpath('a/@href').extract()[0].encode('utf-8').replace('/courses/',''),callback=self.parse_class) #'/courses/aerospc/'

    def parse_class(self, response):
        info = CourseInfoItem()
        sel = Selector(response)
        courses = sel.xpath('//div[@class="courseblock"]') #assuming on course page i.e http://bulletin.berkeley.edu/courses/aerospc/
        major = sel.xpath('//h1/text()').extract()[0].encode('utf-8')
        major_name = major[major.find('('):].strip('()')
        info['major'] = major 
        for course in courses:
            course_code = course.xpath('p/span[@class="code"]/text()').extract()[0].encode('utf-8') #'AEROSPC\xc2\xa01A'
            info['course_code'] = course_code.replace(major_name,'').strip('\xc2\xa0')
            info['course_name'] = course.xpath('p/span[@class="title"]/text()').extract()[0].encode('utf-8') # Foundations of the U.S. Air Force
            info['units'] = course.xpath('p/span[@class="hours"]/text()').extract()[0].encode('utf-8') # '1 Unit'
            info['department'], info['course_level'], info['terms_offered'], info['grading'], info['hours_format'], info['description'] =  [elem.encode('utf-8') for elem in course.xpath('p/text()').extract()[4:10]]
            yield info