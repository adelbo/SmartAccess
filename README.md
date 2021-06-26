# SmartAccess
Ce système de pointage doit assurer les tâches suivantes :
Gestion de présence des personnels (heure d’entrée et heure de sortie). Pour assurer cette tâche on procède à trois méthodes:
Par l’utilisation d’une carte RFID
Par la détection de visage
Manuellement
Gestion des personnels : cette fonction assure l’ajout, la modification et la suppression des employées.
Gestion des visiteurs : Pour assurer la sécurité de la société il faut bien gérer les visiteurs.
Gestion des stagiaires : cette fonction assure l’ajout, la modification et la suppression des stagiaires.
Stockage des données dans une base afin d’être manipuler par le responsable.

Fonctionnement désiré
On s’appuyant sur l’organigramme suivant, nous présentons le fonctionnement du système.
Marquage de présence de l’employé
Présence de l’employée devant la pointeuse. 
Choix de la méthode de pointage 
En cas de pointage avec la RFID
Passage de la carte devant le lecteur 
Lecture de la carte 
Test de l’existence du code 
Si le code existe:
Allumage d’une diode verte 
Bip Sonore
Affichage des informations de présence sur une interface graphique
Ouverture de la porte pour autoriser l’accès

Sinon:
Allumage d’une diode rouge
Bip Sonore
En cas de pointage avec la reconnaissance faciale
Passage de l’employé devant la caméra
Capture de l’image
Comparaison de l’image avec l’existante
Si l’image existe:
Allumage d’une diode verte 
Bip Sonore
Affichage des informations de présence sur une interface graphique
Ouverture de la porte pour autoriser l’accès
Sinon:
Allumage d’une diode rouge
Bip Sonore

En cas de pointage Manuel
Ecriture de code 
Vérification de l’existence du code 

Si le code existe:
Allumage d’une diode verte 
Bip Sonore
Affichage des informations de présence
Ouverture de la porte pour autoriser l’accès
Sinon:
Allumage d’une diode rouge
Bip Sonore

Stockage de données de présence et les informations des personnels dans une base de données afin de faciliter la gestion de présence.

Gestion de l’article
Passage de la carte devant le lecteur 
Lecture de la carte 
Test de l’existence du code 
Si le code existe:
-Allumage d’une diode verte 
-Affichage des informations sur l’article
-autorisation de gestion des articles (ajouter/retirer)
Sinon:
                                    -Allumage d’une diode rouge
-interdiction de gestion des articles (ajouter/retirer)
