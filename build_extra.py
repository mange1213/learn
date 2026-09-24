import json, re
from textblob.en import spelling
# Build a large spelling bank from a frequency dictionary, removing obvious proper-name/foreign-word entries.
exclude=set('''pierre natasha andrew rostov moscow mary french american russian german english british alpatych sarcoma'''.split())
# Add a broad list of common first names/place names that frequently appear in corpus dictionaries.
exclude.update('''aaron abby abigail adam alex alexandra alexander alice alicia amanda amy andrea andrew angela anna anne annie anthony arthur ashley austin barbara ben benjamin beth betty billy bob bobby brad brenda brian bridget bruce carl carol caroline carrie catherine charles charlie chris christine christopher claire dan daniel danny dave david debbie deborah dennis derek diana diane donna doug ed edward elizabeth ellen eric erika eva evelyn frank fred george gerald gary glen glenn greg harold harry heather helen henry jack jackie jacob james jamie jane janet janice jason jeff jennifer jeremy jerry jessica jim jimmy joan joe john johnny jonathan joseph josh joshua judy julie justin karen katherine kathy keith kelly kenneth kevin kim laura lauren lawrence linda lisa logan lucas lucy luke marcia margaret maria marie marilyn mark martha martin matthew megan melanie melissa michael michelle mike nancy natalie nathan nicholas nick nicole olivia pamela patricia patrick paul peter philip rachel rebecca richard robert robin roger ronald rose russell ryan sam samantha samuel sandra sarah scott sean sharon simon sophia stephanie stephen steve susan teresa thomas timothy tom tony tracy trevor tyler victoria vincent virginia walter wendy william zachary'''.split())
items=[]
for w,f in spelling.items():
    w=w.lower()
    if w in exclude or not re.fullmatch(r'[a-z]+',w) or not 3<=len(w)<=14 or f<2: continue
    # Exclude obvious technical/medical/corpus noise.
    if any(x in w for x in ['www','http','xxxx']): continue
    items.append((f,w))
items.sort(key=lambda x:(-x[0],x[1]))
words=[]
for _,w in items:
    if w not in words: words.append(w)
    if len(words)==800: break
# If the corpus filter somehow falls short, add a curated fallback list.
if len(words)<800:
    fallback='''apple banana orange pencil school teacher classroom friend family garden water window animal kitten puppy rabbit horse farm river mountain ocean planet rocket rainbow sunshine thunderstorm bicycle football music picture story book library computer tablet keyboard science nature flower tree forest island village city country travel adventure careful clever happy excited important beautiful wonderful because different discover imagine remember practice success question answer sentence language vocabulary spelling reading writing listening speaking morning evening weekend holiday breakfast lunch dinner kitchen bedroom bathroom clothes shoes jacket weather summer winter spring autumn minute hour second calendar today tomorrow yesterday early late first second third fourth fifth sixth seventh eighth ninth tenth hundred thousand addition subtraction multiplication division fraction decimal number pattern shape circle square triangle rectangle angle line point length width height weight money price change coin dollar rand measure metre kilogram litre half quarter equal greater smaller compare solve problem reason explain create build design draw paint sing dance laugh smile learn teach help share choose complete describe explore collect count sort match missing scramble word game challenge level star badge progress'''.split()
    for w in fallback:
        if w not in words: words.append(w)
        if len(words)==800: break
json.dump(words,open('/mnt/data/wa_new/spell800.json','w'),ensure_ascii=False)
print(len(words), words[:20], words[-20:])
