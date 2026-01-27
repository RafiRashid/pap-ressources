## BDD

- Elisa → base de données regroupant les caractéristiques des volontaires + missions → interface entre organismes et l’ASC → permet de voir l’évolution des contrats

- OSCAR  → bases de données permettant le suivi des demandes des organismes → caractéristiques de chaque organisme 

- Site du SC → bases de données permettant le suivi des candidatures

En bref :
- OSCAR : Données relatives aux organismes et à leur agrément 
- ELISA : Données relatives aux volontaires et à leur contrat
- Site du SC : Données liées aux candidats et candidatures

## Vers une consolidation des données : le projet entrepôt de données

- 3 BDD : OSCAR pour la partie organisme, ELISA pour la partie volontaires et le site internet qui traite les candidatures.

- jointure sur le numéro d’agrément des structures

- EDD permet d'unifier l’ensemble des informations sur le Service Civique.

- l’EDD conserve les données archivée => pouvoir réaliser des analyses rétrospectives et suivre l’évolution des indicateurs.

- Les données contenues dans l’entrepôt sont non-volatiles : elles ne peuvent être ni modifiées, ni supprimées, mais uniquement consultées.

- DSI responsable de l'EDD, PAP définit les indicateurs

- cartographie des données

