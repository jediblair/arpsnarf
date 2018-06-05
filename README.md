# arpsnarf
poll routers via snmp for their arp tables and deposit into mysql

You can use this with a list of routers in a text file for eg:

routers.txt
```
192.168.1.1
192.168.2.2
```

```
cat routers.txt | xargs -n1 ./arpsnarf.py -H
```
This is very much just a rough cut v1 for now
