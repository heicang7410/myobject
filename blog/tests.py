#coding:utf8
from django.test import TestCase
from blog.long import Long_url
from blog.models import Url
class ShortTest(TestCase):
    
    def setUp(self):
   #     Url.objects.create(long_url='http://www.pythoner.cn/home/blog/python_pythoner_cn_2013070801/',short_url='')
        Url.objects.create(long_url='https://github.com/travis-ci/issues/new',short_url='abc123')

    def test_l_s(self):
        """
        测试长url会不会缩短成六位的字符串
        """
        l1='http://www.pythoner.cn/blog/pythoner_cn_2013070801/'
        self.assertEqual(Long_url(l1),'4fdf9t')
    def test_have(self):
        """
        测试已创建的url是否能正常的返回
        """
        l2=Url.objects.filter(long_url='https://github.com/travis-ci/issues/new')
        self.assertEqual(Long_url(l2[0]),'abc123')
        
