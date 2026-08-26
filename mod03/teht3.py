suorakulmionkanta_str = input("Anna suorakulmion kannan pituus: ")
suorakulmionkorkeus_str = input("Anna suorakulmion korkeus: ")
suorakulmionkanta = float(suorakulmionkanta_str)
suorakulmionkorkeus = float(suorakulmionkorkeus_str)
suorakulmionpinta_ala = suorakulmionkanta * suorakulmionkorkeus
suorakulmionpiiri = 2*(suorakulmionkanta + suorakulmionkorkeus)
print("Suorakolmion pinta-ala on: " + str(suorakulmionpinta_ala))
print("Suorakulmion piiri on: " + str(suorakulmionpiiri))