# -*- coding: utf-8 -*-
import requests


class prettygirlPipeline(object):
    def process_item(self, item, spider):
        detailURL=item['detailURL']
        path=item['path']
        fileName=item['fileName']

        image=requests.get(detailURL)
        with open(path,'wb') as f:
            f.write(image.content)
        print u'正在保存图片：',detailURL
        print u'图片路径：',path
        print u'文件：',fileName
        return item
