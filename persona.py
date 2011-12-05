from collections import defaultdict
from math import floor

#restrictions: request or max link
#inherit types
#skill types
#fusion arcana results
#rename to BasePersona and make Persona the ones you actually have, should rename the arrays/dicts too
class Persona(object):
  def __init__(self, id_, name_, base_level_, arcana_, inherit_type_, skills_, restricted_ = False, special_ = False):
    self.id = id_
    self.name = name_
    self.base_level = base_level_
    self.level = base_level_
    self.arcana = arcana_
    self.inherit_type = inherit_type_
    self.skills = skills_
    self.special = special_
    self.restricted = restricted_
    self.inherited_skills = []
  
  def __str__(self):
    return self.name
  
  def __repr__(self):
    return str(self)
  
  def __eq__(self, b):
    #with fusions you need equality checks and the objects might not be the same
    #not sure what other times you might compare them
    return self.id == b.id


personas = [Persona(149, 'Yaksini',50,'Empress','slash',[]),
Persona(133, 'Barong',52,'Emperor','slash',[]),
Persona(40, 'Raphael',61,'Lovers','slash',[]),
Persona(52, 'Chimera',9,'Chariot','slash',[]),
Persona(50, 'Ares',19,'Chariot','slash',[]),
Persona(26, 'Taraka',38,'Hermit','slash',[]),
Persona(54, 'Valkyrie',11,'Strength','slash',[]),
Persona(156, 'Rakshasa',16,'Strength','slash',[]),
Persona(51, 'Titan',23,'Strength','slash',[]),
Persona(80, 'Jikokuten',29,'Strength','slash',[]),
Persona(81, 'Hanuman',37,'Strength','slash',[]),
Persona(126, 'Narasimha',46,'Strength','slash',[]),
Persona(24, 'Kali',55,'Strength','slash',[]),
Persona(57, 'Siegfried',59,'Strength','slash',[], restricted_='max'),
Persona(113, 'Masakado',73,'Tower','slash',[], special_=True, restricted_='item'),
Persona(122, 'Ganesha',58,'Star','slash',[]),
Persona(128, 'Gurr',15,'Moon','slash',[]),
Persona(127, 'Girimehkala',42,'Moon','slash',[], special_=True),
Persona(53, 'Ara Mitama',6,'Chariot','strike',[]),
Persona(83, 'Zouchouten',14,'Chariot','strike',[]),
Persona(116, 'Oumitsunu',30,'Chariot','strike',[]),
Persona(10, 'Nata Taishi',37,'Chariot','strike',[], restricted_='item'),
Persona(82, 'Koumokuten',43,'Chariot','strike',[]),
Persona(55, 'Melchizedek',59,'Justice','strike',[], restricted_='max'),
Persona(88, 'Ubelluris',48,'Hanged Man','strike',[]),
Persona(157, 'Hecatoncheires',54,'Hanged Man','strike',[]),
Persona(117, 'Helel',88,'Star','strike',[], restricted_='max'),
Persona(115, 'Yamatano-orochi',26,'Moon','strike',[]),
Persona(132, 'Vishnu',78,'Sun','strike',[]),
Persona(8, 'Scathach',64,'Priestess','pierce',[], restricted_='max'),
Persona(32, 'Raja Naga',36,'Emperor','pierce',[]),
Persona(68, 'Naga',17,'Hermit','pierce',[]),
Persona(74, 'Eligor',31,'Tower','pierce',[]),
Persona(11, 'Cu Chulainn',40,'Tower','pierce',[]),
Persona(114, 'Seiten Taisei',67,'Tower','pierce',[]),
Persona(162, 'Mara',77,'Tower','pierce',[], special_=True),
Persona(111, 'Chi You',86,'Tower','pierce',[], restricted_='max'),
Persona(163, 'Kartikeya',70,'Star','pierce',[], restricted_='item'),
Persona(1, 'Orpheus',1,'Fool','fire',[], special_=True),
Persona(5, 'Nekomata',5,'Magician','fire',[]),
Persona(6, 'Pyro Jack',14,'Magician','fire',[]),
Persona(147, 'Hua Po',20,'Magician','fire',[], restricted_='item'),
Persona(18, 'Sati',28,'Magician','fire',[]),
Persona(9, 'Rangda',40,'Magician','fire',[]),
Persona(48, 'Surt',52,'Magician','fire',[], restricted_='max'),
Persona(130, 'Berith',13,'Hierophant','fire',[]),
Persona(3, 'Flauros',33,'Hierophant','fire',[]),
Persona(154, 'Kumbhanda',56,'Hermit','fire',[]),
Persona(86, 'Orthrus',28,'Hanged Man','fire',[]),
Persona(158, 'Hell Biker',60,'Hanged Man','fire',[], restricted_='item'),
Persona(30, 'Okuninushi',44,'Temperance','fire',[]),
Persona(100, 'Suzaku',51,'Temperance','fire',[]),
Persona(78, 'Bishamonten',60,'Tower','fire',[]),
Persona(131, 'Saturnus',78,'Star','fire',[]),
Persona(92, 'Seth',66,'Moon','fire',[]),
Persona(139, 'Asura',85,'Sun','fire',[], special_=True, restricted_='max'),
Persona(7, 'Jack Frost',8,'Magician','ice',[]),
Persona(14, 'Apsaras',3,'Priestess','ice',[]),
Persona(148, 'High Pixie',21,'Priestess','ice',[]),
Persona(19, 'Sarasvati',27,'Priestess','ice',[]),
Persona(25, 'Ganga',35,'Priestess','ice',[]),
Persona(16, 'Parvati',47,'Priestess','ice',[]),
Persona(15, 'Laksmi',57,'Empress','ice',[]),
Persona(142, 'Gabriel',69,'Empress','ice',[]),
Persona(22, 'Skadi',80,'Empress','ice',[]),
Persona(33, 'Forneus',7,'Emperor','ice',[]),
Persona(29, 'King Frost',30,'Emperor','ice',[], restricted_='item'),
Persona(150, 'Shiisaa',26,'Hierophant','ice',[]),
Persona(103, 'Genbu',29,'Temperance','ice',[]),
Persona(160, 'Yurlungur',64,'Temperance','ice',[], restricted_='max'),
Persona(42, 'Oberon',15,'Emperor','elec',[]),
Persona(79, 'Take-Mikazuchi',24,'Emperor','elec',[]),
Persona(28, 'Odin',57,'Emperor','elec',[], restricted_='max'),
Persona(38, 'Omoikane',7,'Hierophant','elec',[]),
Persona(151, 'Thoth',41,'Hierophant','elec',[], restricted_='item'),
Persona(143, 'Hokuto Seikun',47,'Hierophant','elec',[]),
Persona(77, 'Thor',53,'Chariot','elec',[], restricted_='max'),
Persona(87, 'Take-Minakata',21,'Hanged Man','elec',[]),
Persona(99, 'Byakko',57,'Temperance','elec',[]),
Persona(112, 'Shiva',82,'Tower','elec',[], special_=True),
Persona(125, 'Dionysus',48,'Moon','elec',[]),
Persona(98, 'Michael',72,'Judgment','elec',[]),
Persona(71, 'Orobas',34,'Magician','wind',[]),
Persona(61, 'Angel',4,'Justice','wind',[]),
Persona(76, 'Fortuna',17,'Fortune','wind',[]),
Persona(155, 'Empusa',23,'Fortune','wind',[], restricted_='item'),
Persona(13, 'Kusi Mitama',29,'Fortune','wind',[]),
Persona(75, 'Clotho',38,'Fortune','wind',[]),
Persona(72, 'Lachesis',45,'Fortune','wind',[]),
Persona(70, 'Atropos',54,'Fortune','wind',[]),
Persona(69, 'Norn',62,'Fortune','wind',[], special_=True, restricted_='max'),
Persona(102, 'Nigi Mitama',12,'Temperance','wind',[]),
Persona(101, 'Seiryu',36,'Temperance','wind',[]),
Persona(123, 'Nandi',39,'Star','wind',[]),
Persona(120, 'Garuda',65,'Star','wind',[]),
Persona(136, 'Quetzalcoatl',43,'Sun','wind',[]),
Persona(134, 'Jatayu',55,'Sun','wind',[]),
Persona(165, 'Suparna',70,'Sun','wind',[]),
Persona(36, 'Daisoujou',53,'Hierophant','light',[], special_=True),
Persona(60, 'Archangel',10,'Justice','light',[]),
Persona(39, 'Principality',16,'Justice','light',[]),
Persona(59, 'Power',25,'Justice','light',[]),
Persona(58, 'Virtue',32,'Justice','light',[]),
Persona(56, 'Dominion',42,'Justice','light',[]),
Persona(49, 'Throne',51,'Justice','light',[]),
Persona(85, 'Vasuki',38,'Hanged Man','light',[]),
Persona(35, 'Mithra',22,'Temperance','light',[]),
Persona(118, 'Sandalphon',74,'Moon','light',[], special_=True, restricted_='max'),
Persona(135, 'Horus',63,'Sun','light',[]),
Persona(47, 'Uriel',63,'Aeon','light',[]),
Persona(168, 'Atavaka',80,'Aeon','light',[]),
Persona(140, 'Metatron',87,'Aeon','light',[], special_=True, restricted_='max'),
Persona(105, 'Mother Harlot',74,'Empress','dark',[]),
Persona(67, 'Yomotsu Shikome',9,'Hermit','dark',[]),
Persona(27, 'Lamia',25,'Hermit','dark',[]),
Persona(159, 'Ghoul',18,'Death','dark',[]),
Persona(97, 'Pale Rider',24,'Death','dark',[], restricted_='item'),
Persona(96, 'Loa',31,'Death','dark',[]),
Persona(94, 'Samael',37,'Death','dark',[]),
Persona(93, 'Mot',45,'Death','dark',[]),
Persona(91, 'Alice',56,'Death','dark',[], special_=True),
Persona(90, 'Thanatos',64,'Death','dark',[], special_=True, restricted_='max'),
Persona(124, 'Chernobog',58,'Moon','dark',[]),
Persona(164, 'Baal Zebul',71,'Moon','dark',[]),
Persona(166, 'Lucifer',89,'Judgment','dark',[], special_=True),
Persona(167, 'Nidhoggr',69,'Aeon','dark',[]),
Persona(145, 'Anubis',59,'Judgment','l&d',[]),
Persona(144, 'Trumpeter',65,'Judgment','l&d',[]),
Persona(141, 'Satan',79,'Judgment','l&d',[]),
Persona(138, 'Messiah',90,'Judgment','l&d',[], special_=True, restricted_='max'),
Persona(20, 'Unicorn',11,'Priestess','recovery',[]),
Persona(17, 'Kikuri-Hime',53,'Priestess','recovery',[]),
Persona(45, 'Leanan Sidhe',33,'Empress','recovery',[]),
Persona(23, 'Hariti',62,'Empress','recovery',[]),
Persona(62, 'Alilat',84,'Empress','recovery',[], restricted_='max'),
Persona(31, 'Kingu',46,'Emperor','recovery',[]),
Persona(34, 'Kohryu',66,'Hierophant','recovery',[], special_=True, restricted_='max'),
Persona(46, 'Pixie',2,'Lovers','recovery',[]),
Persona(152, 'Alp',6,'Lovers','recovery',[]),
Persona(44, 'Queen Mab',27,'Lovers','recovery',[]),
Persona(73, 'Saki Mitama',39,'Lovers','recovery',[]),
Persona(41, 'Titania',48,'Lovers','recovery',[]),
Persona(21, 'Cybele',68,'Lovers','recovery',[], restricted_='max'),
Persona(84, 'Attis',67,'Hanged Man','recovery',[], special_=True, restricted_='max'),
Persona(137, 'Yatagarasu',30,'Sun','recovery',[]),
Persona(37, 'Ananta',75,'Aeon','recovery',[]),
Persona(43, 'Narcissus',20,'Lovers','status',[]),
Persona(153, 'Mothman',32,'Hermit','status',[]),
Persona(66, 'Kurama Tengu',44,'Hermit','status',[]),
Persona(64, 'Nebiros',50,'Hermit','status',[], restricted_='item'),
Persona(63, 'Arahabaki',60,'Hermit','status',[], special_=True, restricted_='max'),
Persona(89, 'Inugami',10,'Hanged Man','status',[]),
Persona(110, 'Lilim',8,'Devil','status',[]),
Persona(95, 'Vetala',24,'Devil','status',[]),
Persona(108, 'Incubus',34,'Devil','status',[]),
Persona(109, 'Succubus',43,'Devil','status',[]),
Persona(161, 'Pazuzu',52,'Devil','status',[]),
Persona(107, 'Lilith',61,'Devil','status',[], special_=True, restricted_='item'),
Persona(106, 'Abaddon',68,'Devil','status',[]),
Persona(104, 'Beelzebub',81,'Devil','status',[], special_=True, restricted_='max'),
Persona(121, 'Kaiwan',49,'Star','status',[]),
Persona(146, 'Slime',12,'Fool','all',[]),
Persona(129, 'Legion',22,'Fool','all',[]),
Persona(119, 'Black Frost',34,'Fool','all',[], special_=True),
Persona(12, 'Ose',44,'Fool','all',[]),
Persona(65, 'Decarabia',50,'Fool','all',[]),
Persona(4, 'Loki',58,'Fool','all',[]),
Persona(2, 'Susano-o',76,'Fool','all',[], special_=True, restricted_='max'),
Persona(169, 'Orpheus Telos',90,'Fool','all',[], special_=True),
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


  
  
     
