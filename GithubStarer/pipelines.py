# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class GithubstarerPipeline(object):
    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/starers.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(str(item['serial_number']) + '\t')
            f.write(item['user_name'] + '  \r\n')
        return item
