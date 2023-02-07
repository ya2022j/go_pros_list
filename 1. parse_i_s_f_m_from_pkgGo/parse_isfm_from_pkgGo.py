


import requests
import os
import re

from bs4 import BeautifulSoup
from lxml import etree


def writeinto_txtfile(filename, data):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")
        f.close()



def output_text(trans_filename,url):
    ret_list = []

    resp = requests.get(url)
    element = etree.HTML(resp.text)

    xpath1 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/a/text()')
    xpath2 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/ul/li/a/text()')
    for item in xpath1:
        ret_list.append(item)
    for item in xpath2:
        ret_list.append(item)

    for item in ret_list:
        writeinto_txtfile(trans_filename, item)

















class Output_Golang_FITM():


    def exec(self):
        self.dt_standby(datafile)
        self.output_method()
        self.output_indepent_func() # ok
        self.output_IT() # ok




    def dt_standby(self,datafile):
        ret = self.readDatafile(datafile)
        for item in ret:
            if "type " in item:
                type_list.append(item.split("type ")[1])
                pass  # interface  or struct
            elif "func" in item and "func (" not in item:
                independent_func_list.append(item)
                # indepent func 在整理独立函数或者方法时，可以把接口或者类型的关系也加入进去

            elif "func (" in item:  # 1.接收器的角度
                method_list.append(item)  # 2. 以方法的实际编写，尤其是返回值的角度




    def output_indepent_func(self):
        print('<li><a href="/">' + '&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;  &nbsp;&nbsp;func:', len(independent_func_list),
              '&nbsp;&nbsp; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; ' + '</a></li> <br>')
        for item in independent_func_list:
            ret = self.get_corre_item_func(item, type_list)
            print('<li><a href="/">&nbsp;&nbsp;' + self.bold_text_indepent(ret) + "&nbsp;&nbsp;</a></li> <br>")
            print("\n")

    def output_IT(self):
        print('<li><a href="/">' +'&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;&nbsp;&nbsp;  type nums:', len(type_list), '&nbsp;&nbsp;&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; '+ '</a></li> <br>')
        for item in type_list:
            print('<li><a href="/">' + item  + "</a></li> <br>")

    def output_method(self):
        try:
            method_ret_list = self.method_dt_standby()
            final_list = []
            for item in type_list:
                item_list = [item]
                for value in method_ret_list:

                    if self.bold_text_type_str(value) == item or self.bold_text_type_str(value) == "*"+item:
                        item_list.append(value)
                final_list.append(item_list)
            for one_type_methods in final_list:
                for item in one_type_methods:
                    if len(one_type_methods[1:]) !=0:

                        if item in type_list:
                            print(
                                '<li><a href="/">' + '&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 &nbsp;&nbsp; {0} : Nums {1}&nbsp;&nbsp; &#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 '.format(
                                    one_type_methods[0], len(one_type_methods[1:])) + '</a></li> <br>')
                        else:
                            print(item)
        except Exception as e:
            raise e


    def bold_text_method(self,old_string):
        # func URLFilters<        (filters ...*regexp.Regexp) CollectorOption
        # --->
        # func <strong>URLFilters</strong>              (filters ...*regexp.Regexp) CollectorOption
        pattern = re.compile('\)(.*?)\(', re.S)
        items = re.findall(pattern, old_string)
        new_string = old_string.replace(items[0], "<strong>{0}</strong>".format(items[0]))

        return new_string

    @staticmethod
    def readDatafile(filename):
        line_list = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip("\n")
                line_list.append(line)
        return line_list


    def get_corre_item_method(self,string_item,type_list):

        corre_type_list = []
        for type_item in type_list:
            if type_item in string_item:
                corre_type_list.append(type_item)
        if corre_type_list == []:
            ret_corre_item = ""
        else:
            ret_corre_item =  str(corre_type_list)[1:-1]
        ret  =  string_item + " &nbsp;&nbsp;   &#129320; |  &#10145 &nbsp;&nbsp; " + ret_corre_item
        return ret

    def get_corre_item_func(self,string_item,type_list):

        corre_type_list = []
        for type_item in type_list:
            if type_item in string_item:
                corre_type_list.append(type_item)
        if corre_type_list == []:
            ret_corre_item = ""
        else:
            ret_corre_item =  "<strong>" +str(corre_type_list)[1:-1] +"</strong>"
        ret  =  string_item + " &nbsp;&nbsp;   &#129320; |  &#10145 &nbsp;&nbsp; " + ret_corre_item
        return ret


    def bold_text_indepent(self,old_string):
        # func URLFilters<        (filters ...*regexp.Regexp) CollectorOption
        # --->
        # func <strong>URLFilters</strong>              (filters ...*regexp.Regexp) CollectorOption
        pattern = re.compile('func (.*?)\(',re.S)
        items = re.findall(pattern,old_string)
        new_string = old_string.replace(items[0],'<strong>{0}</strong>'.format(items[0]))

        return new_string


    def bold_text_type_str(self,string_item):
        method_str_pattern = re.compile("\(.*?\)",re.S)
        items = re.findall(method_str_pattern,string_item)[0]

        if " " in items:
            method_str = items.split(" ")[1].split(")")[0]
        else:
            method_str = items.replace("(","")
            method_str = method_str.replace(")","")
        return method_str

    def method_dt_standby(self):

        method_ret_list = []
        type_ret_list = []
        for item in method_list:
            ret = self.get_corre_item_method(item, type_list)
            method_ret_list.append('<li><a href="/">' + self.bold_text_method(ret) + "</a></li> <br>")
            type_pattern = re.compile("\(.*?\)",re.S)
            one_type = re.findall(type_pattern,'<li><a href="/">' + self.bold_text_method(ret) + "</a></li> <br>")[0]
            type_ret_list.append(one_type)

        return method_ret_list


if __name__ =="__main__":
    url = "https://pkg.go.dev/github.com/fsouza/go-dockerclient"
    src_file = "trans_file"
    if os.path.exists(src_file):
        os.remove(src_file)
    output_text(src_file,url)
    independent_func_list = []
    type_list = []
    method_list = []
    datafile = src_file

    abc = Output_Golang_FITM()
    abc.exec()


