

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
    if "github.com" in url :

        element = etree.HTML(resp.text)

        xpath1 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/a/text()')
        xpath2 = element.xpath('/html/body/main/article/div/div/div[2]/div/div/section[2]/ul/li/ul/li/a/text()')
        for item in xpath1:
            ret_list.append(item)
        for item in xpath2:
            ret_list.append(item)

        for item in ret_list:
            print(item)
            writeinto_txtfile(trans_filename, item)
    else:
        element = etree.HTML(resp.text)

        xpath1 = element.xpath('/html/body/main/article/div/div/div[1]/div[2]/div/section[2]/ul/li/a/text()')
        xpath2 = element.xpath('/html/body/main/article/div/div/div[1]/div[2]/div/section[2]/ul/li/ul/li/a/text()')
        for item in xpath1:
            ret_list.append(item)
        for item in xpath2:
            ret_list.append(item)

        for item in ret_list:
            print(item)
            writeinto_txtfile(trans_filename, item)

















class Output_Golang_FITM():


    def exec(self):
        writeinto_txtfile(htmlfile,header)
        self.dt_standby(datafile)
        self.output_method()
        self.output_indepent_func() # ok
        self.output_IT() # ok

        writeinto_txtfile(htmlfile,footer)
        if os.path.exists(src_file):
            os.remove(src_file)




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
        func_title  = '<li><a href="/">' + '&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;  &nbsp;&nbsp;func:'+str(len(independent_func_list))+'&nbsp;&nbsp; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; ' + '</a></li> <br>'
        writeinto_txtfile(htmlfile,func_title)

        for item in independent_func_list:
            ret = self.get_corre_item_func(item, type_list)
            writeinto_txtfile(htmlfile,'<li><a href="/">&nbsp;&nbsp;' + self.bold_text_indepent(ret) + "&nbsp;&nbsp;</a></li> <br>")

            writeinto_txtfile(htmlfile,"\n")

    def output_IT(self):
        type_title = '<li><a href="/">' +'&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145;&nbsp;&nbsp;  type nums:'+str(len(type_list))+'&nbsp;&nbsp;&#10145;&#10145;&#10145; &#10145;&#10145;&#10145; &#10145;&#10145;&#10145; '+ '</a></li> <br>'
        writeinto_txtfile(htmlfile,type_title)
        for item in type_list:
            writeinto_txtfile(htmlfile,'<li><a href="/">' + item  + "</a></li> <br>")

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
                            writeinto_txtfile(htmlfile,
                                '<li><a href="/">' + '&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 &nbsp;&nbsp; {0} : Nums {1}&nbsp;&nbsp; &#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145&#10145 '.format(
                                    one_type_methods[0], len(one_type_methods[1:])) + '</a></li> <br>')
                        else:
                            writeinto_txtfile(htmlfile,item)
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

def get_htmlfile(url_info):
    #  https://pkg.go.dev/crypto@go1.20
    # https://pkg.go.dev/github.com/gin-gonic/gin
    url_list = url_info.split("/")
    if "github.com" in url_info:
        ret_str = url_list[url_list.index("github.com" )+1]
    else:
        ret_str = url_list[url_list.index("pkg.go.dev" )+1]

    return ret_str




#





if __name__ =="__main__":
    pkg_hp_html = "pkg_go_hp"
    url = "https://pkg.go.dev/github.com/gin-gonic/gin"
    src_file = "trans_file"
    htmlfile = get_htmlfile(url) + ".html"
    htmlfilename = get_htmlfile(url)
    header = ' <html> \n     \n  <meta charset="utf-8">     \n  <meta http-equiv="X-UA-Compatible" content="IE=edge">     \n  <meta name="viewport" content="width=device-width, initial-scale=1.0">     \n  <meta name="Description" content="Package resty provides Simple HTTP and REST client library for Go."> \n  <meta class="js-gtmID" data-gtmid="GTM-W8MVQXG"> ' + \
             '    \n  <link href="../dytree/static/pkg_go.css" rel="stylesheet">   \n <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://svgsilh.com/svg/33581.svg"> ' + \
             '   </head>\n <body>\n <div>      \n   <div>        \n         <section class="Documentation-index">                   \n      <h3 id="pkg-index" class="Documentation-indexHeader"> <a href="#pkg-index"></a></h3>' + \
             '         \n<div>                    \n           <br> \n                    <br> ' + \
             '   \n                     <a class="previous"  style="text-align: left;" href="/{0}.html">&nbsp&nbspBack</a>'.format(pkg_hp_html) + \
             '    \n                   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '     \n                 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '      \n               &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '       \n             &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '        \n           &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + \
             '        \n         <a class="next"   style="text-align: right;" href="/{1}">{0}</a></div><br>'.format(htmlfilename,htmlfile) + \
             '\n <br>  \n                   <ul class="Documentation-indexList"> '
    footer = "</ul> \n                     </section> \n         </div> \n </div> \n </body> \n    </html>"

    output_text(src_file,url)
    independent_func_list = []
    type_list = []
    method_list = []
    datafile = src_file

    abc = Output_Golang_FITM()
    abc.exec()




