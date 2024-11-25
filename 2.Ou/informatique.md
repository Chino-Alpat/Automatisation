<!-- .slide: data-state="nologo-slide" style="text-align: center" -->
#  Dans l'informatique

* Tp pilotage récupération d'information sur un site web, comparaison d'information de différent format

![comparaison_de_doc](images/comparaison_de_doc.webp "comparaison_de_doc") <!-- .element: width="100px" -->


Vous êtes un développeur web chevronné et avez créer une page web sur laquelle vous avez listé tous les films que vous avez vu, vous avez noté ces films de 1 à 5 étoiles.
Michel de la compta, cinéphile averti également à fait la même chose de son coté mais lui à rempli un fichier excel qu'il a exporté en CSV.
Pas toujours d'accord mais convaincu du bien fondé de l'avis de chacun d'entre vous, vous souhaitez croiser ces liste pour en établir une nouvelle.



## Exercice 1
En python, écrire un script qui permet d'ouvrir le fichier suivant: **film-de-michel.csv**,
extraire les informations de ce fichier pour en faire un dictionnaire python au format suivant : 
```
{
    "titre du film": {
        "année": 2024,
        "note": 2
    },
    "titre d'un autre film": {
        "année": 2024,
        "note": 4
    }
}
```

## Exercice 2
En python, écrire un script qui permet d'ouvrir la page web suivante: **mes-film.html** sur le navigateur de votre choix, puis naviguez jusque la liste de vos films préférés, 
extraire les informations de ce site pour en faire un dictionnaire python au même format que le précédent


## Exercice 3
Maintenant que vous savez comment récupéré les informations de votre site **mes-film.html** et les informations du fichiers **film-de-michel.csv**, créer un script qui va faire ces deux actions successivement, 
puis créer un fichier Json **critique-global.json** qui listera tous les films que vous et michel aurez vu **cette année** avec votre note, la note de michel, et la note moyenne du film.


![michel et moi](images/michel_et_moi.webp "michel_et_moi") <!-- .element: width="100px" -->
