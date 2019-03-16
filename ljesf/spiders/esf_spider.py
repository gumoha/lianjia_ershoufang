import scrapy
import logging,re,time,random
from ljesf.items import LjesfItem




class ErShouFang(scrapy.Spider):
    name = 'ljesf'
    allowed_domains = ['lianjia.com']

    def start_requests(self):
        cd_esf = 'https://cd.lianjia.com/ershoufang/'
        yield scrapy.Request(cd_esf,callback=self.parse_district)

    #获取区域
    def parse_district(self,response):
        url = 'https://cd.lianjia.com'
        #['/ershoufang/jinjiang/', '/ershoufang/qingyang/']
        districts = response.xpath('//div[contains(@data-role,"ershoufang")]/div/a/@href').extract()
        dinums =1
        for di in districts:
            di_url = url + di
            time.sleep(random.choice(range(10)))
            print('获取大区域链接', dinums, di_url)
            dinums +=1
            yield scrapy.Request(di_url,callback=self.parse_block)

    def parse_block(self,response):
        url = 'https://cd.lianjia.com'

        blocks = response.xpath('//div[contains(@data-role,"ershoufang")]/div/a/@href').extract()

        blnums =1
        for bl in blocks:
            bl_url = url + bl
            time.sleep(random.choice(range(10)))
            print('获取区域——街区链接', blnums, bl_url)
            blnums += 1
            yield scrapy.Request(bl_url, callback=self.parse_pg)

    def parse_pg(self,response):
        pages =(int(response.xpath('//div[@class="resultDes clear"]/h2/span/text()').extract_first().strip()) // 30) +2

        pg_url = response.url + 'pg'
        for n in range(1,pages):
            next_url = pg_url + str(n)
            time.sleep(random.choice(range(10)))

            yield scrapy.Request(next_url,callback=self.parse_house)

    def parse_house(self,response):
        hs = response.xpath('//li[@class="clear LOGCLICKDATA"]/div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for h in hs:
            time.sleep(random.choice(range(10)))
            yield scrapy.Request(h,callback=self.parse_item)


    def parse_item(self, response):
        print('获取房源信息——>%s'%response.url)

        item = LjesfItem()

        item['houselink'] = response.url
        item['houseID'] = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()').extract_first()
        item['housename'] = response.xpath('//h1/@title').extract_first()

        try:
            item['time_build'] = response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract_first()
        except:
            item['time_build'] = None
        try:
            item['totalprice'] = response.xpath(
                '//div[contains(@class,"price")]/span[contains(@class,"total")]/text()').extract_first()
        except:
            item['totalprice'] = None
        try:
            item['unitprice'] = response.xpath(
                '//div[@class="unitPrice"]/span[@class="unitPriceValue"]/text()').extract_first()
        except:
            item['unitprice'] = None
        try:
            item['community'] = response.xpath(
                '//div[contains(@class,"communityName")]/a[contains(@class,"info")]/text()').extract_first()
        except:
            item['community'] = None

        # 区，范围，环路
        try:
            item['district'] = \
            response.xpath('//div[contains(@class,"areaName")]/span[contains(@class,"info")]/a/text()').extract()[0]
        except:
            item['district'] = None
        try:
            item['block'] = \
            response.xpath('//div[contains(@class,"areaName")]/span[contains(@class,"info")]/a/text()').extract()[1]
        except:
            item['block'] = None
        try:
            item['road'] = \
            response.xpath('//div[contains(@class,"areaName")]/span[contains(@class,"info")]/text()').extract()[
                1].strip()
        except:
            item['road'] = None
        try:
            item['supplement'] = response.xpath(
                '//div[contains(@class,"areaName")]/a[contains(@class,"supplement")]/text()').extract_first()
        except:
            item['supplement'] = None

        # 基本信息
        try:
            item['type_house'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[1]/text()').extract_first()
        except:
            item['type_house'] = None
        try:
            item['area_gross'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[3]/text()').extract_first()
        except:
            item['area_gross'] = None
        try:
            item['area_real'] = re.search(r'\d+', response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[5]/text()').extract_first()).group()
        except:
            item['area_real'] = None
        try:
            item['orientation'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[7]/text()').extract_first()
        except:
            item['orientation'] = None
        try:
            item['decoration'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[9]/text()').extract_first()
        except:
            item['decoration'] = None
        try:
            item['own_time'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[12]/text()').extract_first()
        except:
            item['own_time'] = None
        try:
            item['floor'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[2]/text()').extract_first()
        except:
            item['floor'] = None
        try:
            item['layout'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[4]/text()').extract_first()
        except:
            item['layout'] = None
        try:
            item['type_building'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[6]/text()').extract_first()
        except:
            item['type_building'] = None
        try:
            item['material'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[8]/text()').extract_first()
        except:
            item['material'] = None
        try:
            item['elevator_num'] = response.xpath(
                '//div[contains(@class,"base")]/div[contains(@class,"content")]/ul/li[10]/text()').extract_first()
        except:
            item['elevator_num'] = None

        # 交易信息
        try:
            item['time_listing'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                0]
        except:
            item['time_listing'] = None
        try:
            item['time_deal'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                2]
        except:
            item['time_deal'] = None
        try:
            item['time_limit'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                4]
        except:
            item['time_limit'] = None
        try:
            item['property'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                1]
        except:
            item['property'] = None
        try:
            item['usage_yt'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                3]
        except:
            item['usage_yt'] = None
        try:
            item['own'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                5]
        except:
            item['own'] = None
        try:
            item['pledge'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[@title]/text()').extract_first().strip()
        except:
            item['pledge'] = None
        try:
            item['upload'] = response.xpath(
                '//div[contains(@class,"transaction")]/div[contains(@class,"content")]/ul/li/span[not(@*)]/text()').extract()[
                6]
        except:
            item['upload'] = None

        yield item