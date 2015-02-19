# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from scrapy import Spider
from scrapy.selector import Selector


class SerialsSpider(Spider):
    name = "serials"
    allowed_domains = ["lostfilm.tv"]
    start_urls = (
        'http://www.lostfilm.tv/serials.php',
    )

    def parse(self, response):
        sel = Selector(response)

        serials = []

        for a in sel.css('.shadow .bb a.bb_a'):
            name = ' '.join(a.css('::text').extract())
            url = a.css('::attr(href)').extract()[0].strip()
            id = url.split('=')[1].strip('_')

            serials.append({
                'id': id,
                'name': name,
                'url': 'http://www.lostfilm.tv%s' % url,
            })

        with open('README.md', 'w') as f:
            f.write('# LostFilm RSS\n\n')
            for serial in serials:
                s = '* [%s](https://rawgit.com/onrik/lostrss/master/rss/%s.xml)\n' % (serial['name'], serial['id'])
                f.write(s.encode('utf-8'))

        with open('serials.txt', 'w') as f:
            for serial in serials:
                f.write('%s\n' % serial['url'])
            
