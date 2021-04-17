import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespaces(value):
    return value.strip()

class JokeItem(scrapy.Item):
    joke_text = scrapy.Field(
        input_processor= MapCompose(remove_tags, remove_whitespaces),
        output_processor= TakeFirst()
    )