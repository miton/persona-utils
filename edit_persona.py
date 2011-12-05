#!/usr/bin/env python
from __future__ import division
import sys

per_record_size = 52
per_record_have_offset = 0x00
per_record_id_offset = 0x02
per_record_level_offset = 0x04
per_record_exp_offset = 0x08
per_record_ability_offset = 0x0C
per_record_stats_offset = 0x1C

per_95_exp = 0x0015A593

per_comp_offset = 0x26c4

checksum_offset = 0x8D51

change = 0

def edit_stat(persona_id, slot, new_stat):
  global change
  record = per_comp_offset + per_record_size * (persona_id - 1)

  change += new_stat - buf[record + per_record_stats_offset + slot]
  buf[record + per_record_stats_offset + slot] = new_stat

def max_stats(persona_id):
  global change
  record = per_comp_offset + per_record_size * (persona_id - 1)

  for i in range(5):
    edit_stat(persona_id, i, 99)
  change += 95 - buf[record + per_record_level_offset]
  buf[record + per_record_level_offset] = 95
  change += ((per_95_exp & 0xFF0000) >> 16) - buf[record + per_record_exp_offset + 2]
  change += ((per_95_exp & 0x00FF00) >>  8) - buf[record + per_record_exp_offset + 1] 
  change += ((per_95_exp & 0x0000FF) >>  0) - buf[record + per_record_exp_offset + 0]
  buf[record + per_record_exp_offset + 2] = (per_95_exp & 0xFF0000) >> 16
  buf[record + per_record_exp_offset + 1] = (per_95_exp & 0x00FF00) >>  8
  buf[record + per_record_exp_offset + 0] = (per_95_exp & 0x0000FF) >>  0
  
def edit_skill(persona_id, slot, skill_num):
  global change
  record = per_comp_offset + per_record_size * (persona_id - 1)
  change += skill_num % 256 - buf[record + per_record_ability_offset + slot*2]
  change += skill_num // 256 - buf[record + per_record_ability_offset + slot*2 + 1]
  buf[record + per_record_ability_offset + slot*2] = skill_num % 256
  buf[record + per_record_ability_offset + slot*2 + 1] = skill_num // 256

def save():
  if 1:#change < 0:
    print "oh shit, change is negative and i don't know if python does negative mod right so hope", buf[checksum_offset], change, change % 256, buf[checksum_offset] + change, (buf[checksum_offset] + change) % 256

  buf[checksum_offset] = (buf[checksum_offset] + change) % 256

  f.seek(0)
  f.write(''.join(map(chr,buf)))
  f.close()
  
f = open(sys.argv[1], 'r+b')
buf = map(ord, f.read())
#abilities = False
abilities = True
ffff="""
for i in range(170): #range(per_num):
  #set before to off
  record = per_comp_offset + per_record_size * i
  change += 0 - buf[record + per_record_have_offset]
  #change += 0 - buf[record + per_record_level_offset]
  buf[record + per_record_have_offset] = 0
  #buf[record + per_record_level_offset] = 0
"""
"""
for i in range(min(170 - per_num - 1 ,99)):
  record = per_comp_offset + per_record_size * (per_num + i)
  change += 0x01 - buf[record + per_record_have_offset]
  buf[record + per_record_have_offset] = 1
  change += (i+1) - buf[record + per_record_level_offset]
  buf[record + per_record_level_offset] = i+1
  change += (per_num + i+1) - buf[record + per_record_id_offset]
  buf[record + per_record_id_offset] = per_num + i+1

  if abilities:
    for j in range(8):
      change += skill_num % 256 - buf[record + per_record_ability_offset + j*2]
      change += skill_num // 256 - buf[record + per_record_ability_offset + j*2 + 1]
      buf[record + per_record_ability_offset + j*2] = skill_num % 256
      buf[record + per_record_ability_offset + j*2 + 1] = skill_num // 256
      skill_num += 1
"""
#edit growths
"""

for i in range(170):
  record = per_comp_offset + per_record_size * (per_num + i)
  for j in range(8):
    if buf[record + per_record_ability_offset + j*2 + 1] == 0x2 and (buf[record + per_record_ability_offset + j*2] == 0x2A or buf[record + per_record_ability_offset + j*2] == 0x29):
      skill_num = 0x22B
      change += skill_num % 256 - buf[record + per_record_ability_offset + j*2]
      change += skill_num // 256 - buf[record + per_record_ability_offset + j*2 + 1]
      buf[record + per_record_ability_offset + j*2] = skill_num % 256
      buf[record + per_record_ability_offset + j*2 + 1] = skill_num // 256
"""
sldfj="""
for i in range(per_num+99,170):
  #set after to off
  record = per_comp_offset + per_record_size * i
  change += 0 - buf[record + per_record_have_offset]
  change += 0 - buf[record + per_record_level_offset]
  buf[record + per_record_have_offset] = 0
  buf[record + per_record_level_offset] = 0
"""
"""
if 1:#change < 0:
  print "oh shit, change is negative and i don't know if python does negative mod right so hope", buf[checksum_offset], change, change % 256, buf[checksum_offset] + change, (buf[checksum_offset] + change) % 256

buf[checksum_offset] = (buf[checksum_offset] + change) % 256

f.seek(0)
f.write(''.join(map(chr,buf)))
f.close()
"""

"""
edit_skill(99+37, 3, 66*8+6)
edit_skill(99+37, 4, 59*8+7)
edit_skill(99+37, 5, 24*8+4)
edit_skill(99+37, 6, 25*8+4)
edit_skill(99+37, 7, 71*8+2)
edit_skill(99+10, 7, 74*8+6)
edit_skill(99+10, 5, 74*8+0)
edit_skill(26, 0, 74*8+6)
edit_skill(56, 7, 74*8+6)
edit_skill(99+2, 6, 74*8+6)
edit_skill(99+2, 3, 74*8+1)
edit_skill(25, 2, 74*8+6)
edit_skill(99+20, 0, 73*8+5)
edit_skill(99+20, 1, 73*8+6)
edit_skill(99+20, 2, 73*8+7)
edit_skill(99+20, 3, 27*8+1)
edit_skill(99+20, 4, 27*8+3)
edit_skill(99+20, 5, 26*8+7)
edit_skill(99+20, 6, 0)
edit_skill(99+20, 7, 0)
edit_skill(99+28, 1, 25*8+7)
edit_skill(99+28, 3, 26*8+1)
edit_skill(99+28, 5, 26*8+3)
edit_skill(99+28, 6, 9*8+1)
"""

