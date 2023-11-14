from LinkedList import *
import re

class ACL:
    def __init__(self, acl_list):
        self.acl_list = acl_list

    def initialize(self):
        rule_list = SLinkedList()
        rule_list.headvalue = Node(self.acl_list[0])
        for rule in self.acl_list[1:]:
            rule_list.insert_end(rule, rule_list)
        return rule_list

    def print_acl(self):
        rule_list = self.initialize()
        rule_list.printlist()

class ParseRules:

    def __init__(self, rule):
        self.rule = rule