N = ["SENTENCE","NOUN-PHRASE","VERB-PHRASE","ARTICLE","ADJECTIVE","NOUN","VERB","ADVERB"]
N_tree = {"SENTENCE":{"NOUN-PHRASE":["ARTICLE","ADJECTIVE","NOUN"],"VERB-PHRASE":["VERB","ADVERB"]}}
S = N[0]
T = ["the","hungry","sleepy","cat","dog","chases","runs","quickly","slowly"]

P = {
 	"SENTENCE":[["NOUN-PHRASE","VERB-PHRASE","NOUN-PHRASE"],["NOUN-PHRASE","VERB-PHRASE"]],
 	"NOUN-PHRASE":[["ARTICLE","ADJECTIVE","NOUN"],["ARTICLE","NOUN"]],
 	"VERB-PHRASE":[["VERB","ADVERB"],["VERB"]],
 	"ARTICLE":["the","es"],
 	"ADJECTIVE":["hungry","sleepy"],
 	"NOUN":["cat","dog"],
 	"VERB":["chases","runs"],
 	"ADVERB":["slowly","quickly"]
}

sentence = ''

print("NDICT:",N_tree)
print("\nSENTENCE:",P['SENTENCE'][1])
print("\tNOUN-PHRASE:",P["NOUN-PHRASE"][0])
print("\t\tARTICLE:",P["ARTICLE"][0])
sentence+=P["ARTICLE"][0]+' '
print("\t\tADJECTIVE:",P["ADJECTIVE"][1])
sentence+=P["ADJECTIVE"][1]+' '
print("\t\tNOUN:",P["NOUN"][0])
sentence+=P["NOUN"][0]+' '
print("\tVERB-PHRASE:",P["VERB-PHRASE"][0])
print("\t\tVERB:",P["VERB"][1])
sentence+=P["VERB"][1]+' '
print("\t\tADVERB:",P["ADVERB"][0])
sentence+=P["ADVERB"][0]
print("\nFinal product:",sentence)