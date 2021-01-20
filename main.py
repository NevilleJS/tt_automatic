import camelot
import pandas
import re

# ------------------------------------------------------------------------>

#       OPENING DOC
doc = camelot.read_pdf("tt.pdf", pages="all")

# ------------------------------------------------------------------------>


#       FUNCTION TO FILL UPCOMING BLANK DATES
def date_filler(filler_doc):
    prv_date = ""
    for i in range(len(filler_doc)):
        if filler_doc.at[i, 0] != '':
            prv_date = filler_doc.at[i, 0]
        else:
            filler_doc.at[i, 0] = prv_date
    return filler_doc


# ------------------------------------------------------------------------>

#       APPENDING TABLES OF EACH PAGE
com_doc = doc[0].df

for i in range(1, doc.n):
    com_doc = com_doc.append(doc[i].df)
com_doc = com_doc.reset_index(drop=True)

# ------------------------------------------------------------------------>

#       SOME CLEANING UP OF UNWANTED CELLS
com_doc.drop([0, 1, 2], inplace=True)
com_doc = com_doc.reset_index(drop=True)

com_doc.drop(com_doc[com_doc[3] == ''].index, inplace=True)
com_doc = com_doc.reset_index(drop=True)

# ------------------------------------------------------------------------>

#       date_filler CALL
com_doc = date_filler(com_doc)

# ------------------------------------------------------------------------>

#       MORE CLEANING UP
com_doc.drop([1, 5], axis=1, inplace=True)
com_doc.drop(
    com_doc[(com_doc[2] == "BOTANY") | (com_doc[4] == '')].index, inplace=True)  # EXCLUDING BIOLOGY CLASSES
com_doc = com_doc.reset_index(drop=True)
com_doc = com_doc.T.reset_index(drop=True).T  # RESETING COLUMN INDEX hack

# ------------------------------------------------------------------------>

#   TEMP REGEX
# re.findall(r'\d+', "")

#   LOOPING THROUGH EACH CELL WHILE EXTRACTING CLASS NUMBER(class num returns a list)
# for y in range(len(com_doc)):
#     for x in range(len(com_doc.columns)-1):
#         com_doc.iloc[y, x]
#     re.findall(r"\d+", com_doc.iloc[y, len(com_doc.columns)-1])
# print("\n")
