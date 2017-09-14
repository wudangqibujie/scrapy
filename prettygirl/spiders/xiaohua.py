# -*- coding:utf-8 -*-
import scrapy
import re
import os
from prettygirl.items import prettygirl
from scrapy.http import Request
import requests

class test(scrapy.Spider):
    name='test'
    base='/root/meinv/'
    allowd_domains=['mmonly.cc']
    def start_requests(self):
        for i in range(1,7):
            url='http://www.mmonly.cc/tag/xh1/'+str(i)+'.html'
            yield Request(url,callback=self.parse_one)


    def parse_one(self,response):
        items=[]
        pattern=re.compile(r'<div class="title"><span><a target="_blank" href="(.*?)">(.*?)</a></span></div>',re.S)
        mains=re.findall(pattern,response.text)
        for main in mains:
            item=XiaohuaItem()
            item['siteURL']=main[0]
            item['title']=main[1]
            item['fileName']=self.base+item['title']
            items.append(item)
        for item in items:
            fileName=item['fileName']
            if not os.path.exists(fileName):
                os.makedirs(fileName)
            
            yield Request(url=item['siteURL'],meta={'item1':item},callback=self.parse_two)
    def parse_two(self,response):
        item2=response.meta['item1'] 
        URL=response.url 
        html=requests.get(URL).text.encode('utf-8')
        a=re.compile(r'共(.*?)页:')
        b=re.search(a,html).group(1)
        items=[]
        for i in range(1,int(b)+1):
            item=XiaohuaItem()
            item['pageURL']=URL[:-5]+'_'+str(i)+'.html'
            item['fileName']=item2['fileName']
            item['path']=item['fileName']+'/'+str(i)+'.jpg'
            items.append(item)
        for item in items:
            yield Request(url=item['pageURL'],meta={'item2':item},callback=self.parse_three)

    def parse_three(self,response):
        item3=response.meta['item2']
        items=[]
        item=XiaohuaItem()
        c=response.text 
        a=re.compile(r'<li class="pic-down h-pic-down"><a target="_blank" class="down-btn" href=\'(.*?)\'>')
        b=re.search(a,c).group(1)
        item['detailURL']=b
        item['path']=item3['path']
        item['fileName']=item3['fileName']
        yield item
        
        
            
            
        
        


