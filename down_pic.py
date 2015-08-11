Enter file contents here
#/usr/bin/python
'''
def read_dir_first_page(file1,file2)
	root="http://www.169pp.com"
	f2=File.open(file2,"a")
	x=[]
	#puts file1
	File.open(file1,"r").each do |line|
		http=open(line.chomp!)
		str=http.read
		str.encoding
		list=str.scan(/a\s+href\=(\/News\/\d+\-\d+\-\d+\/\d+\.htm)\s+title/)
		list.each do |i|
			i.each do |b|
				b=root+b
				#puts b
				x<<b
			end
		end
		#p str
		x.uniq!
		x.each do |i|
			f2.puts i
		end
	end
end
'''

import urllib
import re

def output_root_dir(t,file):
	f=open(file,'w+')
	for i in range(1,t):
		f.write('http://www.169pp.com/info/4_%d.htm\n' % i)
		print 'http://www.169pp.com/info/4_%d.htm' % i
	f.close()

def read_dir_first_page(file,file2):
	root="http://www.169pp.com"
	f2=open(file2,"a")
	for line in open(file):
		line=line.strip("\r\n")
		page = urllib.urlopen(line)
		html = page.read()
		print html

if __name__ == "__main__":
	file="page.txt"
	file2='page2.txt'
	t=3
	output_root_dir(t,file)
	read_dir_first_page(file,file2)
