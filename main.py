html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Formation Python pour Débutants - Offre Spéciale</title>
    <meta name="description" content="Apprenez Python facilement avec cette formation complète. Découvrez l'offre spéciale dès maintenant.">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 40px;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #16a085;
        }
        a {
            display: inline-block;
            padding: 10px 15px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        a:hover {
            background-color: #2980b9;
        }
        ul {
            list-style-type: square;
        }
    </style>
</head>
<body>
    <h1>Formation Python pour Débutants</h1>
    <p>Vous voulez apprendre à coder en Python ? Cette formation est parfaite pour commencer.</p>
    
    <h2>Pourquoi choisir cette formation ?</h2>
    <ul>
        <li>Accessible aux débutants</li>
        <li>Certificat reconnu</li>
        <li>Apprentissage pratique et progressif</li>
    </ul>
    
    <p><a href="https://ton-lien-affiliation.com" target="_blank">
        👉 Cliquez ici pour découvrir l'offre
    </a></p>
</body>
</html>
"""

with open("mini_site_affiliation.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Mini-site avec style CSS créé : mini_site_affiliation.html")
