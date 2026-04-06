import pandas as pd

# load data once at module import
PARSES_DF = pd.read_csv("Dictionary_Dataframes/parses.csv", sep="{")
LEMMA_DF = pd.read_csv("Dictionary_Dataframes/lemmas.csv", sep="{")
# remove leftover index columns if present
PARSES_DF = PARSES_DF.drop(columns=[c for c in ["Unnamed: 0"] if c in PARSES_DF.columns], errors='ignore')
LEMMA_DF = LEMMA_DF.drop(columns=[c for c in ["Unnamed: 0"] if c in LEMMA_DF.columns], errors='ignore')

def get_id_parse_latin(word, input_ids):
    # search PARSES_DF for instances and add to input_ids if not already present
    df = PARSES_DF.loc[PARSES_DF["bare_text"] == word]
    for _, row in df.iterrows():
        idv = row["id"]
        if idv not in input_ids:
            input_ids.append(idv)
    return input_ids

def get_id_latin(word):
    # search LEMMA_DF for the word
    df = LEMMA_DF.loc[LEMMA_DF["bare_text"] == word]
    output = []
    for _, row in df.iterrows():
        if row["id"] not in output:
            output.append(row["id"])
    return output

def get_id_full_latin(word):
    ids = get_id_latin(word)
    return get_id_parse_latin(word, ids)

def get_POS_latin(id):
    # returns the part of speech letter(s) for the id
    df = PARSES_DF.loc[PARSES_DF["id"] == id]
    output = []
    for _, row in df.iterrows():
        out = row["morph_code"][0]
        if out not in output:
            output.append(out)
    return output


def get_latin_form(word = "NULL", id = "NULL", case = "NULL",
              number = "NULL", gender = "NULL", mood = "NULL", 
              person = "NULL", tense = "NULL", voice = "NULL",
                degree = "NULL", alt_dialects = False, wanted_pos = "NULL"):
    # check if word is null - use ID in that case
    if(word == "NULL" and id == "NULL"):
        print("Please enter a word or an ID")
        return "ERROR: Please enter a word or an ID"
    if(word!= "NULL" and id !="NULL"):
        print("Please enter a word or an ID, not both")
        return "ERROR: Please enter a word or an ID, not both"
    if(word != "NULL"):
        word = word.lower().strip()
        ids = get_id_full_latin(word)
        if(len(ids) == 0):
            print("No matching words found")
            return "ERROR: No matching words"
    if(id != "NULL"):
        ids = [id]

    for id in ids:
        output = ""
        posTag = "---------"
        pos = get_POS_latin(id)
        # --- noun ---
        if("n" in pos):
            if case == "nominative": case = "n"
            if case == "genative": case = "g"
            if case == "dative": case = "d"
            if case == "accusative": case = "a"
            if case == "ablative": case = "b"
            if case == "locative": case = "l"
            if case == "vocative": case = "v"

            if number == "singular": number = "s"
            if number == "plural": number = "p"

            if gender == "masculine": gender = "m"
            if gender == "feminine": gender = "f"
            if gender == "neuter": gender = "n"

            if case != "NULL":
                posTag = posTag[:7] + case + posTag[8:]
            if number != "NULL":
                posTag = posTag[:2] + number + posTag[3:]
            if gender != "NULL":
                posTag = posTag[:6] + gender + posTag[7:]

        # --- verb ---
        if("v" in pos):
            if mood == "indicative": mood = "i"
            if mood == "subjunctive": mood = "s"
            if mood == "imperative": mood = "m"
            if mood == "infinitive": mood = "n"

            if person == "first": person = "1"
            if person == "second": person = "2"
            if person == "third": person = "3"

            if tense == "present": tense = "p"
            if tense == "imperfect": tense = "i"
            if tense == "perfect": tense = "r"
            if tense == "pluperfect": tense = "l"
            if tense == "future": tense = "f"

            if voice == "active": voice = "a"
            if voice == "passive": voice = "p"

            if number == "singular": number = "s"
            if number == "plural": number = "p"

            if mood != "NULL":
                posTag = posTag[:4] + mood + posTag[5:]
            if person != "NULL":
                posTag = posTag[:1] + person + posTag[2:]
            if tense != "NULL":
                posTag = posTag[:3] + tense + posTag[4:]
            if voice != "NULL":
                posTag = posTag[:5] + voice + posTag[6:]
            if number != "NULL":
                posTag = posTag[:2] + number + posTag[3:]

        # --- adjective ---
        if("a" in pos):
            if case == "nominative": case = "n"
            if case == "genative": case = "g"
            if case == "dative": case = "d"
            if case == "accusative": case = "a"
            if case == "ablative": case = "b"
            if case == "locative": case = "l"
            if case == "vocative": case = "v"
            if case != "NULL":
                posTag = posTag[:7] + case + posTag[8:]
            if number == "singular": number = "s"
            if number == "plural": number = "p"
            if number != "NULL":
                posTag = posTag[:2] + number + posTag[3:]
            if gender == "masculine": gender = "m"
            if gender == "feminine": gender = "f"
            if gender == "neuter": gender = "n"
            if gender != "NULL":
                posTag = posTag[:6] + gender + posTag[7:]
            if degree == "positive": degree = "p"
            if degree == "comparative": degree = "c"
            if degree == "superlative": degree = "s"
            if degree != "NULL":
                posTag = posTag[:8] + gender

        mapping = {
            "noun": "n", "verb": "v", "adjective": "a",
            "adverb": "d", "conjunction": "c"
        }
        if(wanted_pos != "NULL"):
            wanted_pos = mapping.get(wanted_pos, wanted_pos)
            posTag = wanted_pos + posTag[1:]

        # now search parses using the global PARSES_DF
        df = PARSES_DF.loc[PARSES_DF["id"] == id]

        for _, row in df.iterrows():
            fits = True
            for i in range(8):
                char = posTag[i]
                if char != "-" and row["morph_code"][i] != char:
                    fits = False
            if fits and (len(output) > len(row["bare_text"]) or output == ""):
                output = row["bare_text"]
        if output:
            return output.replace("j", "i")

    return "ERROR: Nothing found"


def get_def_latin(id):
    df = LEMMA_DF.loc[LEMMA_DF["id"] == id]
    output = ""
    for _, row in df.iterrows():
        output = row.get("definition", "")
    return output


def get_FPP_latin(word = "NULL", id = "NULL", pos = "NULL"):
    if (word != "NULL"):
        ids = get_id_full_latin(word)
    if (id != "NULL"):
        ids = [id]

    output = {}
    for id in ids:
        output[id] = ""
        if (pos != "NULL"):
            parts_of_speech = [pos]
        else:
            parts_of_speech = get_POS_latin(id)
        if("n" in parts_of_speech):
            temp = get_POS_latin(id = id, case = "nominative", number = "singular")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, case = "nominative", number = "plural")
            if("ERROR" not in temp):
                output[id] = temp
        if("v" in parts_of_speech or "t" in parts_of_speech):
            temp = get_POS_latin(id = id, mood = "indicative", person = "first", number = "singular", tense = "present", voice = "active")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, mood = "indicative", person = "first", number = "plural", tense = "present", voice = "active")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, mood = "indicative", person = "third", number = "singular", tense = "present", voice = "active")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, mood = "indicative", person = "third", number = "plural", tense = "present", voice = "active")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, mood = "indicative", person = "first", number = "singular", tense = "present")
            if("ERROR" not in temp):
                output[id] = temp
        if("a" in parts_of_speech):
            temp = get_POS_latin(id = id, case = "nominative", number = "singular", degree = "positive", gender = "masculine")
            if("ERROR" in temp):
                temp = get_POS_latin(id = id, case = "nominative", number = "singular", gender = "masculine")
            if("ERROR" not in temp):
                output[id] = temp

    return output


def get_dict_latin(word, show_def = False):
    ids = get_id_full_latin(word)
    output = {}
    for id in ids:
        pos = ""
        dictEntry = ""
        rowText = ""
        morph = ""
        text = {}
        definition = get_def_latin(id)
        df = PARSES_DF.loc[PARSES_DF["id"] == id]
        for i in range(10):
            if(not i in text):
                text[i] = "NULL"
        for _, row in df.iterrows():
            rowText = row["bare_text"]
            morph = row["morph_code"]
            if (row["morph_code"][0] == "n" and (pos == "" or pos == "noun")):
                pos = "noun"
                text[2] = row["morph_code"][6]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "n")):
                    if(text[0] == "NULL" or len(row["bare_text"])<len(text[0])):
                        text[0] = row["bare_text"]
                if((row["morph_code"][2] == "s") and (row["morph_code"][7] == "g")):
                    if(text[1] == "NULL" or len(row["bare_text"])<len(text[1])):
                        text[1] = row["bare_text"]
            if (row["morph_code"][0] == "a"):
                pos = "adj"
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
        if(type(definition) != type("str") or len(definition) == 0):
            definition = "No Definiton"
        if(text[0] == "NULL"):
            df2 = LEMMA_DF.loc[LEMMA_DF["id"] == id]
            for _, row in df2.iterrows():
                text[0] = row["bare_text"]
        match(pos):
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
                if(text[0]!= "NULL"):
                    kind = "regular"
                elif(text[5] != "NULL"):
                    kind = "deponent"
                else:
                    kind = "impersonal"
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
            case _:
                dictEntry = pos + ": " + text[0]
                if(show_def):
                    dictEntry += " " + definition 
        output[id] = (dictEntry)
    return output

if(__name__ == '__main__'):
    print("hello")
    print(get_latin_form("pulchra", wanted_pos= "a", case = "a", number = "s", 
                         degree= "p", gender = "f"))
    print(get_latin_form("Romanus", case = "v", number = "p", gender = "m", 
                         wanted_pos = "a", ))
    print(get_latin_form("romanus", case = "v", number = "p", gender = "m", 
                         wanted_pos = "a", ))
    print(get_latin_form("clamo", tense = "l", wanted_pos= "v", 
                         mood = "indicative", number = "plural",
                         voice = "active", person = "third"))