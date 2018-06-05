#!/usr/bin/python
from snimpy.manager import Manager as M
from snimpy.manager import load

from time import gmtime, strftime
from datetime import date, datetime, timedelta
import sys,argparse
import mysql.connector
import binascii

global mysqlerror
mysqlerror = 0



load("IF-MIB")
load("IP-MIB")


def insertRow(routerip,portindex,alias,description,arpip,arpmac):
        curTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        try:
                print(routerip,portindex,alias,description,arpip,arpmac)
                data_mac = (routerip,portindex,alias,description,arpip,arpmac)
                cursor = cnx.cursor()
                cursor.execute(add_mac, data_mac)
                mac_no = cursor.lastrowid
                cnx.commit()
                cursor.close()
        except mysql.connector.Error as err:
                mysqlerror = mysqlerror + 1
                print("Something went wrong: {}".format(err))
        finally:
                return


def main(argv):

        parser = argparse.ArgumentParser(description='Insert ARPs into a database')
        parser.add_argument('-H', action="store", dest="hostname")
        parser.add_argument('-c', action="store", dest="comstring")
        results = parser.parse_args(argv)
        m = M(host=results.hostname, community="public", version=2)

        macs = m.ipNetToMediaPhysAddress
        ifdescr = m.ifDescr
        ifalias = m.ifAlias

        global add_mac
        add_mac = ("INSERT INTO arplist"
                "(routerip, portindex, alias, description, arpip, arpmac)"
                " VALUES (%s, %s, %s, %s, %s, %s)")
        global cnx
        cnx = mysql.connector.connect(user='arpuser', password='arppass',
                host='mysql01.example.net', database='arpentries')


        for (index,value) in macs:
                try:

                        macentry = m.ipNetToMediaPhysAddress[index,value]
                        asciimac = binascii.hexlify(macentry)
                        insertRow(results.hostname, int(index), str(ifalias[index]), str(ifdescr[index]), str(value), asciimac)

                except Exception:
                        print "uh oh something went wrong"

        cnx.close()

if __name__ == "__main__":
   main(sys.argv[1:])
