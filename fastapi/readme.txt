L'API permet de réviser ses tables de multiplications.

Route GET : tablemulti/9 
-on va envoyer un nombre en paramètre et obtenir la table de multiplication entière de ce nombre (ici on a mis 9)

Route Post : /mult
- on va envoyer dans le body 2 nombre et recevoir un objet avec nos deux nombre et le résultat de leurs multiplication
request body :
{
  "val1": 7,
  "val2": 3
}
