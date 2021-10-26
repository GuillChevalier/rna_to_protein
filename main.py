# On importe les array_map
# Le premier fait le lien entre le Codon et la protéine
# Le second le lien entre la protéine en version courte, et son nom complet.
# Le second arraymap ayant un nom à ralonge, on lui donne un alias : s_to_l_map
from geneticCode import amino_acid_map
from geneticCode import shortname_to_longname_map as s_to_l_map
# Sequence de test : 
# AUUAUGCCGAUACGGGGGGGGGCUAUUUUAUUUCCCAAUCCCCCUUAGCGAAGCUGAC

# Codon de démarrage :
initiatorCodonSequence = "AUG"
# Longeur de sequence
codonSequenceLength = len(initiatorCodonSequence)

# Saisie de la séquence à convertir :
rna = input("Please enter your RNA sequence?\n")
# Longeur de la séquence
rnaLenth = len(rna)
# Affichage de la séquence, et de sa longeur
print("Loaded RNA sequence: \"%s\", length: %s. \n" %(rna,rnaLenth))

# Trouver la position de la première occurence de 'initiatorCodonSequence' (AUG)
startIndex = rna.find(initiatorCodonSequence)

sequenceIndex = 0
print(startIndex)
# Si la position de depart est trouvé
if startIndex >= 0:
  # Affichage du codon de départ, et sa position
  print("Position of the Initiator Codon \"%s\": %s." %(initiatorCodonSequence, startIndex))

  # On stock dans sequenceIndex la position de la séquence courante
  sequenceIndex  = startIndex
  # Pour forcer l'arret de la boucle, on utilise ce boolean, on defini par defaut sportLoop à false
  stopLoop = False
  # proteinsList sert à stocker la liste des proteins
  proteinsList = ""
  # proteinsList2= ""
  # Tant que la position de la sequence courante, ne dépasse pas la longeur de la chaine ARN, et que le boolean est à false
  while (sequenceIndex < rnaLenth) and stopLoop == False :
    # valeur actuelle du codon stocké dans 'currentCodon'
    currentCodon = rna[sequenceIndex:sequenceIndex+codonSequenceLength]
    # On incrémente la position avec la longueur du codon courant
    sequenceIndex = sequenceIndex + codonSequenceLength
    if currentCodon:
      # Pour chaque index de amino_acid_map (cf geneticCode.py)
      # print(amino_acid_map.keys())
      for key in amino_acid_map.keys() :
        # print(key)
        # print(amino_acid_map[key])
        # Si le currentCodon est dans l'index courant :
        if currentCodon in amino_acid_map[key]:
          # On ajoute à la chaine proteinsList le codon converti, la protéine correspondante, et son abréviation. 
          proteinsList += " | " +currentCodon + " | " + s_to_l_map[key] + " ("+ key +")\n"
          # proteinsList2 = proteinsList2 + s_to_l_map[key] + ", "
          # Si la clé est stop on arrete l'execution
          if key == "stop":
            # On force donc la sorti de la boucle while
            stopLoop = True
            # On affiche la position du codon stop ainsi que sa valeur
            print("Position of the \"Stop\" Codon \"%s\" : %s." %(currentCodon, sequenceIndex))
            # On affiche la séquence interprétée
            print("Converted RNA sequence : \"%s\".\n" %rna[startIndex:sequenceIndex])
            # On affiche la liste des protéines trouvées
            print("Protein list : \n%s\n" %proteinsList)
            # print("Protein list : \n%s\n" %proteinsList2)
            # On affiche un message de fin d'exection            
            print("End of execution.\n")
            # On sort de la for
            break
else:
  # Si pas de codon de départ, on affiche un message
  exit("There is no initiator codon.")

