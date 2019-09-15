#De sequence die je wilt analyseren
seq = "ATGCGATCGGACCATG"
#.count voor het tellen van de verschillende soorten nucleotiden
aantal_a = seq.count("A")
aantal_t = seq.count("T")
aantal_c = seq.count("C")
aantal_g = seq.count("G")
aantal_n = seq.count("N")
# voor het tellen van het totaal aantal nucleotiden
totaal = aantal_a + aantal_t + aantal_c + aantal_g + aantal_n
# het percentage CG berekenen van de sequentie
percentage_cg = (aantal_c + aantal_g) / (totaal) * 100
# printen van de gegevens
print (aantal_a)
print (aantal_t)
print (aantal_c)
print (aantal_g)
print (aantal_n)
print (totaal)
print (percentage_cg)

