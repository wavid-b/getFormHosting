import pandas as pd
import os

# ---------- LOAD DATA ONCE ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LATIN_LEMMA_DF = pd.read_csv(
    os.path.join(BASE_DIR, "Dictionary_Dataframes/lemmas.csv"),
    sep="{"
)

LATIN_PARSES_DF = pd.read_csv(
    os.path.join(BASE_DIR, "Dictionary_Dataframes/parses.csv"),
    sep="{"
)

# ---------- FUNCTIONS ----------

def get_id_latin(word):
    word = word.lower()
    df = LATIN_LEMMA_DF.loc[LATIN_LEMMA_DF["bare_text"] == word]
    return list(df["id"].unique())

def get_id_parse_latin(word, input_ids):
    df = LATIN_PARSES_DF.loc[LATIN_PARSES_DF["bare_text"] == word]
    for _, row in df.iterrows():
        if row["id"] not in input_ids:
            input_ids.append(row["id"])
    return input_ids

def get_id_full_latin(word):
    ids = get_id_latin(word)
    return get_id_parse_latin(word, ids)

def get_POS_latin(id):
    df = LATIN_PARSES_DF.loc[LATIN_PARSES_DF["id"] == id]
    return list(df["morph_code"].str[0].unique())


def get_latin_form(word="NULL", id="NULL", case="NULL",
                  number="NULL", gender="NULL", mood="NULL",
                  person="NULL", tense="NULL", voice="NULL",
                  degree="NULL", alt_dialects=False, wanted_pos="NULL"):

    if word == "NULL" and id == "NULL":
        return "ERROR: Please enter a word or an ID"

    if word != "NULL" and id != "NULL":
        return "ERROR: Please enter a word or an ID, not both"

    if word != "NULL":
        word = word.lower().strip()
        ids = get_id_full_latin(word)
        if len(ids) == 0:
            return "ERROR: No matching words"
    else:
        ids = [id]

    for id in ids:
        output = ""
        posTag = "---------"
        pos = get_POS_latin(id)

        # --- noun ---
        if "n" in pos:
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
        if "v" in pos:
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

        if wanted_pos != "NULL":
            mapping = {
                "noun": "n", "verb": "v", "adjective": "a",
                "adverb": "d", "conjunction": "c"
            }
            wanted_pos = mapping.get(wanted_pos, wanted_pos)
            posTag = wanted_pos + posTag[1:]

        df = LATIN_PARSES_DF.loc[LATIN_PARSES_DF["id"] == id]

        for _, row in df.iterrows():
            fits = True
            for i in range(8):
                char = posTag[i]
                if char != "-" and row["morph_code"][i] != char:
                    fits = False
            if fits:
                output = row["bare_text"]

        if output:
            return output.replace("j", "i")

    return "ERROR: Nothing found"