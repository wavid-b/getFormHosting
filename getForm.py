
import pandas as pd
import os

def get_id_greek(word):
    lemmaDF = pd.read_csv("Dictionary_Dataframes/greek_words.csv", sep = "\t")
    del lemmaDF['Unnamed: 0']
    #search the lemmaDF for the word
    word = word.lower()
    output = []
    #this is the dataframe of all rows with the word
    df = lemmaDF.loc[lemmaDF["bare_text"] == word]
        #iterrows works, but the others dont. ok whatever
    for index, row in df.iterrows():
        if(row["id"] not in output):
            output.append(row["id"])
    return(output)

def get_POS_greek(id):
    #returns the part of speech of the word
    lemmaDF = pd.read_csv("Dictionary_Dataframes/greek_words.csv", sep = "\t")
    del lemmaDF['Unnamed: 0']
    output = []
    df = lemmaDF.loc[lemmaDF["id"] == id]
    for(index, row) in df.iterrows():
        out = row["morph_code"][0]
        if out not in output:
            output.append(out)
    return output
def get_greek_form(word = "NULL", id = "NULL", case = "NULL",
              number = "NULL", gender = "NULL", mood = "NULL", 
              person = "NULL", tense = "NULL", voice = "NULL",
                degree = "NULL", wanted_pos = "NULL"):
    #check if word is null - use ID in that case
    lemmaDF = pd.read_csv("Dictionary_Dataframes/greek_words.csv", sep = "\t")
    del lemmaDF['Unnamed: 0']
    if(word == "NULL" and id == "NULL"):
        print("Please enter a word or an ID")
        return "ERROR: Please enter a word or an ID"
    if(word!= "NULL" and id !="NULL"):
            print("Please enter a word or an ID, not both")
            return "ERROR: Please enter a word or an ID, not both"
    if(word != "NULL"):
        word = word.lower()
        word = word.strip()

        ids = get_id_greek(word)
        if(len(ids) == 0):
            print("No matching words found")
            return "ERROR: No matching words"
    if(id != "NULL"):
        ids = [id]
    for id in ids:
        #if you find a valid output in one id, you're good. If not, we continue on 
        output = ""
        posTag = "---------"
        pos = get_POS_greek(id)
        #if the word is a noun
        if("n" in pos):
            #noun 
            #case
            if (case == "nominative"):
                case = "n"
            if (case == "genative"):
                case = "g"
            if (case == "dative"):
                case = "d"
            if (case == "accusative"):
                case = "a"
            if (case == "ablative"):
                case = "b"
            if (case == "locative"):
                case = "l"
            if (case == "vocative"):
                case = "v" 
            
            #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
            
            #gender 
            if(gender == "masculine"):
                gender = "m"
            if (gender == "feminine"):
                gender = "f"
            if (gender == "neuter"):
                gender = "n"
           
            #word assigned to output if it exists
            if (case != "NULL"):
                # include case in search
                posTag = posTag[:7] + case + posTag[8:]
            # number
            if (number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
            # gender 
            if(gender != "NULL"):
                posTag = posTag[:6] + gender + posTag[7:]
        if("v" in pos):
            #verb
                #mood
            if(mood == "indicative"):
                mood = "i"
            if(mood == "subjunctive"):
                mood = "s"
            if(mood == "imperative"):
                mood = "m"
            if(mood == "infinitive"):
                mood = "n"
            if(mood == "participle"):
                mood = "p"
            if(mood == "gerund"):
                mood = "d"
            if(mood == "gerundive"):
                mood = "g"
            
                #person
            if(person == "first"):
                person = "1"
            if(person == "second"):
                person = "2"
            if(person == "third"):
                person = "3"
            
                #tense
            if(tense == "present"):
                tense = "p"
            if(tense == "imperfect"):
                tense = "i"
            if(tense == "perfect"):
                tense = "r"
            if(tense == "pluperfect"):
                tense = "l"
            if(tense == "future perfect"):
                tense = "t"
            if(tense == "future"):
                tense = "f"
            
                #voice
            if(voice == "active"):
                voice = "a"
            if(voice == "passive"):
                voice = "p"
            if(voice == "deponent"):
                voice = "d"
            
                #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
                # mood
            if(mood != "NULL"):
                posTag = posTag[:4] + mood + posTag[5:]
            # person
            if(person != "NULL"):
                posTag = posTag[:1] + person + posTag[2:]
            # tense
            if(tense != "NULL"):
                posTag = posTag[:3] + tense + posTag[4:]
            # voice
            if(voice != "NULL"):
                posTag = posTag[:5] + voice + posTag[6:]
            # number
            if(number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
        if("a" in pos):
                #adj case

            #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
            if(number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
            #gender 
            if(gender == "masculine"):
                gender = "m"
            if (gender == "feminine"):
                gender = "f"
            if (gender == "neuter"):
                gender = "n"
            if(gender != "NULL"):
                posTag = posTag[:6] + gender + posTag[7:]
            #degree
            if(degree == "positive"):
                degree = "p"
            if(degree == "comparative"):
                degree = "c"
            if(degree == "superlative"):
                degree = "s"
            if(degree != "NULL"):
                posTag = posTag[:8] + gender
        #set the pos to the wanted pos if it exists
        #change full words to their specific letters
        if(wanted_pos == "noun"):
            wanted_pos = "n"
        if(wanted_pos == "verb"):
            wanted_pos = "v"
        if(wanted_pos == "adjective"):
            wanted_pos = "a"
        if(wanted_pos == "adverb"):
            wanted_pos = "d"
        if(wanted_pos == "conjunction"):
            wanted_pos = "c"
        if(wanted_pos == "pronoun"):
            wanted_pos = "p"
        if(wanted_pos == "numeral"):
            wanted_pos = "m"
        if(wanted_pos == "interjection"):
            wanted_pos = "i"
        if(wanted_pos == "exclaimation"):
            wanted_pos = "e"
        if(wanted_pos == "punctuation"):
            wanted_pos = "u"
        #if the wanted pos is not null, change the posTag to match
        if(wanted_pos != "NULL"):
            posTag = wanted_pos + posTag[1:]
        #now actually find that word in parses 
        df = lemmaDF.loc[lemmaDF["id"] == id]
        for index, row in df.iterrows():
            fits = True
            if(wanted_pos == "v"):
                if(row["morph_code"][0] == "v" or row["morph_code"][0] == "t"):
                    fits = True
                else:
                    fits = False
                for i in range(1, 8):
                    char = posTag[i]
                    if(char != "-"):
                        #morph code is wrong or output is longer than old output or it has misc_features or alt dialect
                        if(row["morph_code"][i] != char or (output != "" and len(output)<len(row["bare_text"]))):
                            fits = False
                        #this is the case that we disclude it from results
            
            else:
                for i in range(8):
                    char = posTag[i]
                    if(char != "-"):
                        #morph code is wrong or output is longer than old output or it has misc_features or alt dialect
                        if(row["morph_code"][i] != char or (output != "" and len(output)<len(row["bare_text"]))):
                            fits = False
                        #this is the case that we disclude it from results
            if fits:
                output = row["bare_text"]

        #before repeating for other ids, return the output if it exists
        if(output != ""):
            return output
        
    return "ERROR: Nothing found with those parameters"
def get_def_greek(id):
    #returns the definition of the word
    lemmaDF = pd.read_csv("Dictionary_Dataframes/greek_words.csv", sep = "\t")
    del lemmaDF['Unnamed: 0']
    out = ""
    df = lemmaDF.loc[lemmaDF["id"] == id]
    for(index, row) in df.iterrows():
        if(len(row["definition"])>len(out)):
            #longest definition is the one we want (?)
            out = row["definition"]
    return out
def get_dict_greek(word, show_def = False):
    ids = get_id_greek(word)
        #list of dictionary entries 
    parsesDF = pd.read_csv("Dictionary_Dataframes/greek_words.csv", sep = "\t")
    del parsesDF['Unnamed: 0']

    output = {}
    for id in ids:
        pos = "" 
        dictEntry = ""
        rowText = ""
        morph = ""
        text = {}
        definition = get_def_latin(id)
        df = parsesDF.loc[parsesDF["id"] == id]
        for i in range(10):
            if(not i in text):
                text[i] = "NULL"
        for index, row in df.iterrows():
            #preset text to be all null
            rowText = row["bare_text"]
            morph = row["morph_code"]
            #noun case
                #check required to prevent substantive adj from outputting as nouns 
            if (row["morph_code"][0] == "n" and (pos == "" or pos == "noun")):
                pos = "noun"
                text[2] = row["morph_code"][6] 
                #make the nom, singular --> text[0]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "n")):
                    #have to hard-code around que enclitic 
                    if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):

                        text[0] = row["bare_text"]
                #make the gen, singular --> text[1]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "g")):
                    if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                        text[1] = row["bare_text"]
            
            #adj case 
            if (row["morph_code"][0] == "a"):
                pos = "adj"
                #for each, need the singular, positive, nominative - without enclitics
                if(type(row["misc_features"]) == type(1.0) ):
                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "m")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]
                    
                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "f")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                            text[1] = row["bare_text"]

                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "n")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[2] == "NULL" or len(row["bare_text"])<len(text[2])):
                            text[2] = row["bare_text"]
            #verb case - need t morph code for the 4PP
            if(row["morph_code"] == "t-sr-pmn-") and (text[3] == "NULL" or len(row["bare_text"])<len(text[3])):
                text[3] = row["bare_text"] 
            #backup 4th PP for verbs stored in text[6]
            if(row["morph_code"] == "t-sf-amn-") and (text[6] == "NULL" or len(row["bare_text"])<len(text[6])):
                text[6] = row["bare_text"] 
            if((row["morph_code"][0] == "v")): 
                pos = "verb"
                kind = "regular"
                morph = row["morph_code"]
                curWord = row["bare_text"]
                #make 3 cases: regular, deponent, and inpersonal - may be more ask Celano
                #0: present first person singular active indicative: v1spia---
                #1: present active infinitive: v--pna---
                #2: perfect first person singular active indicative: v1sria---
                #3: t-sr-pmn- is the morph code --> has 3PP if deponent 
                #4: present third person singular active indicative - for impersonal verbs
                #5: grab stuff with deponent voice tag v1spip---
                if(type(row["misc_features"]) == type(1.0)):
                    if(morph) == "v1spia---":
                        if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]                    
                    if(morph) == "v--pna---":
                        if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                            text[1] = row["bare_text"]
                    if(morph) == "v1sria---":
                        if(text[2] == "NULL" or len(row["bare_text"])<len(text[2])):
                            text[2] = row["bare_text"]
                    if(morph) == "v3spia---":
                        if(text[4] == "NULL" or len(row["bare_text"])<len(text[4])):
                            text[4] = row["bare_text"]
                    if(morph) == "v1spip---":
                        if(text[5] == "NULL" or len(row["bare_text"])<len(text[5])):
                            text[5] = row["bare_text"]                    
            #all other cases
            if(morph[0] == "d"):
                pos = "adv"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]
            if(morph[0] == "c"):
                pos = "conj"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                     text[0] = row["bare_text"]
            if(morph[0] == "r"):
                pos = "adpostion"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "p"):
                pos = "pronoun"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "m"):
                pos = "numeral"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "i"):
                pos = "interjection"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "e" ):
                pos = "exclaimation"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "u"):
                pos = "punctuation"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
        #preventing errors <3 
        if(type(definition) != type("str") or len(definition) == 0):
            definition = "No Definiton"
            #case for when FPP isn't found in parses
        if(text[0] == "NULL"):
            #needs to be getFPP
            df2 = lemmaDF.loc[lemmaDF["id"] == id]
            for index, row in df2.iterrows():
                text[0] = row["bare_text"]
        #make dictionary entry string
        match(pos):
            #make sure each of those exists before trying to output
            case "noun":
                if(show_def):
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + ". - " + (definition)
                else:
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] 
            case "adj":
                if(show_def):
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + " - " + definition
                else:
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] 
            case "verb":
                #change which type by checking if we have a normal FPP
                if(text[0]!= "NULL"):
                    kind = "regular"
                elif(text[5] != "NULL"):
                    kind = "deponent"
                else:
                    kind = "impersonal"
                    #nested switch block! Yay!
                #solve the edge case! 
                if(text[3] == "NULL"):
                    text[3] = text[6]
                match(kind):
                    case "regular":
                        if(show_def):
                            dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[0] + ", " + text[1] + ", "+ text[2] + ", " + text[3]
                    case "deponent":
                        if(show_def):
                            dictEntry = pos + ": " + text[5] + ", " + text[1] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[5] + ", " + text[1] + ", " + text[3]
                    case "impersonal":
                        if(show_def):
                            dictEntry = pos + ": " + text[4] + ", " + text[1] +", " + text[2] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[4] + ", " + text[1] +", " + text[2]+  ", "+ text[3]
            case other:
                dictEntry = pos + ": " + text[0]
                if(show_def):
                    dictEntry += " " + definition 
        output[id] = (dictEntry)
    return output

def get_id_parse_latin(word, input):
    parsesDF = pd.read_csv("Dictionary_Dataframes/parses.csv", sep = "{")
    del parsesDF["Unnamed: 0"]
    #search parseDF for instances and add to output if it isn't already in there
    output = input
    df = parsesDF.loc[parsesDF["bare_text"] == word]
    for index, row in df.iterrows():
        id = row["id"]
        if id not in output:
            output.append(id)
    return output
def get_id_latin(word):
    #search the lemmaDF for the word
    lemmaDF = pd.read_csv("Dictionary_Dataframes/lemmas.csv", sep = "{")
    del lemmaDF['Unnamed: 0']
    output = []
    #this is the dataframe of all rows with the word
    df = lemmaDF.loc[lemmaDF["bare_text"] == word]
        #iterrows works, but the others dont. ok whatever   
    for index, row in df.iterrows():
        if(row["id"] not in output):
            output.append(row["id"])
    return(output) 
def get_id_full_latin(word):
    ids = get_id_latin(word)
    ids = get_id_parse_latin(word, ids)
    return ids
def get_POS_latin(id):
     #returns the part of speech of the word
    parsesDF = pd.read_csv("Dictionary_Dataframes/parses.csv", sep = "{")
    del parsesDF["Unnamed: 0"]
    output = []
    df = parsesDF.loc[parsesDF["id"] == id]
    for(index, row) in df.iterrows():
        out = row["morph_code"][0]
        if out not in output:
            output.append(out)
    return output
def get_latin_form(word = "NULL", id = "NULL", case = "NULL",
              number = "NULL", gender = "NULL", mood = "NULL", 
              person = "NULL", tense = "NULL", voice = "NULL",
                degree = "NULL", alt_dialects = False, wanted_pos = "NULL"):
    
    parsesDF = pd.read_csv("Dictionary_Dataframes/parses.csv", sep = "{")
    del parsesDF["Unnamed: 0"]
    #check if word is null - use ID in that case
    if(word == "NULL" and id == "NULL"):
        print("Please enter a word or an ID")
        return "ERROR: Please enter a word or an ID"
    if(word!= "NULL" and id !="NULL"):
            print("Please enter a word or an ID, not both")
            return "ERROR: Please enter a word or an ID, not both"
    if(word != "NULL"):
        word = word.lower()
        word = word.strip()
        ids = get_id_full_latin(word)
        if(len(ids) == 0):
            print("No matching words found")
            return "ERROR: No matching words"
    if(id != "NULL"):
        ids = [id]
    for id in ids:
        #if you find a valid output in one id, you're good. If not, we continue on 
        output = ""
        posTag = "---------"
        pos = get_POS_latin(id)
        #if the word is a noun
        if("n" in pos):
            #noun 
            #case
            if (case == "nominative"):
                case = "n"
            if (case == "genative"):
                case = "g"
            if (case == "dative"):
                case = "d"
            if (case == "accusative"):
                case = "a"
            if (case == "ablative"):
                case = "b"
            if (case == "locative"):
                case = "l"
            if (case == "vocative"):
                case = "v" 
            
            #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
            
            #gender 
            if(gender == "masculine"):
                gender = "m"
            if (gender == "feminine"):
                gender = "f"
            if (gender == "neuter"):
                gender = "n"
           
            #word assigned to output if it exists
            if (case != "NULL"):
                # include case in search
                posTag = posTag[:7] + case + posTag[8:]
            # number
            if (number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
            # gender 
            if(gender != "NULL"):
                posTag = posTag[:6] + gender + posTag[7:]
        if("v" in pos):
            #verb
                #mood
            if(mood == "indicative"):
                mood = "i"
            if(mood == "subjunctive"):
                mood = "s"
            if(mood == "imperative"):
                mood = "m"
            if(mood == "infinitive"):
                mood = "n"
            if(mood == "participle"):
                mood = "p"
            if(mood == "gerund"):
                mood = "d"
            if(mood == "gerundive"):
                mood = "g"
            
                #person
            if(person == "first"):
                person = "1"
            if(person == "second"):
                person = "2"
            if(person == "third"):
                person = "3"
            
                #tense
            if(tense == "present"):
                tense = "p"
            if(tense == "imperfect"):
                tense = "i"
            if(tense == "perfect"):
                tense = "r"
            if(tense == "pluperfect"):
                tense = "l"
            if(tense == "future perfect"):
                tense = "t"
            if(tense == "future"):
                tense = "f"
            
                #voice
            if(voice == "active"):
                voice = "a"
            if(voice == "passive"):
                voice = "p"
            if(voice == "deponent"):
                voice = "d"
            
                #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
                # mood
            if(mood != "NULL"):
                posTag = posTag[:4] + mood + posTag[5:]
            # person
            if(person != "NULL"):
                posTag = posTag[:1] + person + posTag[2:]
            # tense
            if(tense != "NULL"):
                posTag = posTag[:3] + tense + posTag[4:]
            # voice
            if(voice != "NULL"):
                posTag = posTag[:5] + voice + posTag[6:]
            # number
            if(number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
        if("a" in pos):
                #adj case
            #case
            if (case == "nominative"):
                case = "n"
            if (case == "genative"):
                case = "g"
            if (case == "dative"):
                case = "d"
            if (case == "accusative"):
                case = "a"
            if (case == "ablative"):
                case = "b"
            if (case == "locative"):
                case = "l"
            if (case == "vocative"):
                case = "v" 
            if (case != "NULL"):
                # include case in search
                posTag = posTag[:7] + case + posTag[8:]
            #number
            if (number == "singular"):
                number = "s"
            if (number == "plural"):
                number = "p"
            if(number != "NULL"):
                posTag = posTag[:2] + number + posTag[3:]
            #gender 
            if(gender == "masculine"):
                gender = "m"
            if (gender == "feminine"):
                gender = "f"
            if (gender == "neuter"):
                gender = "n"
            if(gender != "NULL"):
                posTag = posTag[:6] + gender + posTag[7:]
            #degree
            if(degree == "positive"):
                degree = "p"
            if(degree == "comparative"):
                degree = "c"
            if(degree == "superlative"):
                degree = "s"
            if(degree != "NULL"):
                posTag = posTag[:8] + gender
        #set the pos to the wanted pos if it exists
        #change full words to their specific letters
        if(wanted_pos == "noun"):
            wanted_pos = "n"
        if(wanted_pos == "verb"):
            wanted_pos = "v"
        if(wanted_pos == "adjective"):
            wanted_pos = "a"
        if(wanted_pos == "adverb"):
            wanted_pos = "d"
        if(wanted_pos == "conjunction"):
            wanted_pos = "c"
        if(wanted_pos == "pronoun"):
            wanted_pos = "p"
        if(wanted_pos == "numeral"):
            wanted_pos = "m"
        if(wanted_pos == "interjection"):
            wanted_pos = "i"
        if(wanted_pos == "exclaimation"):
            wanted_pos = "e"
        if(wanted_pos == "punctuation"):
            wanted_pos = "u"
        #if the wanted pos is not null, change the posTag to match
        if(wanted_pos != "NULL"):
            posTag = wanted_pos + posTag[1:]
        #now actually find that word in parses 
        df = parsesDF.loc[parsesDF["id"] == id]
        for index, row in df.iterrows():
            fits = True
            if(wanted_pos == "v"):
                if(row["morph_code"][0] == "v" or row["morph_code"][0] == "t"):
                    fits = True
                else:
                    fits = False
                for i in range(1, 8):
                    if(not alt_dialects):
                        if(type(row["misc_features"]) != type(1.0) or type(row["dialects"]) != type(1.0)):
                            fits = False
                    char = posTag[i]
                    if(char != "-"):
                        #morph code is wrong or output is longer than old output or it has misc_features or alt dialect
                        if(row["morph_code"][i] != char or (output != "" and len(output)<len(row["bare_text"]))):
                            fits = False
            else:
                for i in range(8):
                    #check if alt dialects allowed
                    if(not alt_dialects):
                        if(type(row["misc_features"]) != type(1.0) or type(row["dialects"]) != type(1.0)):
                            fits = False
                    char = posTag[i]
                    if(char != "-"):
                        #morph code is wrong or output is longer than old output or it has misc_features or alt dialect
                        if(row["morph_code"][i] != char or (output != "" and len(output)<len(row["bare_text"]))):
                            fits = False
                        #this is the case that we disclude it from results
            if fits:
                output = row["bare_text"]

        #before repeating for other ids, return the output if it exists
        if(output != ""):
            #change to i
            output = output.replace("j", "i")
            return output
    if(not alt_dialects):
        output = get_latin_form(word="NULL", id=id, case=case, voice=voice,
                                 number=number, gender=gender, degree=degree,
                                   wanted_pos=wanted_pos, alt_dialects=True)
    else:
        output = "ERROR: Nothing found with those parameters"
    return output
    
def get_def_latin(id):
    lemmaDF = pd.read_csv("Dictionary_Dataframes/lemmas.csv", sep = "{")
    output = ""
    df = lemmaDF.loc[lemmaDF["id"] == id]
    for index, row in df.iterrows():
        output = (row["definition"])
    return output
def get_dict_latin(word, show_def = False):
    parsesDF = pd.read_csv("Dictionary_Dataframes/parses.csv", sep = "{")
    lemmaDF = pd.read_csv("Dictionary_Dataframes/lemmas.csv", sep = "{")
    ids = get_id_full_latin(word)
        #list of dictionary entries 
    output = {}
    for id in ids:
        pos = "" 
        dictEntry = ""
        rowText = ""
        morph = ""
        text = {}
        definition = get_def_latin(id)
        df = parsesDF.loc[parsesDF["id"] == id]
        for i in range(10):
                if(not i in text):
                    text[i] = "NULL"
        for index, row in df.iterrows():
            #preset text to be all null
            rowText = row["bare_text"]
            morph = row["morph_code"]
            #noun case
                #check required to prevent substantive adj from outputting as nouns 
            if (row["morph_code"][0] == "n" and (pos == "" or pos == "noun")):
                pos = "noun"
                text[2] = row["morph_code"][6] 
                #make the nom, singular --> text[0]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "n")):
                    #have to hard-code around que enclitic 
                    if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):

                        text[0] = row["bare_text"]
                #make the gen, singular --> text[1]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "g")):
                    if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                        text[1] = row["bare_text"]
            
            #adj case 
            if (row["morph_code"][0] == "a"):
                pos = "adj"
                #for each, need the singular, positive, nominative - without enclitics
                if(type(row["misc_features"]) == type(1.0) ):
                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "m")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]
                    
                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "f")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                            text[1] = row["bare_text"]

                    if((row["morph_code"][2] == "s")
                    and (row["morph_code"][7] == "n") 
                    and (row["morph_code"][6] == "n")
                    and (row["morph_code"][8] == "p" or row["morph_code"][8] == "-")):
                        if(text[2] == "NULL" or len(row["bare_text"])<len(text[2])):
                            text[2] = row["bare_text"]
            #verb case - need t morph code for the 4PP
            if(row["morph_code"] == "t-sr-pmn-") and (text[3] == "NULL" or len(row["bare_text"])<len(text[3])):
                text[3] = row["bare_text"] 
            #backup 4th PP for verbs stored in text[6]
            if(row["morph_code"] == "t-sf-amn-") and (text[6] == "NULL" or len(row["bare_text"])<len(text[6])):
                text[6] = row["bare_text"] 
            if((row["morph_code"][0] == "v")): 
                pos = "verb"
                kind = "regular"
                morph = row["morph_code"]
                curWord = row["bare_text"]
                #make 3 cases: regular, deponent, and inpersonal - may be more ask Celano
                #0: present first person singular active indicative: v1spia---
                #1: present active infinitive: v--pna---
                #2: perfect first person singular active indicative: v1sria---
                #3: t-sr-pmn- is the morph code --> has 3PP if deponent 
                #4: present third person singular active indicative - for impersonal verbs
                #5: grab stuff with deponent voice tag v1spip---
                if(type(row["misc_features"]) == type(1.0)):
                    if(morph) == "v1spia---":
                        if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]                    
                    if(morph) == "v--pna---":
                        if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                            text[1] = row["bare_text"]
                    if(morph) == "v1sria---":
                        if(text[2] == "NULL" or len(row["bare_text"])<len(text[2])):
                            text[2] = row["bare_text"]
                    if(morph) == "v3spia---":
                        if(text[4] == "NULL" or len(row["bare_text"])<len(text[4])):
                            text[4] = row["bare_text"]
                    if(morph) == "v1spip---":
                        if(text[5] == "NULL" or len(row["bare_text"])<len(text[5])):
                            text[5] = row["bare_text"]                    
            #all other cases
            if(morph[0] == "d"):
                pos = "adv"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                            text[0] = row["bare_text"]
            if(morph[0] == "c"):
                pos = "conj"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                     text[0] = row["bare_text"]
            if(morph[0] == "r"):
                pos = "adpostion"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "p"):
                pos = "pronoun"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "m"):
                pos = "numeral"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "i"):
                pos = "interjection"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "e" ):
                pos = "exclaimation"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
            if(morph[0] == "u"):
                pos = "punctuation"
                if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                    text[0] = row["bare_text"]
        #preventing errors <3 
        if(type(definition) != type("str") or len(definition) == 0):
            definition = "No Definiton"
            #case for when FPP isn't found in parses
        if(text[0] == "NULL"):
            df2 = lemmaDF.loc[lemmaDF["id"] == id]
            for index, row in df2.iterrows():
                text[0] = row["bare_text"]
        #make dictionary entry string
        match(pos):
            #make sure each of those exists before trying to output
            case "noun":
                if(show_def):
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + ". - " + (definition)
                else:
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] 
            case "adj":
                if(show_def):
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + " - " + definition
                else:
                    dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] 
            case "verb":
                #change which type by checking if we have a normal FPP
                if(text[0]!= "NULL"):
                    kind = "regular"
                elif(text[5] != "NULL"):
                    kind = "deponent"
                else:
                    kind = "impersonal"
                    #nested switch block! Yay!
                #solve the edge case! 
                if(text[3] == "NULL"):
                    text[3] = text[6]
                match(kind):
                    case "regular":
                        if(show_def):
                            dictEntry = pos + ": " + text[0] + ", " + text[1] + ", " + text[2] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[0] + ", " + text[1] + ", "+ text[2] + ", " + text[3]
                    case "deponent":
                        if(show_def):
                            dictEntry = pos + ": " + text[5] + ", " + text[1] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[5] + ", " + text[1] + ", " + text[3]
                    case "impersonal":
                        if(show_def):
                            dictEntry = pos + ": " + text[4] + ", " + text[1] +", " + text[2] + ", " + text[3] + "- " + definition
                        else:
                            dictEntry = pos + ": " + text[4] + ", " + text[1] +", " + text[2]+  ", "+ text[3]
            case other:
                dictEntry = pos + ": " + text[0]
                if(show_def):
                    dictEntry += " " + definition 
        output[id] = (dictEntry)
    return output

if(__name__ == '__main__'):
    #os.chdir("Individual/Leipzig-Research/Lemmatizer-GRK")
    
    print("hello")
    # print(get_greek_form("λεγω", mood = "indicative", tense = "present", voice = "active", person = "third", number = "singular"))
    # print(get_latin_form("mater", gender = "f", number = "p", case = "a"))
    # print(get_latin_form("senex", gender = "m", number = "s", case = "d"))
    print(get_latin_form("pulchra", wanted_pos= "a", case = "a", number = "s", 
                         degree= "p", gender = "f"))
    print(get_latin_form("Romanus", case = "v", number = "p", gender = "m", 
                         wanted_pos = "a", ))
    print(get_latin_form("romanus", case = "v", number = "p", gender = "m", 
                         wanted_pos = "a", ))