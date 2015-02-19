# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import PyRSS2Gen
from datetime import datetime
from scrapy import Spider
from scrapy.selector import Selector


class LostfilmSpider(Spider):
    name = "lostfilm"
    allowed_domains = ["lostfilm.tv"]
    start_urls = (
        'http://lostfilm.tv/browse.php?cat=236',
        'http://lostfilm.tv/browse.php?cat=235',
        'http://lostfilm.tv/browse.php?cat=190',
        'http://lostfilm.tv/browse.php?cat=162',
        'http://lostfilm.tv/browse.php?cat=163',
        'http://lostfilm.tv/browse.php?cat=157',
        'http://lostfilm.tv/browse.php?cat=110',
        'http://lostfilm.tv/browse.php?cat=233',
        'http://lostfilm.tv/browse.php?cat=210',
        'http://lostfilm.tv/browse.php?cat=153',
        'http://lostfilm.tv/browse.php?cat=125',
        'http://lostfilm.tv/browse.php?cat=198',
        'http://lostfilm.tv/browse.php?cat=206',
        'http://lostfilm.tv/browse.php?cat=227',
        'http://lostfilm.tv/browse.php?cat=111',
        'http://lostfilm.tv/browse.php?cat=219',
        'http://lostfilm.tv/browse.php?cat=119',
        'http://lostfilm.tv/browse.php?cat=232',
        'http://lostfilm.tv/browse.php?cat=101',
        'http://lostfilm.tv/browse.php?cat=52',
        'http://lostfilm.tv/browse.php?cat=195',
        'http://lostfilm.tv/browse.php?cat=169',
        'http://lostfilm.tv/browse.php?cat=115',
        'http://lostfilm.tv/browse.php?cat=225',
        'http://lostfilm.tv/browse.php?cat=160',
        'http://lostfilm.tv/browse.php?cat=223',
        'http://lostfilm.tv/browse.php?cat=123',
        'http://lostfilm.tv/browse.php?cat=187',
        'http://lostfilm.tv/browse.php?cat=114',
        'http://lostfilm.tv/browse.php?cat=51',
        'http://lostfilm.tv/browse.php?cat=217',
        'http://lostfilm.tv/browse.php?cat=193',
        'http://lostfilm.tv/browse.php?cat=121',
        'http://lostfilm.tv/browse.php?cat=93',
        'http://lostfilm.tv/browse.php?cat=179',
        'http://lostfilm.tv/browse.php?cat=96',
        'http://lostfilm.tv/browse.php?cat=228',
        'http://lostfilm.tv/browse.php?cat=109',
        'http://lostfilm.tv/browse.php?cat=145',
        'http://lostfilm.tv/browse.php?cat=212',
        'http://lostfilm.tv/browse.php?cat=140',
        'http://lostfilm.tv/browse.php?cat=199',
        'http://lostfilm.tv/browse.php?cat=137',
        'http://lostfilm.tv/browse.php?cat=143',
        'http://lostfilm.tv/browse.php?cat=117',
        'http://lostfilm.tv/browse.php?cat=129',
        'http://lostfilm.tv/browse.php?cat=149', 
        'http://lostfilm.tv/browse.php?cat=203', 
        'http://lostfilm.tv/browse.php?cat=230', 
        'http://lostfilm.tv/browse.php?cat=46', 
        'http://lostfilm.tv/browse.php?cat=229', 
        'http://lostfilm.tv/browse.php?cat=165', 
        'http://lostfilm.tv/browse.php?cat=170', 
        'http://lostfilm.tv/browse.php?cat=177', 
        'http://lostfilm.tv/browse.php?cat=178',
        'http://lostfilm.tv/browse.php?cat=183', 
        'http://lostfilm.tv/browse.php?cat=222', 
        'http://lostfilm.tv/browse.php?cat=237',
        'http://lostfilm.tv/browse.php?cat=151', 
        'http://lostfilm.tv/browse.php?cat=192', 
        'http://lostfilm.tv/browse.php?cat=108', 
        'http://lostfilm.tv/browse.php?cat=188', 
        'http://lostfilm.tv/browse.php?cat=184', 
        'http://lostfilm.tv/browse.php?cat=204', 
        'http://lostfilm.tv/browse.php?cat=224', 
        'http://lostfilm.tv/browse.php?cat=126', 
        'http://lostfilm.tv/browse.php?cat=185', 
        'http://lostfilm.tv/browse.php?cat=104', 
        'http://lostfilm.tv/browse.php?cat=141', 
        'http://lostfilm.tv/browse.php?cat=30', 
        'http://lostfilm.tv/browse.php?cat=197', 
        'http://lostfilm.tv/browse.php?cat=213',
        'http://lostfilm.tv/browse.php?cat=64',
        'http://lostfilm.tv/browse.php?cat=231', 
        'http://lostfilm.tv/browse.php?cat=191', 
        'http://lostfilm.tv/browse.php?cat=181', 
        'http://lostfilm.tv/browse.php?cat=215', 
        'http://lostfilm.tv/browse.php?cat=186', 
        'http://lostfilm.tv/browse.php?cat=159', 
        'http://lostfilm.tv/browse.php?cat=136', 
        'http://lostfilm.tv/browse.php?cat=218', 
        'http://lostfilm.tv/browse.php?cat=182', 
        'http://lostfilm.tv/browse.php?cat=194', 
        'http://lostfilm.tv/browse.php?cat=168', 
        'http://lostfilm.tv/browse.php?cat=211', 
        'http://lostfilm.tv/browse.php?cat=173', 
        'http://lostfilm.tv/browse.php?cat=167', 
        'http://lostfilm.tv/browse.php?cat=221', 
        'http://lostfilm.tv/browse.php?cat=161', 
        'http://lostfilm.tv/browse.php?cat=209', 
        'http://lostfilm.tv/browse.php?cat=65', 
        'http://lostfilm.tv/browse.php?cat=150',
        'http://lostfilm.tv/browse.php?cat=196',
        'http://lostfilm.tv/browse.php?cat=189', 
        'http://lostfilm.tv/browse.php?cat=207', 
        'http://lostfilm.tv/browse.php?cat=147', 
        'http://lostfilm.tv/browse.php?cat=139',
        'http://lostfilm.tv/browse.php?cat=180',
        'http://lostfilm.tv/browse.php?cat=116',
        'http://lostfilm.tv/browse.php?cat=164',
        'http://lostfilm.tv/browse.php?cat=200', 
        'http://lostfilm.tv/browse.php?cat=128',
        'http://lostfilm.tv/browse.php?cat=176', 
        'http://lostfilm.tv/browse.php?cat=95', 
        'http://lostfilm.tv/browse.php?cat=158', 
        'http://lostfilm.tv/browse.php?cat=103', 
        'http://lostfilm.tv/browse.php?cat=148', 
        'http://lostfilm.tv/browse.php?cat=154', 
        'http://lostfilm.tv/browse.php?cat=201', 
        'http://lostfilm.tv/browse.php?cat=172', 
        'http://lostfilm.tv/browse.php?cat=234', 
        'http://lostfilm.tv/browse.php?cat=208', 
        'http://lostfilm.tv/browse.php?cat=205',
        'http://lostfilm.tv/browse.php?cat=226', 
        'http://lostfilm.tv/browse.php?cat=127', 
        'http://lostfilm.tv/browse.php?cat=134', 
        'http://lostfilm.tv/browse.php?cat=105', 
        'http://lostfilm.tv/browse.php?cat=216', 
        'http://lostfilm.tv/browse.php?cat=202', 
        'http://lostfilm.tv/browse.php?cat=214', 
        'http://lostfilm.tv/browse.php?cat=130', 
        'http://lostfilm.tv/browse.php?cat=220', 
        'http://lostfilm.tv/browse.php?cat=37', 
        'http://lostfilm.tv/browse.php?cat=174',
    )

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
            items=series
        )

        with open("rss/%s.xml" % id, "w") as f:
            feed.write_xml(f)
            
