true = True
#blatantly taken from https://github.com/arantius/persona-3-fes-fusion-calculator/blob/master/data.js
personas_a = [
    {'name': 'Orpheus',         'level':  1, 'arcana': 'Fool', 'special': true},
    {'name': 'Slime',           'level': 12, 'arcana': 'Fool'},
    {'name': 'Legion',          'level': 22, 'arcana': 'Fool'},
    {'name': 'Black Frost',     'level': 34, 'arcana': 'Fool', 'special': true},
    {'name': 'Ose',             'level': 44, 'arcana': 'Fool'},
    {'name': 'Decarabia',       'level': 50, 'arcana': 'Fool'},
    {'name': 'Loki',            'level': 58, 'arcana': 'Fool'},
    {'name': 'Susano-o',        'level': 76, 'arcana': 'Fool', 'max': true, 'special': true},
    {'name': 'Orpheus Telos',   'level': 90, 'arcana': 'Fool', 'special': true},
    {'name': 'Nekomata',        'level':  5, 'arcana': 'Magician'},
    {'name': 'Jack Frost',      'level':  8, 'arcana': 'Magician'},
    {'name': 'Pyro Jack',       'level': 14, 'arcana': 'Magician'},
    {'name': 'Hua Po',          'level': 20, 'arcana': 'Magician', 'item': true},
    {'name': 'Sati',            'level': 28, 'arcana': 'Magician'},
    {'name': 'Orobas',          'level': 34, 'arcana': 'Magician'},
    {'name': 'Rangda',          'level': 40, 'arcana': 'Magician'},
    {'name': 'Surt',            'level': 52, 'arcana': 'Magician', 'max': true},
    {'name': 'Apsaras',         'level':  3, 'arcana': 'Priestess'},
    {'name': 'Unicorn',         'level': 11, 'arcana': 'Priestess'},
    {'name': 'High Pixie',      'level': 21, 'arcana': 'Priestess'},
    {'name': 'Sarasvati',       'level': 27, 'arcana': 'Priestess'},
    {'name': 'Ganga',           'level': 35, 'arcana': 'Priestess'},
    {'name': 'Parvati',         'level': 47, 'arcana': 'Priestess'},
    {'name': 'Kikuri-Hime',     'level': 53, 'arcana': 'Priestess'},
    {'name': 'Scathach',        'level': 64, 'arcana': 'Priestess', 'max': true},
    {'name': 'Leanan Sidhe',    'level': 33, 'arcana': 'Empress'},
    {'name': 'Yaksini',         'level': 50, 'arcana': 'Empress'},
    {'name': 'Laksmi',          'level': 57, 'arcana': 'Empress'},
    {'name': 'Hariti',          'level': 62, 'arcana': 'Empress'},
    {'name': 'Gabriel',         'level': 69, 'arcana': 'Empress'},
    {'name': 'Mother Harlot',   'level': 74, 'arcana': 'Empress'},
    {'name': 'Skadi',           'level': 80, 'arcana': 'Empress'},
    {'name': 'Alilat',          'level': 84, 'arcana': 'Empress', 'max': true},
    {'name': 'Forneus',         'level':  7, 'arcana': 'Emperor'},
    {'name': 'Oberon',          'level': 15, 'arcana': 'Emperor'},
    {'name': 'Take-Mikazuchi',  'level': 24, 'arcana': 'Emperor'},
    {'name': 'King Frost',      'level': 30, 'arcana': 'Emperor', 'item': true},
    {'name': 'Raja Naga',       'level': 36, 'arcana': 'Emperor'},
    {'name': 'Kingu',           'level': 46, 'arcana': 'Emperor'},
    {'name': 'Barong',          'level': 52, 'arcana': 'Emperor'},
    {'name': 'Odin',            'level': 57, 'arcana': 'Emperor', 'max': true},
    {'name': 'Omoikane',        'level':  7, 'arcana': 'Hierophant'},
    {'name': 'Berith',          'level': 13, 'arcana': 'Hierophant'},
    {'name': 'Shiisaa',         'level': 26, 'arcana': 'Hierophant'},
    {'name': 'Flauros',         'level': 33, 'arcana': 'Hierophant'},
    {'name': 'Thoth',           'level': 41, 'arcana': 'Hierophant', 'item': true},
    {'name': 'Hokuto Seikun',   'level': 47, 'arcana': 'Hierophant'},
    {'name': 'Daisoujou',       'level': 53, 'arcana': 'Hierophant', 'special': true},
    {'name': 'Kohryu',          'level': 66, 'arcana': 'Hierophant', 'max': true, 'special': true},
    {'name': 'Pixie',           'level':  2, 'arcana': 'Lovers'},
    {'name': 'Alp',             'level':  6, 'arcana': 'Lovers'},
    {'name': 'Narcissus',       'level': 20, 'arcana': 'Lovers'},
    {'name': 'Queen Mab',       'level': 27, 'arcana': 'Lovers'},
    {'name': 'Saki Mitama',     'level': 39, 'arcana': 'Lovers'},
    {'name': 'Titania',         'level': 48, 'arcana': 'Lovers'},
    {'name': 'Raphael',         'level': 61, 'arcana': 'Lovers'},
    {'name': 'Cybele',          'level': 68, 'arcana': 'Lovers', 'max': true},
    {'name': 'Ara Mitama',      'level':  6, 'arcana': 'Chariot'},
    {'name': 'Chimera',         'level':  9, 'arcana': 'Chariot'},
    {'name': 'Zouchouten',      'level': 14, 'arcana': 'Chariot'},
    {'name': 'Ares',            'level': 19, 'arcana': 'Chariot'},
    {'name': 'Oumitsunu',       'level': 30, 'arcana': 'Chariot'},
    {'name': 'Nata Taishi',     'level': 37, 'arcana': 'Chariot', 'item': true},
    {'name': 'Koumokuten',      'level': 43, 'arcana': 'Chariot'},
    {'name': 'Thor',            'level': 53, 'arcana': 'Chariot', 'max': true},
    {'name': 'Angel',           'level':  4, 'arcana': 'Justice'},
    {'name': 'Archangel',       'level': 10, 'arcana': 'Justice'},
    {'name': 'Principality',    'level': 16, 'arcana': 'Justice'},
    {'name': 'Power',           'level': 25, 'arcana': 'Justice'},
    {'name': 'Virtue',          'level': 32, 'arcana': 'Justice'},
    {'name': 'Dominion',        'level': 42, 'arcana': 'Justice'},
    {'name': 'Throne',          'level': 51, 'arcana': 'Justice'},
    {'name': 'Melchizedek',     'level': 59, 'arcana': 'Justice', 'max': true},
    {'name': 'Yomotsu Shikome', 'level':  9, 'arcana': 'Hermit'},
    {'name': 'Naga',            'level': 17, 'arcana': 'Hermit'},
    {'name': 'Lamia',           'level': 25, 'arcana': 'Hermit'},
    {'name': 'Mothman',         'level': 32, 'arcana': 'Hermit'},
    {'name': 'Taraka',          'level': 38, 'arcana': 'Hermit'},
    {'name': 'Kurama Tengu',    'level': 44, 'arcana': 'Hermit'},
    {'name': 'Nebiros',         'level': 50, 'arcana': 'Hermit', 'item': true},
    {'name': 'Kumbhanda',       'level': 56, 'arcana': 'Hermit'},
    {'name': 'Arahabaki',       'level': 60, 'arcana': 'Hermit', 'max': true, 'special': true},
    {'name': 'Fortuna',         'level': 17, 'arcana': 'Fortune'},
    {'name': 'Empusa',          'level': 23, 'arcana': 'Fortune', 'item': true},
    {'name': 'Kusi Mitama',     'level': 29, 'arcana': 'Fortune'},
    {'name': 'Clotho',          'level': 38, 'arcana': 'Fortune'},
    {'name': 'Lachesis',        'level': 45, 'arcana': 'Fortune'},
    {'name': 'Atropos',         'level': 54, 'arcana': 'Fortune'},
    {'name': 'Norn',            'level': 62, 'arcana': 'Fortune', 'max': true, 'special': true},
    {'name': 'Valkyrie',        'level': 11, 'arcana': 'Strength'},
    {'name': 'Rakshasa',        'level': 16, 'arcana': 'Strength'},
    {'name': 'Titan',           'level': 23, 'arcana': 'Strength'},
    {'name': 'Jikokuten',       'level': 29, 'arcana': 'Strength'},
    {'name': 'Hanuman',         'level': 37, 'arcana': 'Strength'},
    {'name': 'Narasimha',       'level': 46, 'arcana': 'Strength'},
    {'name': 'Kali',            'level': 55, 'arcana': 'Strength'},
    {'name': 'Siegfried',       'level': 59, 'arcana': 'Strength', 'max': true},
    {'name': 'Inugami',         'level': 10, 'arcana': 'Hanged Man'},
    {'name': 'Take-Minakata',   'level': 21, 'arcana': 'Hanged Man'},
    {'name': 'Orthrus',         'level': 28, 'arcana': 'Hanged Man'},
    {'name': 'Vasuki',          'level': 38, 'arcana': 'Hanged Man'},
    {'name': 'Ubelluris',       'level': 48, 'arcana': 'Hanged Man'},
    {'name': 'Hecatoncheires',  'level': 54, 'arcana': 'Hanged Man'},
    {'name': 'Hell Biker',      'level': 60, 'arcana': 'Hanged Man', 'item': true},
    {'name': 'Attis',           'level': 67, 'arcana': 'Hanged Man', 'max': true, 'special': true},
    {'name': 'Ghoul',           'level': 18, 'arcana': 'Death'},
    {'name': 'Pale Rider',      'level': 24, 'arcana': 'Death', 'item': true},
    {'name': 'Loa',             'level': 31, 'arcana': 'Death'},
    {'name': 'Samael',          'level': 37, 'arcana': 'Death'},
    {'name': 'Mot',             'level': 45, 'arcana': 'Death'},
    {'name': 'Alice',           'level': 56, 'arcana': 'Death', 'special': true},
    {'name': 'Thanatos',        'level': 64, 'arcana': 'Death', 'max': true, 'special': true},
    {'name': 'Nigi Mitama',     'level': 12, 'arcana': 'Temperance'},
    {'name': 'Mithra',          'level': 22, 'arcana': 'Temperance'},
    {'name': 'Genbu',           'level': 29, 'arcana': 'Temperance'},
    {'name': 'Seiryu',          'level': 36, 'arcana': 'Temperance'},
    {'name': 'Okuninushi',      'level': 44, 'arcana': 'Temperance'},
    {'name': 'Suzaku',          'level': 51, 'arcana': 'Temperance'},
    {'name': 'Byakko',          'level': 57, 'arcana': 'Temperance'},
    {'name': 'Yurlungur',       'level': 64, 'arcana': 'Temperance', 'max': true},
    {'name': 'Lilim',           'level':  8, 'arcana': 'Devil'},
    {'name': 'Vetala',          'level': 24, 'arcana': 'Devil'},
    {'name': 'Incubus',         'level': 34, 'arcana': 'Devil'},
    {'name': 'Succubus',        'level': 43, 'arcana': 'Devil'},
    {'name': 'Pazuzu',          'level': 52, 'arcana': 'Devil'},
    {'name': 'Lilith',          'level': 61, 'arcana': 'Devil', 'item': true, 'special': true},
    {'name': 'Abaddon',         'level': 68, 'arcana': 'Devil'},
    {'name': 'Beelzebub',       'level': 81, 'arcana': 'Devil', 'max': true, 'special': true},
    {'name': 'Eligor',          'level': 31, 'arcana': 'Tower'},
    {'name': 'Cu Chulainn',     'level': 40, 'arcana': 'Tower'},
    {'name': 'Bishamonten',     'level': 60, 'arcana': 'Tower'},
    {'name': 'Seiten Taisei',   'level': 67, 'arcana': 'Tower'},
    {'name': 'Masakado',        'level': 73, 'arcana': 'Tower', 'item': true, 'special': true},
    {'name': 'Mara',            'level': 77, 'arcana': 'Tower', 'special': true},
    {'name': 'Shiva',           'level': 82, 'arcana': 'Tower', 'special': true},
    {'name': 'Chi You',         'level': 86, 'arcana': 'Tower', 'max': true},
    {'name': 'Nandi',           'level': 39, 'arcana': 'Star'},
    {'name': 'Kaiwan',          'level': 49, 'arcana': 'Star'},
    {'name': 'Ganesha',         'level': 58, 'arcana': 'Star'},
    {'name': 'Garuda',          'level': 65, 'arcana': 'Star'},
    {'name': 'Kartikeya',       'level': 70, 'arcana': 'Star', 'item': true},
    {'name': 'Saturnus',        'level': 78, 'arcana': 'Star'},
    {'name': 'Helel',           'level': 88, 'arcana': 'Star', 'max': true},
    {'name': 'Gurr',            'level': 15, 'arcana': 'Moon'},
    {'name': 'Yamatano-orochi', 'level': 26, 'arcana': 'Moon'},
    {'name': 'Girimehkala',     'level': 42, 'arcana': 'Moon', 'special': true},
    {'name': 'Dionysus',        'level': 48, 'arcana': 'Moon'},
    {'name': 'Chernobog',       'level': 58, 'arcana': 'Moon'},
    {'name': 'Seth',            'level': 66, 'arcana': 'Moon'},
    {'name': 'Baal Zebul',      'level': 71, 'arcana': 'Moon'},
    {'name': 'Sandalphon',      'level': 74, 'arcana': 'Moon', 'max': true, 'special': true},
    {'name': 'Yatagarasu',      'level': 30, 'arcana': 'Sun'},
    {'name': 'Quetzalcoatl',    'level': 43, 'arcana': 'Sun'},
    {'name': 'Jatayu',          'level': 55, 'arcana': 'Sun'},
    {'name': 'Horus',           'level': 63, 'arcana': 'Sun'},
    {'name': 'Suparna',         'level': 70, 'arcana': 'Sun'},
    {'name': 'Vishnu',          'level': 78, 'arcana': 'Sun'},
    {'name': 'Asura',           'level': 85, 'arcana': 'Sun', 'max': true, 'special': true},
    {'name': 'Anubis',          'level': 59, 'arcana': 'Judgment'},
    {'name': 'Trumpeter',       'level': 65, 'arcana': 'Judgment'},
    {'name': 'Michael',         'level': 72, 'arcana': 'Judgment'},
    {'name': 'Satan',           'level': 79, 'arcana': 'Judgment'},
    {'name': 'Lucifer',         'level': 89, 'arcana': 'Judgment', 'special': true},
    {'name': 'Messiah',         'level': 90, 'arcana': 'Judgment', 'max': true, 'special': true},
    {'name': 'Uriel',           'level': 63, 'arcana': 'Aeon'},
    {'name': 'Nidhoggr',        'level': 69, 'arcana': 'Aeon'},
    {'name': 'Ananta',          'level': 75, 'arcana': 'Aeon'},
    {'name': 'Atavaka',         'level': 80, 'arcana': 'Aeon'},
    {'name': 'Metatron',        'level': 87, 'arcana': 'Aeon', 'max': true, 'special': true},
]

type_lists = [
('slash', ['Yaksini','Barong','Raphael','Chimera','Ares','Taraka','Valkyrie','Rakshasa','Titan','Jikokuten','Hanuman','Narasimha','Kali','Siegfried','Masakado','Ganesha','Gurr','Girimehkala',]),
('strike',['Ara Mitama','Zouchouten','Oumitsunu','Nata Taishi','Koumokuten','Melchizedek','Ubelluris','Hecatoncheires','Helel','Yamatano-orochi','Vishnu',]),
('pierce',['Scathach','Raja Naga','Naga','Eligor','Cu Chulainn','Seiten Taisei','Mara','Chi You','Kartikeya',]),
('fire',['Orpheus','Nekomata','Pyro Jack','Hua Po','Sati','Rangda','Surt','Berith','Flauros','Kumbhanda','Orthrus','Hell Biker','Okuninushi','Suzaku','Bishamonten','Saturnus','Seth','Asura',]),
('ice',['Jack Frost','Apsaras','High Pixie','Sarasvati','Ganga','Parvati','Laksmi','Gabriel','Skadi','Forneus','King Frost','Shiisaa','Genbu','Yurlungur',]),
('elec',['Oberon','Take-Mikazuchi','Odin','Omoikane','Thoth','Hokuto Seikun','Thor','Take-Minakata','Byakko','Shiva','Dionysus','Michael',]),
('wind',['Orobas','Angel','Fortuna','Empusa','Kusi Mitama','Clotho','Lachesis','Atropos','Norn','Nigi Mitama','Seiryu','Nandi','Garuda','Quetzalcoatl','Jatayu','Suparna',]),
('light',['Daisoujou','Archangel','Principality','Power','Virtue','Dominion','Throne','Vasuki','Mithra','Sandalphon','Horus','Uriel','Atavaka','Metatron',]),
('dark',['Mother Harlot','Yomotsu Shikome','Lamia','Ghoul','Pale Rider','Loa','Samael','Mot','Alice','Thanatos','Chernobog','Baal Zebul','Lucifer','Nidhoggr',]),
('l&d',['Anubis','Trumpeter','Satan','Messiah',]),
('recovery',['Unicorn','Kikuri-Hime','Leanan Sidhe','Hariti','Alilat','Kingu','Kohryu','Pixie','Alp','Queen Mab','Saki Mitama','Titania','Cybele','Attis','Yatagarasu','Ananta',]),
('status',['Narcissus','Mothman','Kurama Tengu','Nebiros','Arahabaki','Inugami','Lilim','Vetala','Incubus','Succubus','Pazuzu','Lilith','Abaddon','Beelzebub','Kaiwan',]),
('all',['Slime','Legion','Black Frost','Ose','Decarabia','Loki','Susano-o','Orpheus Telos',])]

ids = {'Gurr': 128, 'Orobas': 71, 'Byakko': 99, 'Hell Biker': 158, 'Seiryu': 101, 'Orpheus': 1, 'Pyro Jack': 6, 'Hariti': 23, 'Jikokuten': 80, 'Vasuki': 85, 'Koumokuten': 82, 'Garuda': 120, 'Mot': 93, 'Asura': 139, 'Helel': 117, 'Nandi': 123, 'Omoikane': 38, 'Alice': 91, 'Throne': 49, 'Forneus': 33, 'Thanatos': 90, 'Gabriel': 142, 'Pale Rider': 97, 'Bishamonten': 78, 'Seth': 92, 'Okuninushi': 30, 'Thor': 77, 'Abaddon': 106, 'Orpheus Telos': 169, 'Ghoul': 159, 'Suparna': 165, 'Ganesha': 122, 'Rangda': 9, 'Angel': 61, 'Ara Mitama': 53, 'Yaksini': 149, 'Naga': 68, 'Attis': 84, 'Berith': 130, 'Atropos': 70, 'Hokuto Seikun': 143, 'Queen Mab': 44, 'Mara': 162, 'Trumpeter': 144, 'Lamia': 27, 'Yatagarasu': 137, 'Nebiros': 64, 'Ubelluris': 88, 'Vishnu': 132, 'Lucifer': 166, 'Ares': 50, 'Kali': 24, 'Sati': 18, 'Black Frost': 119, 'Lilim': 110, 'Kartikeya': 163, 'Quetzalcoatl': 136, 'Horus': 135, 'Kaiwan': 121, 'Flauros': 3, 'Atavaka': 168, 'Virtue': 58, 'Uriel': 47, 'Odin': 28, 'Suzaku': 100, 'Zouchouten': 83, 'Laksmi': 15, 'Nekomata': 5, 'Beelzebub': 104, 'Ananta': 37, 'High Pixie': 148, 'Alilat': 62, 'Dionysus': 125, 'Take-Minakata': 87, 'Messiah': 138, 'Nigi Mitama': 102, 'Lachesis': 72, 'Clotho': 75, 'Ganga': 25, 'Ose': 12, 'Jack Frost': 7, 'Archangel': 60, 'Loa': 96, 'Parvati': 16, 'Rakshasa': 156, 'Yurlungur': 160, 'Skadi': 22, 'Oumitsunu': 116, 'Baal Zebul': 164, 'Satan': 141, 'Chernobog': 124, 'Hua Po': 147, 'Siegfried': 57, 'Lilith': 107, 'Pixie': 46, 'Scathach': 8, 'Surt': 48, 'Eligor': 74, 'Fortuna': 76, 'Samael': 94, 'Mithra': 35, 'Kikuri-Hime': 17, 'Melchizedek': 55, 'Dominion': 56, 'Daisoujou': 36, 'Kohryu': 34, 'Barong': 133, 'Succubus': 109, 'Empusa': 155, 'Arahabaki': 63, 'Titan': 51, 'Apsaras': 14, 'Sarasvati': 19, 'Kumbhanda': 154, 'Chimera': 52, 'Incubus': 108, 'Vetala': 95, 'Narasimha': 126, 'Legion': 129, 'Orthrus': 86, 'Girimehkala': 127, 'Principality': 39, 'Inugami': 89, 'Shiva': 112, 'Decarabia': 65, 'Hecatoncheires': 157, 'Nidhoggr': 167, 'Genbu': 103, 'Oberon': 42, 'Nata Taishi': 10, 'Saki Mitama': 73, 'Metatron': 140, 'Pazuzu': 161, 'Susano-o': 2, 'Power': 59, 'Yomotsu Shikome': 67, 'King Frost': 29, 'Norn': 69, 'Mother Harlot': 105, 'Jatayu': 134, 'Unicorn': 20, 'Cu Chulainn': 11, 'Thoth': 151, 'Raja Naga': 32, 'Kusi Mitama': 13, 'Valkyrie': 54, 'Seiten Taisei': 114, 'Michael': 98, 'Titania': 41, 'Raphael': 40, 'Hanuman': 81, 'Yamatano-orochi': 115, 'Sandalphon': 118, 'Kurama Tengu': 66, 'Masakado': 113, 'Chi You': 111, 'Take-Mikazuchi': 79, 'Taraka': 26, 'Mothman': 153, 'Anubis': 145, 'Slime': 146, 'Loki': 4, 'Leanan Sidhe': 45, 'Narcissus': 43, 'Shiisaa': 150, 'Cybele': 21, 'Saturnus': 131, 'Alp': 152, 'Kingu': 31}

with open('pdb.txt', 'w') as f:
  by_name = {}
  for i,persona in enumerate(personas_a):
    name = persona['name']
    by_name[name] = persona
    persona['id'] = ids[name]

  for type, names in type_lists:
    for name in names:
      persona = by_name[name]
      f.write("Persona(%d, '%s',%d,'%s','%s',[]" % (persona['id'], name, int(persona['level']), persona['arcana'], type))
      if 'special' in persona:
        f.write(", special_=True")
      if 'max' in persona:
        f.write(", restricted_='max'")
      if 'item' in persona:
        f.write(", restricted_='item'")
      f.write("),\n")

  
