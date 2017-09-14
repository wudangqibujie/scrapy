from scrapy import cmdline


name = 'test'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
