# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CourseInfoItem(Item):
    major = Field()
    course_code = Field()
    course_name = Field()
    units = Field()
    department = Field()
    course_level = Field()
    terms_offered = Field()


