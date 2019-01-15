from scrapy import cmdline

name = 'ljesf'

cmd ='scrapy crawl %s'%name

cmdline.execute(cmd.split())