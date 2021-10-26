# On importe les array_map
# Le premier fait le lien entre le Codon et la protéine
# Le second le lien entre la protéine en version courte, et son nom complet.
# Le second arraymap ayant un nom à ralonge, on lui donne un alias : s_to_l_map
from geneticCode import amino_acid_map
from geneticCode import shortname_to_longname_map as s_to_l_map
# Sequence de test : 
# ATTAUGCCGATACGGGGGGGGGCTATTTTATTTCCCAAUCCCCCUUAGCGAAGCUGAC

# Codon de démarrage :
initiatorCodonSequence = "AUG"
# Longeur de sequence
codonSequenceLenth = len(initiatorCodonSequence)

# Saisie de la séquence à convertir :
rna = input("Please enter your RNA sequence?\n")
# Longeur de la séquence
rnaLenth = len(rna)
# Affichage de la séquence, et de sa longeur
print("RNA sequence: \"%s\", length : %s." %(rna,rnaLenth))

# Trouver la position de la première occurence de 'initiatorCodonSequence' (AUG)
startIndex = rna.find(initiatorCodonSequence)

sequenceIndex = 0
# Si la position de depart est trouvé
if startIndex:
  # Affichage du codon de départ, et sa position
  print("Position of the Initiator Codon \"%s\" : %s." %(initiatorCodonSequence, startIndex))

  # On stock dans sequenceIndex la position de la séquence courante
  sequenceIndex  = startIndex
  # Tant que la position de la sequence courante, ne dépasse pas la longeur de la chaine ARN, et que le boolean est à true
  while (sequenceIndex < rnaLenth):
    # valeur actuelle du codon stocké dans 'currentCodon'
    currentCodon = rna[sequenceIndex:sequenceIndex+codonSequenceLenth]
    if currentCodon:
      # Pour chaque index de amino_acid_map (cf geneticCode.py)
      for key in amino_acid_map.keys() :
        # Si le currentCodon est dans l'index courant :
        if currentCodon in amino_acid_map[key]:
          # On affiche la clé corrrespondante
          print(s_to_l_map[key])
          # Si la clé est stop on arrete l'execution
          if key == "stop":
            break
    # On incrémente la position avec la longueur du codon courant
    sequenceIndex+=codonSequenceLenth
else:
  # Si pas de codon de départ, on affiche un message
  print("There is no initiator codon.")

