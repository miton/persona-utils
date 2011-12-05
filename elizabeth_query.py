from persona import *
from fusion import *
from skill import *

#terribly inefficient but only needs to be run once so...
#actually this is not quite right because triangle fusion uses current levels(?) and it doesn't try special fusions either
#how did I end up with Orpheus Telos in the results though?
#guess is fusion2 missing the found check
#turned out to be fusion2 going negative i
for base, skill_type in [('Surt', 'fire'), ('Skadi', 'ice'), ('Odin', 'elec'), ('Norn', 'wind')]:
  possible = set([persona_by_name[base]])
  old_possible = possible.copy()

  done = False
  depth = 0

  while not done:
    possible = old_possible.copy()
    for persona_a in old_possible:
      for persona_b in personas:
        if persona_b == persona_a:
          continue
        result = fusion2(persona_a, persona_b)
        if result and can_inherit(result, skill_type):
          possible.add(result)

        for persona_c in personas:
          if persona_c == persona_a or persona_c == persona_b:
            continue
          result = fusion3(persona_b, persona_c, persona_a, this_order=True)
          if result and can_inherit(result, skill_type):
            possible.add(result)
          result = fusion3(persona_a, persona_c, persona_b, this_order=True)
          if result and can_inherit(result, skill_type):
            possible.add(result)

          result = fusion3(persona_a, persona_b, persona_c, this_order=True)
          if result and can_inherit(result, skill_type):
            possible.add(result)

    if len(possible.difference(old_possible)) == 0:
      done = True
    else:
      depth += 1
      old_possible = possible.copy()
    #add every special that has at least one compontent in possible, but I don't have the specials yet
    print skill_type, depth, len(possible), possible

          
        
