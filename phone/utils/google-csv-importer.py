#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
import subprocess
import uuid

with open(sys.argv[1]) as csvfile:
    print("opening: " + sys.argv[1])
    reader = csv.DictReader(csvfile, delimiter=',')   

    contact_list = {}    
        
    
    for row in reader:
        new = []
        
        if row["Middle Name"] != "":    
            new.append(row["First Name"] +" "+ row["Middle Name"])
        else:
             new.append(row["First Name"])
        new.append(row["Last Name"])
        new.append(row["Organization Name"])
        new.append(row["Phone 1 - Value"])
        
        if row["Photo"] != "":
            photo_name = uuid.uuid4().hex.upper()[0:8]
     
            subprocess.run(["rm","images/*"])
            
            subprocess.run(["bash", "-c" , "curl " + row["Photo"] + " > images/" + photo_name + ".jpg " ])
            
            subprocess.run(["convert", "images/" + photo_name + ".jpg", "-resize", "128", "images/" + photo_name + ".ppm"])
            
            subprocess.run(["ptp16", "images/" + photo_name + ".ppm", "images/" + photo_name + ".p16"])
            
            subprocess.run(["rm", "images/" + photo_name + ".ppm"])
            subprocess.run(["rm", "images/" + photo_name + ".jpg"])
            
            new.append("appdata/phone/images/" + photo_name + ".p16")
        else:
            new.append("appdata/phone/empty.p16")
        

        contact_list[(row["First Name"] +" "+ row["Middle Name"]) +" "+ row["Last Name"]] = new

    cn = 0
    for r in contact_list:
      print("valid_" + str(cn) + "=1")
      print("name_" + str(cn) + "=" +contact_list.get(r)[0])
      print("surname_" + str(cn) + "=" + contact_list.get(r)[1])
      print("company_" + str(cn) + "=" + contact_list.get(r)[2])
      print("phone_" + str(cn) + "_0=" + contact_list.get(r)[3])
      print("note_" + str(cn) + "=")
      print("pic_" + str(cn) + "=" + contact_list.get(r)[4])
      
      cn += 1
