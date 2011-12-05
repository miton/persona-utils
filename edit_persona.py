#!/usr/bin/env python
from __future__ import division
import sys

from persona import persona_by_id, persona_by_name
from skill import ability_ids

per_record_size = 52
per_record_have_offset = 0x00
per_record_id_offset = 0x02
per_record_level_offset = 0x04
per_record_exp_offset = 0x08
per_record_ability_offset = 0x0C
per_record_stats_offset = 0x1C

per_95_exp = 0x0015A593 #actually does not seem that all persona use the same curve

per_comp_offset = 0x26c4
per_inv_offset  = 0x2418

checksum_offset = 0x8D51

change = 0

def comp_to_inv(persona_id, inv_slot):
  global change
  inv_record = per_inv_offset + per_record_size * inv_slot
  comp_record = per_comp_offset + per_record_size * (persona_id - 1)
  for i in range(per_record_size):
    change += buf[comp_record + i] - buf[inv_record + i]
    buf[inv_record + i] = buf[comp_record + i]

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

def edit_skills(persona_name, skills):
  global change

  per_id = persona_by_name[persona_name].id
  for i,v in enumerate(skills):
    edit_skill(per_id, i, ability_ids[v])

def save():
  buf[checksum_offset] = (buf[checksum_offset] + change) % 256

  f.seek(0)
  f.write(''.join(map(chr,buf)))
  f.close()
  
f = open(sys.argv[1], 'r+b')
buf = map(ord, f.read())

