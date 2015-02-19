# -*- coding: utf-8 -*-

# Scrapy settings for lostrss project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lostrss'

SPIDER_MODULES = ['lostrss.spiders']
NEWSPIDER_MODULE = 'lostrss.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lostrss (+http://www.yourdomain.com)'


# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 31536000