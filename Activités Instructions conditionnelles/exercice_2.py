def jeu(x):
    votre_santé = 100
    santé_adversaire = 200 
    puissance_attaque = 120
    if x <= 2 :
        votre_santé = votre_santé // 2
    elif 3<= x <= 8 :
        santé_adversaire = santé_adversaire - puissance_attaque
    else :
        santé_adversaire = 0 
    print('Nombre dé :', x,'| Votre santé',votre_santé,'| Santé adverse',santé_adversaire)
jeu(2),jeu(8),jeu(10)