from LinkedList import *

acl = ["seq 10 permit ip 172.255.136.0 0.0.0.255 any",
       "seq 12 permit ip 192.168.147.128 0.0.0.127 any",
       "seq 20 permit tcp 188.42.192.0 0.0.0.255 188.42.192.0 0.0.0.255",
       "seq 30 permit icmp any any count",
       "seq 40 hard-drop ip any any count"]

rule_list = SLinkedList()
rule_list.headvalue = Node(acl[0])
for rule in acl[1:]:
    rule_list.insert_end(rule, rule_list)

