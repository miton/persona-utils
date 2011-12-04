arcana_ranks = {
  'Hierophant': 6, 'Devil': 16, 'Justice': 9, 'Sun': 20, 'Moon': 19, 'Lovers': 7, 'Strength': 12, 'Hanged Man': 13, 'Hermit': 10, 'Fool': 1, 'Star': 18, 'Magician': 2, 'Judgment': 21, 'Aeon': 22, 'Fortune': 11, 'Death': 14, 'Priestess': 3, 'Tower': 17, 'Emperor': 5, 'Chariot': 8, 'Temperance': 15, 'Empress': 4
}

fusion2_arcana = {
  'Hierophant' : {'Fool': 'Hermit', 'Hierophant': 'Hierophant', 'Emperor': 'Chariot', 'Fortune': 'Emperor', 'Chariot': 'Justice', 'Justice': 'Chariot', 'Sun': 'Temperance', 'Star': 'Priestess', 'Priestess': 'Chariot', 'Moon': 'Temperance', 'Empress': 'Priestess', 'Lovers': 'Magician', 'Death': 'Empress', 'Strength': 'Priestess', 'Temperance': 'Strength', 'Tower': 'Temperance', 'Magician': 'Hermit', 'Judgment': 'Lovers', 'Hanged Man': 'Lovers', 'Hermit': 'Chariot'},
  'Devil' : {'Fool': 'Hermit', 'Lovers': 'Strength', 'Fortune': 'Moon', 'Devil': 'Devil', 'Aeon': 'Lovers', 'Empress': 'Lovers', 'Chariot': 'Hanged Man', 'Strength': 'Fortune', 'Temperance': 'Death', 'Magician': 'Temperance', 'Hanged Man': 'Moon', 'Hermit': 'Death'},
  'Justice' : {'Fool': 'Lovers', 'Hierophant': 'Chariot', 'Emperor': 'Devil', 'Fortune': 'Chariot', 'Chariot': 'Magician', 'Justice': 'Justice', 'Sun': 'Emperor', 'Star': 'Emperor', 'Priestess': 'Lovers', 'Empress': 'Emperor', 'Lovers': 'Chariot', 'Death': 'Moon', 'Strength': 'Temperance', 'Temperance': 'Moon', 'Tower': 'Star', 'Magician': 'Hierophant', 'Judgment': 'Aeon', 'Hanged Man': 'Priestess', 'Hermit': 'Priestess'},
  'Sun' : {'Fool': 'Empress', 'Hierophant': 'Temperance', 'Emperor': 'Empress', 'Fortune': 'Temperance', 'Star': 'Justice', 'Justice': 'Emperor', 'Sun': 'Sun', 'Priestess': 'Star', 'Moon': 'Temperance', 'Empress': 'Lovers', 'Lovers': 'Hierophant', 'Strength': 'Priestess', 'Temperance': 'Star', 'Magician': 'Lovers', 'Judgment': 'Star', 'Aeon': 'Empress'},
  'Moon' : {'Fool': 'Fortune', 'Hierophant': 'Temperance', 'Lovers': 'Empress', 'Fortune': 'Chariot', 'Star': 'Death', 'Death': 'Star', 'Sun': 'Temperance', 'Priestess': 'Star', 'Moon': 'Moon', 'Empress': 'Lovers', 'Chariot': 'Fortune', 'Strength': 'Hanged Man', 'Temperance': 'Empress', 'Tower': 'Fortune', 'Magician': 'Priestess', 'Hanged Man': 'Empress', 'Hermit': 'Magician'},
  'Lovers' : {'Fool': 'Priestess', 'Hierophant': 'Magician', 'Emperor': 'Chariot', 'Fortune': 'Magician', 'Devil': 'Strength', 'Chariot': 'Emperor', 'Justice': 'Chariot', 'Sun': 'Hierophant', 'Star': 'Hierophant', 'Priestess': 'Magician', 'Moon': 'Empress', 'Empress': 'Fortune', 'Lovers': 'Lovers', 'Death': 'Devil', 'Aeon': 'Hanged Man', 'Strength': 'Hierophant', 'Temperance': 'Priestess', 'Tower': 'Star', 'Magician': 'Emperor', 'Hanged Man': 'Hermit', 'Hermit': 'Justice'},
  'Strength' : {'Fool': 'Hanged Man', 'Hierophant': 'Priestess', 'Lovers': 'Hierophant', 'Temperance': 'Moon', 'Devil': 'Fortune', 'Justice': 'Temperance', 'Sun': 'Priestess', 'Priestess': 'Hermit', 'Moon': 'Hanged Man', 'Empress': 'Chariot', 'Chariot': 'Justice', 'Death': 'Hanged Man', 'Strength': 'Strength', 'Star': 'Priestess', 'Tower': 'Devil', 'Emperor': 'Hanged Man', 'Judgment': 'Hanged Man', 'Hanged Man': 'Hermit', 'Hermit': 'Fortune'},
  'Hanged Man' : {'Fool': 'Magician', 'Hierophant': 'Lovers', 'Emperor': 'Hermit', 'Fortune': 'Strength', 'Devil': 'Moon', 'Chariot': 'Fortune', 'Justice': 'Priestess', 'Star': 'Strength', 'Priestess': 'Strength', 'Moon': 'Empress', 'Empress': 'Chariot', 'Lovers': 'Hermit', 'Death': 'Devil', 'Aeon': 'Temperance', 'Strength': 'Hermit', 'Temperance': 'Hierophant', 'Tower': 'Death', 'Magician': 'Devil', 'Hanged Man': 'Hanged Man', 'Hermit': 'Fortune'},
  'Hermit' : {'Fool': 'Priestess', 'Hierophant': 'Chariot', 'Emperor': 'Strength', 'Fortune': 'Emperor', 'Devil': 'Death', 'Chariot': 'Temperance', 'Justice': 'Priestess', 'Star': 'Chariot', 'Priestess': 'Strength', 'Moon': 'Magician', 'Empress': 'Lovers', 'Lovers': 'Justice', 'Aeon': 'Star', 'Strength': 'Fortune', 'Temperance': 'Hanged Man', 'Magician': 'Chariot', 'Hanged Man': 'Fortune', 'Hermit': 'Hermit'},
  'Fool' : {'Hierophant': 'Hermit', 'Devil': 'Hermit', 'Justice': 'Lovers', 'Sun': 'Empress', 'Moon': 'Fortune', 'Lovers': 'Priestess', 'Strength': 'Hanged Man', 'Hanged Man': 'Magician', 'Hermit': 'Priestess', 'Fool': 'Fool', 'Star': 'Aeon', 'Magician': 'Hierophant', 'Judgment': 'Star', 'Aeon': 'Death', 'Fortune': 'Justice', 'Death': 'Strength', 'Priestess': 'Justice', 'Tower': 'Moon', 'Emperor': 'Chariot', 'Chariot': 'Emperor', 'Temperance': 'Hierophant', 'Empress': 'Fortune'},
  'Star' : {'Fool': 'Aeon', 'Hierophant': 'Priestess', 'Emperor': 'Justice', 'Fortune': 'Moon', 'Star': 'Star', 'Justice': 'Emperor', 'Sun': 'Justice', 'Priestess': 'Justice', 'Moon': 'Death', 'Empress': 'Temperance', 'Lovers': 'Hierophant', 'Aeon': 'Devil', 'Strength': 'Priestess', 'Temperance': 'Moon', 'Magician': 'Empress', 'Judgment': 'Temperance', 'Hanged Man': 'Strength', 'Hermit': 'Chariot'},
  'Magician' : {'Fool': 'Hierophant', 'Hierophant': 'Hermit', 'Emperor': 'Temperance', 'Fortune': 'Emperor', 'Devil': 'Temperance', 'Chariot': 'Devil', 'Justice': 'Hierophant', 'Sun': 'Lovers', 'Star': 'Empress', 'Priestess': 'Lovers', 'Moon': 'Priestess', 'Empress': 'Hanged Man', 'Lovers': 'Emperor', 'Temperance': 'Death', 'Tower': 'Empress', 'Magician': 'Magician', 'Hanged Man': 'Devil', 'Hermit': 'Chariot'},
  'Judgment' : {'Fool': 'Star', 'Hierophant': 'Lovers', 'Strength': 'Hanged Man', 'Temperance': 'Moon', 'Justice': 'Aeon', 'Sun': 'Star', 'Priestess': 'Empress', 'Star': 'Temperance', 'Tower': 'Aeon', 'Emperor': 'Hierophant', 'Judgment': 'Judgment', 'Aeon': 'Star'},
  'Aeon' : {'Fool': 'Death', 'Lovers': 'Hanged Man', 'Fortune': 'Devil', 'Star': 'Devil', 'Devil': 'Lovers', 'Sun': 'Empress', 'Priestess': 'Empress', 'Aeon': 'Aeon', 'Empress': 'Moon', 'Chariot': 'Death', 'Temperance': 'Star', 'Tower': 'Moon', 'Judgment': 'Star', 'Hanged Man': 'Temperance', 'Hermit': 'Star'},
  'Fortune' : {'Fool': 'Justice', 'Hierophant': 'Emperor', 'Lovers': 'Magician', 'Fortune': 'Fortune', 'Devil': 'Moon', 'Star': 'Moon', 'Justice': 'Chariot', 'Sun': 'Temperance', 'Priestess': 'Magician', 'Moon': 'Chariot', 'Empress': 'Strength', 'Chariot': 'Strength', 'Aeon': 'Devil', 'Temperance': 'Lovers', 'Tower': 'Moon', 'Magician': 'Emperor', 'Hanged Man': 'Strength', 'Hermit': 'Emperor'},
  'Death' : {'Fool': 'Strength', 'Hierophant': 'Empress', 'Lovers': 'Devil', 'Justice': 'Moon', 'Priestess': 'Emperor', 'Moon': 'Star', 'Empress': 'Devil', 'Strength': 'Hanged Man', 'Death': 'Death', 'Emperor': 'Moon', 'Hanged Man': 'Devil'},
  'Priestess' : {'Fool': 'Justice', 'Hierophant': 'Chariot', 'Emperor': 'Justice', 'Fortune': 'Magician', 'Chariot': 'Magician', 'Justice': 'Lovers', 'Sun': 'Star', 'Star': 'Justice', 'Priestess': 'Priestess', 'Moon': 'Star', 'Empress': 'Lovers', 'Lovers': 'Magician', 'Death': 'Emperor', 'Aeon': 'Empress', 'Strength': 'Hermit', 'Temperance': 'Empress', 'Magician': 'Lovers', 'Judgment': 'Empress', 'Hanged Man': 'Strength', 'Hermit': 'Strength'},
  'Tower' : {'Fool': 'Moon', 'Hierophant': 'Temperance', 'Lovers': 'Star', 'Fortune': 'Moon', 'Justice': 'Star', 'Moon': 'Fortune', 'Empress': 'Chariot', 'Chariot': 'Moon', 'Aeon': 'Moon', 'Strength': 'Devil', 'Temperance': 'Devil', 'Tower': 'Tower', 'Magician': 'Empress', 'Judgment': 'Aeon', 'Hanged Man': 'Death'},
  'Emperor' : {'Fool': 'Chariot', 'Hierophant': 'Chariot', 'Emperor': 'Emperor', 'Temperance': 'Hanged Man', 'Chariot': 'Hermit', 'Justice': 'Devil', 'Sun': 'Empress', 'Priestess': 'Justice', 'Empress': 'Lovers', 'Lovers': 'Chariot', 'Death': 'Moon', 'Strength': 'Hanged Man', 'Star': 'Justice', 'Magician': 'Temperance', 'Judgment': 'Hierophant', 'Hanged Man': 'Hermit', 'Hermit': 'Strength'},
  'Chariot' : {'Fool': 'Emperor', 'Hierophant': 'Justice', 'Emperor': 'Hermit', 'Fortune': 'Strength', 'Devil': 'Hanged Man', 'Chariot': 'Chariot', 'Justice': 'Magician', 'Priestess': 'Magician', 'Moon': 'Fortune', 'Empress': 'Devil', 'Lovers': 'Emperor', 'Aeon': 'Death', 'Strength': 'Justice', 'Temperance': 'Death', 'Tower': 'Moon', 'Magician': 'Devil', 'Hanged Man': 'Fortune', 'Hermit': 'Temperance'},
  'Temperance' : {'Fool': 'Hierophant', 'Hierophant': 'Strength', 'Emperor': 'Hanged Man', 'Fortune': 'Lovers', 'Devil': 'Death', 'Chariot': 'Death', 'Justice': 'Moon', 'Sun': 'Star', 'Star': 'Moon', 'Priestess': 'Empress', 'Moon': 'Empress', 'Empress': 'Lovers', 'Lovers': 'Priestess', 'Aeon': 'Star', 'Strength': 'Moon', 'Temperance': 'Temperance', 'Tower': 'Devil', 'Magician': 'Death', 'Judgment': 'Moon', 'Hanged Man': 'Hierophant', 'Hermit': 'Hanged Man'},
  'Empress' : {'Fool': 'Fortune', 'Hierophant': 'Priestess', 'Emperor': 'Lovers', 'Fortune': 'Strength', 'Devil': 'Lovers', 'Chariot': 'Devil', 'Justice': 'Emperor', 'Sun': 'Lovers', 'Star': 'Temperance', 'Priestess': 'Lovers', 'Moon': 'Lovers', 'Empress': 'Empress', 'Lovers': 'Fortune', 'Death': 'Devil', 'Aeon': 'Moon', 'Strength': 'Chariot', 'Temperance': 'Lovers', 'Tower': 'Chariot', 'Magician': 'Hanged Man', 'Hanged Man': 'Chariot', 'Hermit': 'Lovers'},
}

fusion3_arcana = {
  'Hierophant' : {'Hierophant': 'Hierophant', 'Lovers': 'Temperance', 'Fortune': 'Emperor', 'Star': 'Priestess', 'Justice': 'Magician', 'Sun': 'Temperance', 'Moon': 'Temperance', 'Chariot': 'Sun', 'Death': 'Empress', 'Aeon': 'Tower', 'Strength': 'Emperor', 'Temperance': 'Strength', 'Tower': 'Temperance', 'Devil': 'Fool', 'Judgment': 'Lovers', 'Hanged Man': 'Fortune', 'Hermit': 'Chariot'},
  'Devil' : {'Devil': 'Devil', 'Star': 'Magician', 'Sun': 'Death', 'Moon': 'Judgment', 'Tower': 'Judgment', 'Judgment': 'Moon', 'Aeon': 'Lovers'},
  'Justice' : {'Death': 'Moon', 'Fortune': 'Chariot', 'Star': 'Emperor', 'Justice': 'Justice', 'Sun': 'Emperor', 'Moon': 'Tower', 'Strength': 'Temperance', 'Aeon': 'Judgment', 'Temperance': 'Moon', 'Tower': 'Sun', 'Devil': 'Tower', 'Judgment': 'Aeon', 'Hanged Man': 'Priestess', 'Hermit': 'Strength'},
  'Sun' : {'Sun': 'Sun', 'Judgment': 'Star', 'Aeon': 'Empress'},
  'Moon' : {'Sun': 'Temperance', 'Judgment': 'Priestess', 'Aeon': 'Judgment', 'Moon': 'Moon'},
  'Lovers' : {'Strength': 'Hierophant', 'Fortune': 'Fool', 'Chariot': 'Strength', 'Justice': 'Hanged Man', 'Sun': 'Hierophant', 'Star': 'Hierophant', 'Moon': 'Empress', 'Lovers': 'Lovers', 'Death': 'Devil', 'Aeon': 'Hanged Man', 'Temperance': 'Priestess', 'Tower': 'Star', 'Devil': 'Death', 'Judgment': 'Sun', 'Hanged Man': 'Hermit', 'Hermit': 'Hierophant'},
  'Strength' : {'Death': 'Hanged Man', 'Temperance': 'Moon', 'Sun': 'Priestess', 'Moon': 'Aeon', 'Devil': 'Empress', 'Aeon': 'Tower', 'Strength': 'Strength', 'Star': 'Priestess', 'Tower': 'Judgment', 'Judgment': 'Hanged Man', 'Hanged Man': 'Fortune', 'Hermit': 'Emperor'},
  'Hanged Man' : {'Devil': 'Death', 'Star': 'Strength', 'Sun': 'Judgment', 'Moon': 'Empress', 'Death': 'Devil', 'Aeon': 'Temperance', 'Temperance': 'Hierophant', 'Tower': 'Death', 'Judgment': 'Aeon', 'Hanged Man': 'Hanged Man'},
  'Hermit' : {'Death': 'Tower', 'Temperance': 'Hanged Man', 'Star': 'Chariot', 'Devil': 'Death', 'Sun': 'Star', 'Moon': 'Magician', 'Strength': 'Fortune', 'Aeon': 'Star', 'Fortune': 'Emperor', 'Tower': 'Death', 'Judgment': 'Tower', 'Hanged Man': 'Fortune', 'Hermit': 'Hermit'},
  'Fool' : {'Hierophant': 'Hermit', 'Devil': 'Justice', 'Justice': 'Chariot', 'Sun': 'Empress', 'Moon': 'Fortune', 'Lovers': 'Temperance', 'Strength': 'Hanged Man', 'Hanged Man': 'Magician', 'Hermit': 'Priestess', 'Fool': 'Fool', 'Star': 'Aeon', 'Magician': 'Emperor', 'Judgment': 'Star', 'Aeon': 'Death', 'Fortune': 'Justice', 'Death': 'Strength', 'Priestess': 'Magician', 'Tower': 'Moon', 'Emperor': 'Lovers', 'Chariot': 'Devil', 'Temperance': 'Hierophant', 'Empress': 'Fortune'},
  'Star' : {'Sun': 'Aeon', 'Judgment': 'Temperance', 'Star': 'Star', 'Aeon': 'Devil', 'Moon': 'Sun'},
  'Magician' : {'Hierophant': 'Hermit', 'Devil': 'Temperance', 'Lovers': 'Devil', 'Fortune': 'Emperor', 'Emperor': 'Lovers', 'Star': 'Empress', 'Justice': 'Fool', 'Sun': 'Lovers', 'Priestess': 'Devil', 'Moon': 'Fortune', 'Empress': 'Hanged Man', 'Chariot': 'Moon', 'Death': 'Tower', 'Aeon': 'Sun', 'Strength': 'Star', 'Temperance': 'Death', 'Tower': 'Empress', 'Magician': 'Magician', 'Judgment': 'Tower', 'Hanged Man': 'Devil', 'Hermit': 'Hanged Man'},
  'Judgment' : {'Judgment': 'Judgment', 'Aeon': 'Fool'},
  'Aeon' : {'Aeon': 'Aeon'},
  'Fortune' : {'Death': 'Judgment', 'Temperance': 'Lovers', 'Star': 'Moon', 'Devil': 'Hermit', 'Sun': 'Temperance', 'Moon': 'Chariot', 'Strength': 'Sun', 'Aeon': 'Devil', 'Fortune': 'Fortune', 'Tower': 'Aeon', 'Judgment': 'Star', 'Hanged Man': 'Strength'},
  'Death' : {'Death': 'Death', 'Star': 'Tower', 'Devil': 'Judgment', 'Sun': 'Moon', 'Moon': 'Star', 'Chariot': 'Judgment', 'Temperance': 'Tower', 'Tower': 'Sun', 'Judgment': 'Fool', 'Aeon': 'Sun'},
  'Priestess' : {'Hierophant': 'Chariot', 'Devil': 'Tower', 'Lovers': 'Hermit', 'Fortune': 'Magician', 'Star': 'Justice', 'Justice': 'Hierophant', 'Sun': 'Star', 'Priestess': 'Priestess', 'Moon': 'Star', 'Empress': 'Lovers', 'Chariot': 'Emperor', 'Death': 'Emperor', 'Aeon': 'Empress', 'Strength': 'Chariot', 'Temperance': 'Empress', 'Tower': 'Death', 'Emperor': 'Hierophant', 'Judgment': 'Justice', 'Hanged Man': 'Strength', 'Hermit': 'Fool'},
  'Tower' : {'Star': 'Judgment', 'Sun': 'Moon', 'Moon': 'Fortune', 'Tower': 'Tower', 'Judgment': 'Aeon', 'Aeon': 'Fool'},
  'Emperor' : {'Hierophant': 'Chariot', 'Devil': 'Tower', 'Lovers': 'Strength', 'Fortune': 'Sun', 'Star': 'Hermit', 'Justice': 'Chariot', 'Sun': 'Empress', 'Moon': 'Tower', 'Chariot': 'Justice', 'Death': 'Moon', 'Aeon': 'Sun', 'Strength': 'Hanged Man', 'Temperance': 'Hanged Man', 'Tower': 'Death', 'Emperor': 'Emperor', 'Judgment': 'Hierophant', 'Hanged Man': 'Temperance', 'Hermit': 'Lovers'},
  'Chariot' : {'Strength': 'Justice', 'Fortune': 'Hermit', 'Star': 'Sun', 'Justice': 'Magician', 'Sun': 'Justice', 'Moon': 'Fortune', 'Chariot': 'Chariot', 'Death': 'Fool', 'Aeon': 'Death', 'Temperance': 'Death', 'Tower': 'Moon', 'Devil': 'Star', 'Judgment': 'Tower', 'Hanged Man': 'Fortune', 'Hermit': 'Hanged Man'},
  'Temperance' : {'Devil': 'Moon', 'Star': 'Hermit', 'Sun': 'Judgment', 'Moon': 'Empress', 'Temperance': 'Temperance', 'Tower': 'Devil', 'Judgment': 'Justice', 'Aeon': 'Star'},
  'Empress' : {'Hierophant': 'Priestess', 'Devil': 'Magician', 'Lovers': 'Fortune', 'Fortune': 'Strength', 'Star': 'Temperance', 'Justice': 'Emperor', 'Sun': 'Lovers', 'Moon': 'Lovers', 'Empress': 'Empress', 'Chariot': 'Devil', 'Death': 'Devil', 'Aeon': 'Moon', 'Strength': 'Chariot', 'Temperance': 'Lovers', 'Tower': 'Chariot', 'Emperor': 'Fool', 'Judgment': 'Devil', 'Hanged Man': 'Chariot', 'Hermit': 'Lovers'},
}
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
    a, b, c = sorted([a,b,c], key=lambda i: i.level * 100 + arcana_order[i.arcana])
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
