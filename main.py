from Import import *

class Currency:
    def __init__(self, option="sell", curr="usd", city="kiev"):
        self.url = f"https://minfin.com.ua/currency/auction/{curr}/{option}/{city}/"
    def adr(self):
        self.r = requests.get(self.url, timeout=5)  # get html from request
        self.soup2 = BeautifulSoup(self.r.text, 'lxml').find_all('span', class_="text-address")  # cook with bs4
        a=[]
        for item in self.soup2:
            a.append(BeautifulSoup(str(item),"lxml").get_text())
        #print a list of adress(commented)
        #print(a)
        # return a list of adress
        return a
        # option sell like standart
    def currence(self):
        # get html from request
        self.r=requests.get(self.url, timeout=5)
        # cook with bs4
        self.soup = BeautifulSoup(self.r.text, 'lxml').find_all('div', class_="Typography cardHeadlineL align")
        # create empty list
        a=list()
        # get componets from list of html elements
        for item in self.soup:
            a.append(BeautifulSoup(str(item), "lxml").get_text())#
        b=list()
        for s in a:
            b1=(s.replace(" USD","")).replace(",", ".")
            b.append(float(b1))
        # create new value for return list values(commented)
        print(b)
        # get result from list
        print(self.url)
        #return list of numbers
        return b
        def mean(b):
            mea=round(sum(b)/len(b), 2)
            return mea
        print("Min:\n",min(b),"\nMax:\n", max(b), "\nMean:\n", mean(b))

    def find(self):
        b=self.currence()
        a=self.adr()
        try:
            #print(a)
            #Adress of element with minimum element,
            print("Min:\n",a[b.index(min(b))])
            print("Max:\n",a[b.index(max(b))])
        except:
            pass

    def nearest(self):
        # return list of numbers
        b=self.currence()
        a=self.adr()
        boj = sum(b) / len(b)
        ben = b.copy()
        ben.sort()
        rou = round(boj, 2)
        c = []
        for s in ben:
            if s < rou:
                c.append(s)
        print("adress:", a)
        print("Row of prices", c)
        print("List of adresses:")
        prev=None
        for item in c:
            print(a[c.index(item)], "Price:--", item)
            a.remove(a[c.index(item)])
            #a.remove((c.index(item)) //list.remove(x): x not in list
_first=Currency()
#(commented) call of funtions //now in unneedable because we call find()
"""_first.adr()
_first.currence()
_first.find()"""
_first.nearest()