__author__ = 'zhenbangxiao'

import urllib2

url = 'http://www.weibo.com'
response = urllib2.urlopen(url)
print response.read().decode('gb2312').encode('utf8')       ## Compulsory for some Simplified Chinese websites