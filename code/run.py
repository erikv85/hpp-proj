#!/usr/bin/env python

import os
import sys

# Argument handling:
def_file = 0;
def_threads = 1;
if len(sys.argv)==1:
  i = def_file
  j = def_threads
else: # expecting two args
  i = sys.argv[1]
  j = sys.argv[2]

# Program and dirs:
program = "decrypt"
files_dir = "../encrypted_files/"
#res_dir = "../decrypted_files/"
res_dir = " "
run_dir = "./"

# Input and output to program:
files = ("abcdefgh.txt", "image1.jpg", "image2.jpg", "image3.jpg")
dec_files = ["dec_"+f for f in files]

# Compile and run:
os.system("make")

run = run_dir+program+" "+files_dir+files[i]
run = run+" "+res_dir+dec_files[i]+" "+str(j)
os.system(run)

