
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
            return output
        
    return "ERROR: Nothing found with those parameters"
        

if(__name__ == '__main__'):
    #os.chdir("Individual/Leipzig-Research/Lemmatizer-GRK")
    print(os.getcwd())
    print("hello")
    print(get_greek_form("λεγω", mood = "indicative", tense = "present", voice = "active", person = "third", number = "singular"))
    print(get_latin_form("mater", gender = "f", number = "p", case = "a"))