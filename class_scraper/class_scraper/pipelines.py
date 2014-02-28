# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import unicodedata
class CleanUnicodePipeline(object):

    def process_item(self, item, spider):
        for key in item:
           # try:
                clean_str = item[key].decode('utf8', 'ignore')
                item[key] = unicodedata.normalize('NFKC', clean_str).replace(',', '&#44;')
            #except:
                #print('Error cleaning item elements: '+str(item))
        return item
                
class WritePipeline(object):

    def process_item(self, item, spider):
        if item:
            f = open('classes.csv', 'a')
            new_data = ''
            for key in ['major','course_code','course_name', 'units', 'department', 'course_level', 'terms_offered', 'grading', 'hours_format', 'description']:
                new_data +=u'{},'.format(item[key])
            f.write('{}\n'.format(new_data.rstrip(',')))
            f.flush()
        else:
            print('Error scraping Data.')
