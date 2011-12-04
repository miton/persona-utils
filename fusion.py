def fusion_2(a, b):
  result_level = 1 + floor((a.level + b.level) / 2.0)
  result_arcana = fusion2_arcana[a.arcana][b.arcana]
  
  arcana_list = persona_by_arcana[result_arcana]
  for i,persona in enumerate(arcana_list):
    if persona.base_level >= result_level and not persona.special:
      break

  if a.arcana == b.arcana:
    i -= 1
  if persona == a  or persona == b:
    i -= 1
  #can this go negative?
  return arcana_list[i]

def fusion_3(a, b, c, this_order = False):
  if not this_order:
    a, b, c = sorted([a,b,c], key=lambda i: i.level * 100 + arcana_order[i.arcana]))
  intermediate_arcana = fusion2_arcana[a.arcana][b.arcana]
  
  result_level = 5 + floor((a.level + b.level + c.level) / 3.0)
  result_arcana = fusion3_arcana[intermediate_arcana][c.arcana]

  arcana_list = persona_by_arcana[result_arcana]
  found = False
  for i,persona in enumerate(arcana_list):
    if persona.base_level >= result_level and not persona.special:
      found = True
      break

  if not found:
    return None
  return persona
