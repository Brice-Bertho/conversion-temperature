# Installation

`pip install web.py`

# Lancement de l'application

`python app.py`

# Tester the application

Accédez à l'application via l'url : `http://localhost:8080`
Vous pouvez également accéder à des sous routes telles que :

- `http://localhost:8080/GordonRamsay`
- `http://localhost:8080/users`
- `http://localhost:8080/users/1`

# Lire le script actuellement mis en place

Avant de modifier un script existant , il est toujours interessant de le lire et de le comprendre.
Prenez donc un premier temps à lire les scripts qui se déroule. au sein de app.py

# Exercice à réaliser

Forkez ce dépôt, implémentez votre code puis une fois satisfait par votre travail, réalisez une merge request.

En vous inspirant du script présent , nous allons réaliser un web service qui nous permets de réaliser des conversions de température.
Voici les routes souhaitées :

- /c={temp}
- /f={temp}
- /k={temp}

Et le site nous retourne la conversion en Celsius, Fahrenheit et Kelvin au sein de la structure suivante : 

```xml
<temperature>
  <celsius></celsius>
  <fahrenheit></fahrenheit>
  <kelvin></kelvin>
</temperature>
```

Sachant que voici les conversions, en prenant C une température en Celsius, F une température en Fahrenheit et K une température en Kelvin :

 - C = (F-32)/1.8
 - K = C + 273.15

 N'oubliez pas de fournir les entêtes de réponse adéquats.
 En cas d'erreur, il est attendu à ce que vous retourniez la structure suivante : 

```xml
<temperature>
  <error></error>
</temperature>
```

En plus de la réalisation de cet XML, veuillez réaliser le XSD associé!
