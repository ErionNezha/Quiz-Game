# Kuiz i Kafshave — nga Erion Nezha (c) 2026. Te gjitha te drejtat te rezervuara.

def kontrollo_pergjigjen(pergjigja, sakta):
    global piket
    vazhdon = True
    tentativa = 0
    while vazhdon and tentativa < 3:
        if pergjigja.lower() == sakta.lower():
            print("Pergjigje e saktë! ✅")
            piket = piket + 1
            vazhdon = False
        else:
            if tentativa < 2:
                pergjigja = input("Gabim, provo përsëri: ")
            tentativa = tentativa + 1
    if tentativa == 3:
        print("Përgjigja e saktë është:", sakta)

piket = 0
print("Gjej Kafshën 🐾")
p1 = input("Cili ari jeton në Polin e Veriut? ")
kontrollo_pergjigjen(p1, "ariu polar")
p2 = input("Cila është kafsha më e shpejtë e tokës? ")
kontrollo_pergjigjen(p2, "gatopardi")
p3 = input("Cila është kafsha më e madhe? ")
kontrollo_pergjigjen(p3, "balena blu")
print("Rezultati yt është: " + str(piket) + "/3")
