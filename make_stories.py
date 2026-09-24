import json, re
pairs=[
('The Seed Project','Mia','school garden','three sunflower seeds','measure their growth','a chart','a small science project'),
('The Lost Bookmark','Liam','library','a blue bookmark','ask the librarian','a reading shelf','a new book to explore'),
('The Rainy Race','Ava','park','a paper boat','watch which boat travels farthest','a puddle','a lesson about water'),
('The Solar Oven','Noah','back garden','a cardboard box','test how sunlight warms it','a simple oven','a warm snack'),
('The Kindness Jar','Zoe','classroom','a glass jar','write kind actions','a jar full of notes','kindness can grow'),
('The Map Mystery','Ethan','community centre','a hand-drawn map','follow three clues','a reading corner','a message about teamwork'),
('The Bird Watch','Ella','school yard','a notebook','record birds without disturbing them','a quiet observation spot','new facts about local birds'),
('The Number Shop','Jayden','pretend shop','ten paper coins','calculate totals and change','a maths game','a stronger maths skill'),
('The Recycling Team','Amara','school courtyard','three labelled bins','sort clean items','a recycling station','a cleaner school'),
('The Moon Journal','Kai','bedroom window','a moon journal','draw the moon each evening','a series of sketches','patterns in the night sky'),
('The Bridge Builders','Sofia','classroom','paper and craft sticks','test different designs','a strong paper bridge','mistakes can improve ideas'),
('The Story Picnic','Ben','park','two storybooks','take turns reading aloud','a shady tree','a favourite story'),
('The Weather Watchers','Lara','school veranda','a thermometer','record temperature and clouds','a weather chart','how weather changes'),
('The Secret Ingredient','Daniel','kitchen','a recipe card','measure ingredients carefully','a fruit salad','why measurements matter'),
('The Bicycle Bell','Mila','neighbourhood','a loose bicycle bell','check and tighten it safely','a working bell','how small repairs need care'),
('The Ocean Poster','Sam','classroom','blue paper and drawings','organise facts about oceans','a colourful poster','new ocean facts'),
('The Puzzle Box','Leah','study desk','a wooden puzzle box','solve number clues','a hidden note','patience helps solve problems'),
('The Garden Visitor','Theo','vegetable garden','a tiny green frog','watch it quietly','a safe place under a leaf','respect for living things'),
('The Reading Challenge','Nia','home reading corner','a reading tracker','read for fifteen minutes','a completed tracker','reading every day builds confidence'),
('The Wind Experiment','Luke','playground','a pinwheel','compare it in calm and windy spots','a spinning pinwheel','wind can move objects'),
('The Class Museum','Ruby','classroom','old postcards','label and arrange them','a mini museum','history can be interesting'),
('The Helpful Robot','Oliver','garage','cardboard wheels','design a robot to carry blocks','a working model','planning before building helps'),
('The Seedling Rescue','Grace','greenhouse','a drooping seedling','check water and sunlight','a healthier plant','plants need the right care'),
('The Shadow Clock','Caleb','school field','a stick and chalk','mark the shadow at different times','a simple shadow clock','the sun appears to move across the sky'),
('The Word Detective','Isla','reading room','a dictionary','find meanings for tricky words','a word list','context helps explain words'),
('The Music Pattern','Adam','music room','a small drum','copy a rhythm and create a new one','a short rhythm','patterns appear in music'),
('The Safe Crossing','Emma','street corner','a bright safety card','practise the safe crossing steps','a safe crossing plan','look, listen and think before crossing'),
('The Budget Picnic','Finn','kitchen table','a small budget','choose snacks without spending too much','a picnic list','planning helps manage money'),
('The Mountain Model','Chloe','science table','clay and cardboard','build a mountain model','a model with labelled parts','landforms have different shapes'),
('The Library Helper','Leo','library','a trolley of books','sort books by topic','an organised shelf','labels make finding books easier'),
('The Clean Water Test','Aria','science club','two clear cups','compare clean and muddy water','a simple observation sheet','water quality matters'),
('The Friendship Flag','Max','classroom','coloured paper','design a flag together','a class flag','listening helps groups work well'),
('The Mini Farm','Poppy','back yard','small pots and soil','plant herbs and label them','a mini herb garden','plants can be grown in small spaces'),
('The Traffic Light Game','Ryan','driveway','red, yellow and green cards','practise safe road decisions','a safety game','colours can signal actions'),
('The Star Collector','Mason','bedroom','a star chart','earn stars for reading practice','a full chart','small goals can build a habit'),
('The Fraction Pizza','Hannah','classroom','a paper pizza','divide it into equal parts','a fraction pizza','fractions describe equal parts'),
('The Recycling Robot','Aiden','school hall','clean boxes and bottles','build a robot from reusable items','a recycled robot','old materials can have new uses'),
('The Quiet Library','Sienna','library','a whisper card','help visitors keep voices low','a calm reading space','quiet spaces help concentration'),
('The Nature Walk','Cole','nature trail','a checklist','identify safe things to observe','a completed checklist','careful observation teaches us'),
('The Marble Ramp','Layla','garage','three toy cars','test ramps of different heights','a results table','fair tests change one thing at a time'),
('The Word Garden','Jaden','classroom wall','paper flowers','write new vocabulary on each flower','a word garden','new words grow through practice'),
('The Compass Walk','Mia','school field','a simple compass','follow north, south, east and west clues','a completed route','directions help us navigate'),
('The Healthy Lunch','Eli','kitchen','fruit, bread and yoghurt','plan a balanced lunch','a colourful lunchbox','different foods provide different nutrients'),
('The Tiny Theatre','Ari','classroom','paper puppets','write and perform a short scene','a puppet show','reading aloud can build confidence'),
('The Rain Gauge','Zara','garden','a clear measuring cup','measure rainfall after storms','a rain record','weather can be measured'),
('The Code Wheel','Theo','desk','a paper code wheel','decode a friendly message','a secret note','patterns can carry information'),
('The Team Relay','Nolan','sports field','four cones','plan a fair relay','a smooth relay','teamwork and practice matter'),
('The Book Review','Lily','reading corner','a favourite book','write three reasons she liked it','a short review','readers can explain their opinions'),
('The Little Inventor','Owen','workshop table','straws and tape','build a tower that stands by itself','a tall tower','testing helps improve designs'),
('The Night Sky Club','Maya','school roof area','a star chart','compare visible stars on two nights','a shared observation page','careful notes help scientists'),
]
af=[
('Die Saadprojek','Mia','skooltuin','drie sonneblomsaadjies','hul groei meet','’n grafiek','’n klein wetenskapprojek'),
('Die Verlore Boekmerk','Liam','biblioteek','’n blou boekmerk','die bibliotekaris vra','’n boekrak','’n nuwe boek om te ontdek'),
('Die Reënren','Ava','park','’n papierbootjie','kyk watter bootjie die verste vaar','’n plas water','’n les oor water'),
('Die Sonoond','Noah','agtertuin','’n kartondoos','toets hoe sonlig dit warm maak','’n eenvoudige oond','’n warm happie'),
('Die Goedheidsfles','Zoe','klaskamer','’n glasfles','goeie dade neerskryf','’n fles vol briefies','dat goedheid kan groei'),
('Die Kaartgeheim','Ethan','gemeenskapsentrum','’n handgetekende kaart','drie leidrade volg','’n leeshoekie','’n boodskap oor spanwerk'),
('Die Voëlkyk','Ella','skoolterrein','’n notaboek','voëls waarneem sonder om hulle te pla','’n stil kykplek','nuwe feite oor plaaslike voëls'),
('Die Getalwinkel','Jayden','voorraadwinkel','tien papiermunte','totale en kleingeld bereken','’n wiskundespeletjie','’n sterker wiskundevaardigheid'),
('Die Herwinningspan','Amara','skoolplaas','drie gemerkte dromme','skoon items sorteer','’n herwinningstasie','’n skoner skool'),
('Die Maanjoernaal','Kai','slaapkamervenster','’n maanjoernaal','elke aand die maan teken','’n reeks sketse','patrone in die naghemel'),
('Die Brugbouers','Sofia','klaskamer','papier en handwerkstokkies','verskillende ontwerpe toets','’n sterk papierbrug','dat foute idees kan verbeter'),
('Die Storiepiekniek','Ben','park','twee storieboeke','om die beurt hardop lees','’n skaduryke boom','’n gunstelingstorie'),
('Die Weerkykers','Lara','skoolstoep','’n termometer','temperatuur en wolke aanteken','’n weergrafiek','hoe weer verander'),
('Die Geheime Bestanddeel','Daniel','kombuis','’n resepkaart','bestanddele versigtig meet','’n vrugteslaai','waarom metings belangrik is'),
('Die Fietsieklokkie','Mila','buurt','’n los fietsieklokkie','dit veilig nagaan en vasmaak','’n werkende klokkie','dat klein herstelwerk sorg nodig het'),
('Die Oseaanplakkaat','Sam','klaskamer','blou papier en tekeninge','feite oor oseane rangskik','’n kleurvolle plakkaat','nuwe oseaanfeite'),
('Die Legkaartkissie','Leah','studietafel','’n houtlegkaartkissie','getalleleidrade oplos','’n versteekte nota','dat geduld help om probleme op te los'),
('Die Tuinbesoeker','Theo','groentetuin','’n klein groen padda','dit rustig dophou','’n veilige plek onder ’n blaar','respek vir lewende dinge'),
('Die Leesuitdaging','Nia','leeskamer by die huis','’n leesspoor','vir vyftien minute lees','’n voltooide spoor','dat daaglikse lees selfvertroue bou'),
('Die Windeksperiment','Luke','speelgrond','’n windmeul','dit in stil en winderige plekke vergelyk','’n draaiende windmeul','dat wind voorwerpe kan beweeg'),
('Die Klasmuseum','Ruby','klaskamer','ou poskaarte','dit etiketteer en rangskik','’n klein museum','dat geskiedenis interessant kan wees'),
('Die Behulpsame Robot','Oliver','motorhuis','kartonwiele','’n robot ontwerp om blokke te dra','’n werkende model','dat beplanning help voor jy bou'),
('Die Saailingredding','Grace','kweekhuis','’n hangende saailing','water en sonlig nagaan','’n gesonder plant','dat plante die regte sorg nodig het'),
('Die Skaduklok','Caleb','skoolveld','’n stok en kryt','die skaduwee op verskillende tye merk','’n eenvoudige skaduklok','dat die son deur die dag van posisie lyk te verander'),
('Die Woorddetektief','Isla','leeskamer','’n woordeboek','betekenisse van moeilike woorde vind','’n woordelys','dat konteks woorde kan verduidelik'),
('Die Musiekpatroon','Adam','musiekkamer','’n klein drom','’n ritme naboots en ’n nuwe een maak','’n kort ritme','dat patrone in musiek voorkom'),
('Die Veilige Oorgang','Emma','straathoek','’n helder veiligheidskaart','veilige oorgangstappe oefen','’n veilige plan','om te kyk, luister en dink voor jy oorsteek'),
('Die Piekniekbegroting','Finn','kombuistafel','’n klein begroting','happies kies sonder om te veel te spandeer','’n pieknieklys','dat beplanning geld help bestuur'),
('Die Bergmodel','Chloe','wetenskaptafel','klei en karton','’n bergmodel bou','’n model met gemerkte dele','dat landvorme verskillende vorms het'),
('Die Biblioteekhelper','Leo','biblioteek','’n trollie boeke','boeke volgens onderwerp sorteer','’n netjiese rak','dat etikette boeke makliker vindbaar maak'),
('Die Skoonwatertoets','Aria','wetenskapklub','twee helder koppies','skoon en modderige water vergelyk','’n eenvoudige waarnemingsblad','dat watergehalte belangrik is'),
('Die Vriendskapsvlag','Max','klaskamer','gekleurde papier','saam ’n vlag ontwerp','’n klasvlag','dat luister groepe help saamwerk'),
('Die Mini Plaas','Poppy','agterplaas','klein potte en grond','kruie plant en etiketteer','’n mini-kruietuin','dat plante in klein ruimtes kan groei'),
('Die Verkeersligspeletjie','Ryan','oprit','rooi, geel en groen kaarte','veilige padbesluite oefen','’n veiligheidsspeletjie','dat kleure aksies kan aandui'),
('Die Sterresamelaar','Mason','slaapkamer','’n sterkaart','sterre verdien vir leesoefening','’n vol kaart','dat klein doelwitte ’n gewoonte kan bou'),
('Die Breukpizza','Hannah','klaskamer','’n papierpizza','dit in gelyke dele verdeel','’n breukpizza','dat breuke gelyke dele beskryf'),
('Die Herwinningsrobot','Aiden','skoolsaal','skoon bokse en bottels','’n robot uit herbruikbare items bou','’n herwinningsrobot','dat ou materiale nuwe gebruike kan kry'),
('Die Stil Biblioteek','Sienna','biblioteek','’n fluisterkaart','besoekers help om sag te praat','’n rustige leesplek','dat stil ruimtes konsentrasie help'),
('Die Natuurstap','Cole','natuurroete','’n kontrolelys','veilige dinge identifiseer om waar te neem','’n voltooide lys','dat versigtige waarneming ons leer'),
('Die Albasterhelling','Layla','motorhuis','drie speelgoedmotors','hellings van verskillende hoogtes toets','’n resultate-tabel','dat ’n billike toets een ding op ’n slag verander'),
('Die Woordtuin','Jaden','klaskamermuur','papierblomme','nuwe woordeskat op elke blom skryf','’n woordtuin','dat nuwe woorde deur oefening groei'),
('Die Kompasstap','Mia','skoolveld','’n eenvoudige kompas','noord, suid, oos en wes leidrade volg','’n voltooide roete','dat rigtings ons help navigeer'),
('Die Gesonde Middagete','Eli','kombuis','vrugte, brood en jogurt','’n gebalanseerde middagete beplan','’n kleurvolle kosblik','dat verskillende kosse verskillende voedingstowwe gee'),
('Die Klein Teater','Ari','klaskamer','papierpoppe','’n kort toneel skryf en opvoer','’n poppeteater','dat hardop lees selfvertroue kan bou'),
('Die Reënmeter','Zara','tuin','’n helder maatbeker','reënval ná storms meet','’n reënrekord','dat weer gemeet kan word'),
('Die Kodewiel','Theo','lessenaar','’n papierkodewiel','’n vriendelike boodskap ontsyfer','’n geheime nota','dat patrone inligting kan dra'),
('Die Span-aflos','Nolan','sportveld','vier keëls','’n billike aflos beplan','’n gladde aflos','dat spanwerk en oefening belangrik is'),
('Die Boekresensie','Lily','leeskamer','’n gunstelingboek','drie redes skryf waarom sy daarvan hou','’n kort resensie','dat lesers hul menings kan verduidelik'),
('Die Klein Uitvinder','Owen','werksbank','strooitjies en kleefband','’n toring bou wat self staan','’n hoë toring','dat toetsing ontwerpe verbeter'),
('Die Naghemelklub','Maya','skool se dakarea','’n sterkaart','sigbare sterre op twee aande vergelyk','’n gedeelde waarnemingsblad','dat noukeurige notas wetenskaplikes help'),
]
assert len(pairs)==50 and len(af)==50

def eng_story(t):
 title,name,place,obj,action,found,lesson=t
 text=f"{name} went to the {place}. There, {name} found {obj}. {name} decided to {action}. After a little careful work, {name} had {found}. At the end, {name} learned {lesson}."
 qs=[
 [f"Where did {name} go?",[place.title(),'A cinema','A stadium'],0],
 [f"What did {name} find?",[obj.capitalize(),'A sandwich','A toy'],0],
 [f"What did {name} learn?",[lesson.capitalize(),'That practice is useless','That questions are bad'],0]
 ]
 return {'lang':'English','title':title,'text':text,'qs':qs}

def af_story(t):
 title,name,place,obj,action,found,lesson=t
 text=f"{name} het na die {place} gegaan. Daar het {name} {obj} gevind. {name} besluit om te {action}. Ná ’n bietjie versigtige werk het {name} {found} gehad. Aan die einde het {name} geleer {lesson}."
 qs=[
 [f"Waarheen het {name} gegaan?",[place.capitalize(),'’n Bioskoop','’n Stadion'],0],
 [f"Wat het {name} gevind?",[obj.capitalize(),'’n Toebroodjie','’n Speelding'],0],
 [f"Wat het {name} geleer?",[lesson.capitalize(),'Dat oefening nutteloos is','Dat vrae sleg is'],0]
 ]
 return {'lang':'Afrikaans','title':title,'text':text,'qs':qs}

stories=[]
for e,a in zip(pairs,af):
    stories.append(eng_story(e)); stories.append(af_story(a))
print(len(stories))
js='const STORIES='+json.dumps(stories,ensure_ascii=False,separators=(',',':'))+';\n'
open('/mnt/data/wa_new/stories100.js','w',encoding='utf8').write(js)
