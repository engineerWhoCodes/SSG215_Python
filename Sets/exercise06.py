#Using dict to check the membership of an item against another.
sciGreats = {'Antoine-Laurent de Laoisier', 'Isaac Newton', 'Michael Faraday', 'Humphrey Davy', ' Lord Rayleigh', 'James Clerk Maxwell', 'John Dalton', 'John William Strutt Baron Rayleigh'}
nobLaur = {'Henri Becqurel', 'Marie Curie', 'Robert Goddard', 'Pierre Jolliot', 'Wolfgang Pauli', 'Levi Von Mises', 'Paul Dirac', 'Robert Andrews Millikan', 'Neils Bohr', 'Louis de Broglie', 'Albert Einstein', 'Wilhelm Rontgen', 'Max Born', 'Jack St. Claire Kilby', 'Albert Fert', 'Erwin Schrondinger', 'Roger Penrose', 'John William Srtutt Baron Rayleigh', 'Reinhard Genzel', 'Andrea Ghez', 'James Peebles', 'Didier Queloz', 'Michel Mayor', 'Donna Strickland', 'Gerard Mourou'}
myDict = {} 
for sct in sciGreats:
    if sct  in nobLaur:
        myDict[sct] = 'Nobel Laureate'
    else:
        myDict[sct] = 'Simply Great'
print('The laureate list:', myDict)
    