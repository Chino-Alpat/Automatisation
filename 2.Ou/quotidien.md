<!-- .slide: data-state="nologo-slide" style="text-align: center" -->
# Où ?

* TP - Réalisez des exemples d'automatisation au quotidien, dans l'IT, dans l'industrie

<!-- .slide: data-state="nologo-slide" style="text-align: center" -->
# Au Quotidien 

* Tp pilotage de thermostat et d'une chaudière connecté

![pilotage chaudiere](images/pilotage_chaudiere.webp "pilotage chaudière") <!-- .element: width="100px" -->


## Exercice 1

Vous êtes féru d'automatisation et de domotique, vous avez donc investi dans un kit complet comprenant thermostat et chaudière connecté, 
cependant l'application qui permet de piloter ces éléments n'est pas compatible avec votre téléphone, et vous souhaiteriez pouvoir piloter tous ce système via votre ordinateur.
Grâce à vos contact chez chaudierepresdechezvous.com vous avez réussi à obtenir la documentation de l'API dont voici un extrait :

# TODO ajoutez la doc de l'API

**au regard cette documentation, rédigez un script python qui permet de consultez la température d'une pièce de la maison en particulier**

```
   De quelle pièce de la maison souhaitez vous connaitre la temperature ?
   Salle de bain
   Il fait XX dégré dans la salle de bain 
``` 


## Exercice 2
Vous savez désormais comment consultez la température d'une pièce en particulier, vous souhaitez maintenant listez toutes les pièce ou la temperature est en dessous d'une certaine valeur :

# TODO ajoutez la doc de l'API

**au regard cette documentation, rédigez un script python qui permet de listez toutes les pièces ou la temperature est en dessous d'une certaine valeur**

```
   temperature limite
   20
   Il fait moins de 20 dégré dans les pièces suivantes:
   chambre
   salle de bain
   salon
``` 

## Exercice 3
Maintenant qu'il vous est possible de connaitre les temperature de chaque pièces de votre maison, et de connaitre la liste des pièces ou il fait moins de X dégrés,
vous souhaitez mettre en place un système automatique qui vérifie la température de chaque pièce toutes les secondes, et qui si il fait plus de 20 degrés coupe le thermostat, et si il fait moins de 17 le rallume

