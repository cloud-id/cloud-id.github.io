# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup


class Case(object):
	"""docstring for Case"""
	def __init__(self):
		self.title = ''
		self.thumb = ' '
		self.subtitle = ' '
		self.back = ' '
		self.slove = ' '
		self.content = []
		self.img_list = []
		self.render_img_list = []
		pass
	def feed(self,url):
		html_doc = open(url).read()
		soup = BeautifulSoup(html_doc)
		self.title = soup.title.get_text()				
		for i in soup.find_all('p'):
			self.content.append(i.get_text().encode('utf-8'))  
		for i in soup.find_all('img'):
			self.img_list.append(i['src'].encode('utf-8')) 

		self.back = self.get_back()
		self.slove = self.get_slove()
		self.get_img_list()
		return 
		pass

	def get_back(self):
		start=-2;
		end=-2;
		for i in self.content:
			if (('Project background:')in i):
				start = self.content.index(i)
			if (('Cloud-ID solutions:')in i):
				end = self.content.index(i)
		return '<br>\n'.join(self.content[start+1:end])
	def get_slove(self):
		start = -2;
		end = -2;
		for i in self.content:
			if (('Based on the above requirements')in i):
				start = self.content.index(i)
			if (i.startswith('Photos of the event')):
				end = self.content.index(i)
		return '<br>\n'.join(self.content[start+1:end])
	def get_img_list(self):
		self.thumb = ''+self.img_list[0]
		for i in self.img_list :
			self.img_list[self.img_list.index(i)] = '''<img class="img-responsive" src="BLOG_IMG">'''.replace('BLOG_IMG',i)
	def render(self):
		template='''
                <li>
                  <h5>Project：BLOG_TITLE </h5>
                  <p><img width="100%" src="BLOG_THUMB"></p>
                  <div class="overview hide">
                    <div class="col-md-8 col-md-offset-2 overview-content">
                      <a class="close">&times;</a>
                      <h4>Project：BLOG_TITLE</h4>
                      <h5>Project background :</h5>
                      <p>BLOG_BACK </p>
                      <h5>Cloud-ID solutions:<br>Based on the above requirements of the Sponsor and combined with the background of the event, we finally have implemented the following solutions:</h5>
                      <p>
             			BLOG_SLOVE
                        </p>
                      <h5>Photos of the event:</h5>
                      BLOG_IMG_LIST
                      
                    </div>
                  </div>
                </li>
		'''
		out = template.replace('BLOG_TITLE',(self.title).encode('utf-8'))
		out = out.replace('BLOG_BACK',self.back)
		out = out.replace('BLOG_SLOVE',self.slove)
		out = out.replace('BLOG_THUMB',self.thumb)
		out = out.replace('BLOG_IMG_LIST','\n'.join(self.img_list))
		return out
a = Case();
# a.feed('BASF MDI_TDI Project 10th Anniversary Dinner.html')
# print a.render()


#print a.slove
#print a.render()
import os
for filename in os.listdir(r'.'):
    if filename.endswith('.html'):
    	a = Case();
    	a.feed(filename)
    	print a.render()
		