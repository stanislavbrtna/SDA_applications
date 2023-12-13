#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys

with open(sys.argv[1]) as csvfile:
    print("opening: " + sys.argv[1])
    reader = csv.DictReader(csvfile, delimiter=',')   

    contact_list = {}    
        
    
    for row in reader:
        new = []
        
        if row["Additional Name"] != "":    
            new.append(row["Given Name"] +" "+ row["Additional Name"])
        else:
             new.append(row["Given Name"])
        new.append(row["Family Name"])
        new.append(row["Organization 1 - Name"])
        new.append(row["Phone 1 - Value"])
        

        contact_list[(row["Given Name"] +" "+ row["Additional Name"]) +" "+ row["Family Name"]] = new

    cn = 0
    for r in contact_list:
      print("name_" + str(cn) + "=" +contact_list.get(r)[0])
      print("surname_" + str(cn) + "=" + contact_list.get(r)[1])
      print("company_" + str(cn) + "=" + contact_list.get(r)[2])
      print("phone_" + str(cn) + "_0=" + contact_list.get(r)[3])
      
      cn += 1
