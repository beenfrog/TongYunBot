#coding=UTF-8
from collections import defaultdict
import io

import sys
if sys.version_info[0] < 3:
	reload(sys)
	sys.setdefaultencoding('utf8')
else:
	from functools import cmp_to_key

class Yun():
	def __init__(self, yunbiao_filename, hanzibiao_filename):
		self.yunbiao_filename   = yunbiao_filename
		self.hanzibiao_filename = hanzibiao_filename
		
		self.yunbiao, self.hanzibiao = self.read_dataset()
		self.sort_yunbiao()

	
	def read_dataset(self):
		yunbiao = defaultdict(dict)
		keyfound = []
		with io.open(self.yunbiao_filename, 'r', encoding='UTF-8') as fid:
			for line in fid:
				line = line.strip()
				if len(line) > 0:
					items = line.split()
					bigkey = items[0]
					smallkey = items[1]
					order    = int(items[2])
					hanzi_list = items[3:]

					keythis = bigkey + smallkey
					if keythis in keyfound:
						yunbiao[bigkey][smallkey][order-1] = hanzi_list
					else:
						yunbiao[bigkey][smallkey] = [None] * 4
						yunbiao[bigkey][smallkey][order-1] = hanzi_list
						keyfound.append(keythis)
		fid.close()

		hanzibiao = {}
		with io.open(self.hanzibiao_filename, 'r', encoding='UTF-8') as fid:
			line = fid.readline()
			item_list = list(line.strip())
			item_list.pop(0) # delete first unicode label
			for idx,item in enumerate(item_list):
				hanzibiao[item] = idx
			
		fid.close()

		return yunbiao, hanzibiao

	def sort_yunbiao(self):
		def cmp_hanzi(ch1, ch2):
			is_ch1 = ch1 in self.hanzibiao
			is_ch2 = ch2 in self.hanzibiao
			if is_ch1 and is_ch2:
				return self.hanzibiao[ch1] - self.hanzibiao[ch2]
			if is_ch1 and not is_ch2:
				return -1
			if not is_ch1 and  is_ch2:
				return 1
			if not is_ch1 and not is_ch2:
				return 0

		for bigkey in self.yunbiao:
			for smallkey in self.yunbiao[bigkey]:
				for order in range(4):
					oldlist = self.yunbiao[bigkey][smallkey][order]
					if sys.version_info[0] < 3:
						newlist = sorted(oldlist, cmp = cmp_hanzi)
					else:
						newlist = sorted(oldlist, key = cmp_to_key(cmp_hanzi))
					self.yunbiao[bigkey][smallkey][order] = newlist

	def same(self, hanzi):
		hanzi = hanzi[-1]
		same_list = []
		for bigkey in self.yunbiao:
			for smallkey in self.yunbiao[bigkey]:
				for order in range(4):
					if hanzi in self.yunbiao[bigkey][smallkey][order]:
						same_list.append(self.yunbiao[bigkey][smallkey][order])
						for smallkey2 in self.yunbiao[bigkey]:
							if smallkey2 != smallkey:
								same_list.append(self.yunbiao[bigkey][smallkey2][order])
		return same_list

	def same_print(self, hanzi):
		same_list = self.same(hanzi)
		outstring  = hanzi + "\n"
		for item in same_list:
			outstring = outstring + "〇∙" + "∙".join(item) + "\n"

		return outstring


if __name__ == "__main__":
	tongyun = Yun("./yunbiao.txt", "./hanzi.txt")
	print(tongyun.same_print("韵"))
