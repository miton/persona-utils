from collections import defaultdict
from math import floor

#restrictions: request or max link
#inherit types
#skill types
#fusion arcana results

class Persona(object):
  def __init__(self, id_, name_, base_level_, arcana_, inherit_type_, skills_, restricted_ = False, special_ = False):
    self.id = id_
    self.name = name_
    self.base_level = base_level_
    self.arcana = arcana_
    self.inherit_type = inherit_type_
    self.skills = skills_
    self.special = special_
    self.restricted = restricted_
    self.inherited_skills = []

personas = [
Persona('Yaksini',50,'Empress','slash',[]),
Persona('Barong',52,'Emperor','slash',[]),
Persona('Raphael',61,'Lovers','slash',[]),
Persona('Chimera',9,'Chariot','slash',[]),
Persona('Ares',19,'Chariot','slash',[]),
Persona('Taraka',38,'Hermit','slash',[]),
Persona('Valkyrie',11,'Strength','slash',[]),
Persona('Rakshasa',16,'Strength','slash',[]),
Persona('Titan',23,'Strength','slash',[]),
Persona('Jikokuten',29,'Strength','slash',[]),
Persona('Hanuman',37,'Strength','slash',[]),
Persona('Narasimha',46,'Strength','slash',[]),
Persona('Kali',55,'Strength','slash',[]),
Persona('Siegfried',59,'Strength','slash',[]),
Persona('Masakado',73,'Tower','slash',[]),
Persona('Ganesha',58,'Star','slash',[]),
Persona('Gurr',15,'Moon','slash',[]),
Persona('Girimehkala',42,'Moon','slash',[]),
Persona('Ara Mitama',6,'Chariot','strike',[]),
Persona('Zouchouten',14,'Chariot','strike',[]),
Persona('Oumitsunu',30,'Chariot','strike',[]),
Persona('Nata Taishi',37,'Chariot','strike',[]),
Persona('Koumokuten',43,'Chariot','strike',[]),
Persona('Melchizedek',59,'Justice','strike',[]),
Persona('Ubelluris',48,'Hanged Man','strike',[]),
Persona('Hecatoncheires',54,'Hanged Man','strike',[]),
Persona('Helel',88,'Star','strike',[]),
Persona('Yamatano-orochi',26,'Moon','strike',[]),
Persona('Vishnu',78,'Sun','strike',[]),
Persona('Scathach',64,'Priestess','pierce',[]),
Persona('Raja Naga',36,'Emperor','pierce',[]),
Persona('Naga',17,'Hermit','pierce',[]),
Persona('Eligor',31,'Tower','pierce',[]),
Persona('Cu Chulainn',40,'Tower','pierce',[]),
Persona('Seiten Taisei',67,'Tower','pierce',[]),
Persona('Mara',77,'Tower','pierce',[]),
Persona('Chi You',86,'Tower','pierce',[]),
Persona('Kartikeya',70,'Star','pierce',[]),
Persona('Orpheus',1,'Fool','fire',[]),
Persona('Nekomata',5,'Magician','fire',[]),
Persona('Pyro Jack',14,'Magician','fire',[]),
Persona('Hua Po',20,'Magician','fire',[]),
Persona('Sati',28,'Magician','fire',[]),
Persona('Rangda',40,'Magician','fire',[]),
Persona('Surt',52,'Magician','fire',[]),
Persona('Berith',13,'Hierophant','fire',[]),
Persona('Flauros',33,'Hierophant','fire',[]),
Persona('Kumbhanda',56,'Hermit','fire',[]),
Persona('Orthrus',28,'Hanged Man','fire',[]),
Persona('Hell Biker',60,'Hanged Man','fire',[]),
Persona('Okuninushi',44,'Temperance','fire',[]),
Persona('Suzaku',51,'Temperance','fire',[]),
Persona('Bishamonten',60,'Tower','fire',[]),
Persona('Saturnus',78,'Star','fire',[]),
Persona('Seth',66,'Moon','fire',[]),
Persona('Asura',85,'Sun','fire',[]),
Persona('Jack Frost',8,'Magician','ice',[]),
Persona('Apsaras',3,'Priestess','ice',[]),
Persona('High Pixie',21,'Priestess','ice',[]),
Persona('Sarasvati',27,'Priestess','ice',[]),
Persona('Ganga',35,'Priestess','ice',[]),
Persona('Parvati',47,'Priestess','ice',[]),
Persona('Laksmi',57,'Empress','ice',[]),
Persona('Gabriel',69,'Empress','ice',[]),
Persona('Skadi',80,'Empress','ice',[]),
Persona('Forneus',7,'Emperor','ice',[]),
Persona('King Frost',30,'Emperor','ice',[]),
Persona('Shiisaa',26,'Hierophant','ice',[]),
Persona('Genbu',29,'Temperance','ice',[]),
Persona('Yurlungur',64,'Temperance','ice',[]),
Persona('Oberon',15,'Emperor','elec',[]),
Persona('Take-mikazuchi',24,'Emperor','elec',[]),
Persona('Odin',57,'Emperor','elec',[]),
Persona('Omoikane',7,'Hierophant','elec',[]),
Persona('Thoth',41,'Hierophant','elec',[]),
Persona('Hokuto Seikun',47,'Hierophant','elec',[]),
Persona('Thor',53,'Chariot','elec',[]),
Persona('Take-minakata',21,'Hanged Man','elec',[]),
Persona('Byakko',57,'Temperance','elec',[]),
Persona('Shiva',82,'Tower','elec',[]),
Persona('Dionysus',48,'Moon','elec',[]),
Persona('Michael',72,'Judgment','elec',[]),
Persona('Orobas',34,'Magician','wind',[]),
Persona('Angel',4,'Justice','wind',[]),
Persona('Fortuna',17,'Fortune','wind',[]),
Persona('Empusa',23,'Fortune','wind',[]),
Persona('Kusi Mitama',29,'Fortune','wind',[]),
Persona('Clotho',38,'Fortune','wind',[]),
Persona('Lachesis',45,'Fortune','wind',[]),
Persona('Atropos',54,'Fortune','wind',[]),
Persona('Norn',62,'Fortune','wind',[]),
Persona('Nigi Mitama',12,'Temperance','wind',[]),
Persona('Seiryuu',36,'Temperance','wind',[]),
Persona('Nandi',39,'Star','wind',[]),
Persona('Garuda',65,'Star','wind',[]),
Persona('Quetzalcoatl',43,'Sun','wind',[]),
Persona('Jatayu',55,'Sun','wind',[]),
Persona('Suparna',70,'Sun','wind',[]),
Persona('Daisoujou',53,'Hierophant','light',[]),
Persona('Archangel',10,'Justice','light',[]),
Persona('Principality',16,'Justice','light',[]),
Persona('Power',25,'Justice','light',[]),
Persona('Virtue',32,'Justice','light',[]),
Persona('Dominion',42,'Justice','light',[]),
Persona('Throne',51,'Justice','light',[]),
Persona('Vasuki',38,'Hanged Man','light',[]),
Persona('Mithra',22,'Temperance','light',[]),
Persona('Sandalphon',74,'Moon','light',[]),
Persona('Horus',63,'Sun','light',[]),
Persona('Uriel',63,'Aeon','light',[]),
Persona('Atavaka',80,'Aeon','light',[]),
Persona('Metatron',87,'Aeon','light',[]),
Persona('Mother Harlot',74,'Empress','dark',[]),
Persona('Yomotsu Shikome',9,'Hermit','dark',[]),
Persona('Lamia',25,'Hermit','dark',[]),
Persona('Ghoul',18,'Death','dark',[]),
Persona('Pale Rider',24,'Death','dark',[]),
Persona('Loa',31,'Death','dark',[]),
Persona('Samael',37,'Death','dark',[]),
Persona('Mot',45,'Death','dark',[]),
Persona('Alice',56,'Death','dark',[]),
Persona('Thanatos',64,'Death','dark',[]),
Persona('Chernobog',58,'Moon','dark',[]),
Persona('Baal Zebul',71,'Moon','dark',[]),
Persona('Lucifer',89,'Judgment','dark',[]),
Persona('Nidhoggr',69,'Aeon','dark',[]),
Persona('Anubis',59,'Judgment','l&d',[]),
Persona('Trumpeter',65,'Judgment','l&d',[]),
Persona('Satan',79,'Judgment','l&d',[]),
Persona('Messiah',90,'Judgment','l&d',[]),
Persona('Unicorn',11,'Priestess','recovery',[]),
Persona('Kikuri-hime',53,'Priestess','recovery',[]),
Persona('Leanan Sidhe',33,'Empress','recovery',[]),
Persona('Hariti',62,'Empress','recovery',[]),
Persona('Alilat',84,'Empress','recovery',[]),
Persona('Kingu',46,'Emperor','recovery',[]),
Persona('Kohryu',66,'Hierophant','recovery',[]),
Persona('Pixie',2,'Lovers','recovery',[]),
Persona('Alp',6,'Lovers','recovery',[]),
Persona('Queen Mab',27,'Lovers','recovery',[]),
Persona('Saki Mitama',39,'Lovers','recovery',[]),
Persona('Titania',48,'Lovers','recovery',[]),
Persona('Cybele',68,'Lovers','recovery',[]),
Persona('Attis',67,'Hanged Man','recovery',[]),
Persona('Yatagarasu',30,'Sun','recovery',[]),
Persona('Ananta',75,'Aeon','recovery',[]),
Persona('Narcissus',20,'Lovers','status',[]),
Persona('Mothman',32,'Hermit','status',[]),
Persona('Kurama Tengu',44,'Hermit','status',[]),
Persona('Nebiros',50,'Hermit','status',[]),
Persona('Arahabaki',60,'Hermit','status',[]),
Persona('Inugami',10,'Hanged Man','status',[]),
Persona('Lilim',8,'Devil','status',[]),
Persona('Vetala',24,'Devil','status',[]),
Persona('Incubus',34,'Devil','status',[]),
Persona('Succubus',43,'Devil','status',[]),
Persona('Pazuzu',52,'Devil','status',[]),
Persona('Lilith',61,'Devil','status',[]),
Persona('Abaddon',68,'Devil','status',[]),
Persona('Beelzebub',81,'Devil','status',[]),
Persona('Kaiwan',49,'Star','status',[]),
Persona('Slime',12,'Fool','all',[]),
Persona('Legion',22,'Fool','all',[]),
Persona('Black Frost',34,'Fool','all',[]),
Persona('Ose',44,'Fool','all',[]),
Persona('Decarabia',50,'Fool','all',[]),
Persona('Loki',58,'Fool','all',[]),
Persona('Susano-o',76,'Fool','all',[]),
Persona('Orpheus Telos',90,'Fool','all',[]),
]

persona_by_name = {}
persona_by_arcana = defaultdict(list)
persona_by_id = sorted(personas, key=lambda i: i.id)

for persona in personas:
  persona_by_name[persona.name] = persona
  persona_by_arcana[persona.arcana].append(persona)

for arcana in persona_by_arcana.keys():
  persona_by_arcana[arcana].sort(key=lambda i: i.base_level)
  #print map(lambda i: i.name, persona_by_arcana[arcana])

def can_inherit(persona_type, skill_type):
  #missing the types I don't care about right now
  possibilities = {
    'all'      : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
    'status'   : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
    'l&d'      : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
    'recovery' : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
    'slash'    : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'strike'   : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'pierce'   : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}   
    'fire'     : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'ice'      : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'elec'     : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'wind'     : {'fire': False, 'ice' : False, 'elec' : False, 'wind' : False}
    'light'    : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
    'dark'     : {'fire':  True, 'ice' :  True, 'elec' :  True, 'wind' :  True}
  }
  return possibilities[persona_type][skill_type]



def fusion_2(a, b):
  level = 1 + floor((a.level + b.level) / 2)
  
  
     
