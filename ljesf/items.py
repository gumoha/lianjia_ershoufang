# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjesfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 30
    houselink = scrapy.Field()  # 房源链接
    houseID = scrapy.Field()  # 链家ID
    housename = scrapy.Field()  # 房源名字
    time_build = scrapy.Field()  # 建筑时间
    totalprice = scrapy.Field()  # 总价
    unitprice = scrapy.Field()  # 单价

    community = scrapy.Field()  # 小区
    district = scrapy.Field()  # 行政区
    block = scrapy.Field()  # 区域范围
    road = scrapy.Field()  # 几环路
    supplement = scrapy.Field()  # 补充信息，地铁

    # 基本信息
    type_house = scrapy.Field()  # 户型
    area_gross = scrapy.Field()  # 建筑面积
    area_real = scrapy.Field()  # 实际面积
    orientation = scrapy.Field()  # 朝向
    decoration = scrapy.Field()  # 装修情况
    own_time = scrapy.Field()  # 产权年限
    floor = scrapy.Field()  # 楼层
    layout = scrapy.Field()  # 户型结构
    type_building = scrapy.Field()  # 建筑类型
    material = scrapy.Field()  # 建筑结构（钢混）
    elevator_num = scrapy.Field()  # 梯户比例（两梯六户）

    # 交易信息
    time_listing = scrapy.Field()  # 挂牌时间
    time_deal = scrapy.Field()  # 上次交易时间
    time_limit = scrapy.Field()  # 房屋年限
    property = scrapy.Field()  # 交易权属
    usage_yt = scrapy.Field()  # 房屋用途
    own = scrapy.Field()  # 产权所有
    pledge = scrapy.Field()  # 抵押信息
    upload = scrapy.Field()  # 上传房本
