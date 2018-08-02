# ISAMM Summer Challenge
# Subject 4: Design and development of an app dedicated to the management of ISAMM Clubs

## Subject Assigned To Team 15
Achref - achref.yak@gmail.com


Acteurs :
 Représentant d’un Club
 ○ Président
 ○ Staff
Responsable relations clubs
 Etudiant


Fonctionnalités :
 Représentant d’un Club :
 *  Réserver le local des clubs
 *  Les présidents des clubs peuvent réserver le local du club pour des réunions ou des workshops.
 *  Réserver une date et une salle des événements/formations:
 *  Les présidents des clubs peuvent réserver des dates des événements/formations pour éviter les problèmes de logistiques.
 *  Gérer les staffs/membres du club:
 *  Les présidents des clubs peuvent gérer(consulter, ajouter , supprimer) les staffs/membres de leur club pour avoir accès à la plateforme.
 *  Consulter et gérer le calendrier des évènements qui se déroulent à l’ISAMM (ajouter, modifier, supprimer, archiver évènement).
 *  Admission aux clubs: Les étudiants peuvent faire des demandes d'admission aux clubs le président du club peut accepter ou refuser cette demande .
 *  Affectation de missions aux membres du club (qui affecte des missions : de communication de publicité, etc aux différents membres? le président du club?)
 Etudiant :
 * Demander de joindre un club
 *  Consulter les anciens et les nouveaux événements qui auront lieu à l’ISAMM (donc consulter le calendrier et l’archive ou l’historique).
 *  Dans chaque page d'événement on trouve :
Les photos de l'événement
Les détails de l’évènement
Les récompenses
Les partenaires
Les sponsors
 *  Consulter le calendrier des évènements qui se déroulent à l’ISAMM (c’est la même fonctionnalité que là haut?)
 *  Evaluer les événements auxquels il a participé : il vaut mieux avoir une interface “mes évènements” pour chaque 
membre où il pourra trouver les évènements auxquels il a participé et pouvoir les évaluer, les évènements marqués “je m’intéresse à” et les évènements marqués “je participe”.

Technologies:
 * framework django 1.8.0
  Django est un framework web gratuit et libre écrit en Python. Un framework web est un ensemble de composants qui vous aide à développer des sites web plus rapidement et plus facilement.
  Lorsque vous créez un site web, vous avez souvent besoin de la même chose : une manière de gérer l'authentification de vos utilisateurs (créer un compte, se connecter, se déconnecter), une partie dédiée à
  la gestion de votre site, des formulaires, une manière de mettre en ligne des fichiers, etc.
 * Angular est un framework JavaScript Open Source développé par Google. Il utilise l’architecture MVM (Modèle Vue Modèle), proche du modèle MVC. Cela va permettre de structurer son code et bien séparer la vue (l’interface) des modèles (fonctionnement).
   Il est considéré comme un langage « côté client », ceux-ci permettent de gérer l’interface utilisateur de chaque page (affichage, interactions…) de façon dynamique et viennent en complément aux langages côté serveur.