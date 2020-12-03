s = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
pat="ATC"

'''функция и вызов функции'''
def PatternCount (Pattern, Text):
  count = 0
  for i in range (len(Text) - len(Pattern) + 1):
    if Text[i:i + len(Pattern)] == Pattern:
      count = count + 1
  return count
  
print(PatternCount(pat,s))

''''''
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
   return Count

'''удаление повторных'''
def remove_duplicates(Items):
    ItemsNoDuplicates = []
    ItemsNoDuplicates = list(set(Items))
    return ItemsNoDuplicates

'''вывод частых сочетаний'''
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

'''Поиск позиции, с которых начинается определенный Pattern'''    
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range (len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions
    
'''Нахождение комплиментарной строки нуклеотидов ДНК'''    
def complement(Nucleotide):
    comp = []
    for ch in Nucleotide:
        if ch == 'A':
            comp.append('T')
        if ch == 'C':
            comp.append('G')
        if ch == 'T':
            comp.append('A')
        if ch == 'G':
            comp.append('C')
    return ''.join(comp)
    
def ReverseComplement(Pattern):
    revComp = '' 
    revComp = reverse(complement(Pattern))
    return revComp

def reverse(Text):
    reVerse = ''
    reVerse = Text[::-1]
    return reVerse
