# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import PyRSS2Gen
from datetime import datetime
from scrapy import Spider
from scrapy.selector import Selector


class LostfilmSpider(Spider):
    name = "lostfilm"
    allowed_domains = ["lostfilm.tv"]
    start_urls = ()

    def __init__(self, *args, **kwargs):
        super(LostfilmSpider, self).__init__(*args, **kwargs)
        with open('serials.txt') as f:
            self.start_urls = [u.strip() for u in f.readlines()]

    def parse(self, response):
        sel = Selector(response)

        id = response.url.split('=')[1].strip()
        title = sel.css('.mid h1::text')[0].extract().strip()
        series = []

        mid = sel.css('.mid')[0].xpath('div')[1]
        for div in mid.css('div'):
            try:
                cls = div.xpath('@class')[0].extract()
            except:
                continue

            if cls.startswith('t_row'):
                trs = div.css('tr')

                date = trs[0].css('td')[1].css('span::text')[0].extract().strip()
                number = trs[0].css('td')[1].css('span::text')[2].extract().strip()
                name_ru = trs[1].css('nobr span::text')[0].extract().strip()
                name_en = trs[1].css('nobr::text')[0].extract().strip()
                url = 'https://www.lostfilm.tv%s' % div.css('a::attr(href)')[1].extract().strip()

                item = PyRSS2Gen.RSSItem(
                    title = '%s %s' % (name_ru, name_en),
                    link = url,
                    description = number,
                    pubDate = datetime.strptime(date, '%d.%m.%Y %H:%M')
                )
                series.append(item)


        feed = PyRSS2Gen.RSS2(
            title=title,
            link="https://www.lostfilm.tv/browse.php?cat=%s" % id,
            description='',
            lastBuildDate=datetime.now(),
            items=series
        )

        with open("rss/%s.xml" % id, "w") as f:
            feed.write_xml(f, encoding='utf-8')
            
