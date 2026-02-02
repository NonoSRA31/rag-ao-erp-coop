\# RAG AO ERP – Coopératives agricoles



Ce projet implémente un outil de type RAG (Retrieval-Augmented Generation)

destiné à assister la réponse aux appels d’offres privés ERP

dans le contexte des coopératives agricoles et groupes agro-industriels.



L’objectif n’est pas de générer automatiquement des réponses commerciales,

mais de produire des réponses :

\- structurées,

\- traçables au cahier des charges,

\- sans hallucination,

\- validables par des décideurs métier.



---



\## Périmètre fonctionnel



L’outil est conçu pour intervenir sur des projets de type :

\- remplacement d’ERP,

\- refonte applicative,

dans des contextes coopératifs complexes (multi-sociétés, multi-sites).



Il couvre notamment les domaines :

\- Achats / Approvisionnements,

\- Stocks et traçabilité,

\- Logistique,

\- Finance,

\- Ventes.



---



\## Principes non négociables



\- Une section d’appel d’offres = une génération

\- Aucune génération sans contexte explicite

\- Aucun engagement automatique (délais, coûts, promesses)

\- Validation humaine obligatoire

\- Zéro hallucination par construction



---



\## Architecture générale



Le projet est structuré autour de :

\- données d’appels d’offres découpées par section (`/data`)

\- un template de réponse figé (`/templates`)

\- un backend Python contrôlant strictement le LLM (`/backend`)

\- un mécanisme de retrieval ciblé (RAG)



L’interface utilisateur (non incluse à ce stade) impose le workflow

et empêche tout usage de type chatbot libre.



---



\## Workflow d’utilisation



1\. Découper l’appel d’offres par section

2\. Charger une section dans l’outil

3\. Appliquer le template de réponse

4\. Générer sous contraintes

5\. Valider automatiquement

6\. Arbitrer humainement

7\. Exporter la réponse



---



\## Statut du projet



Projet en cours de construction.

Les premières étapes portent sur :

\- la structuration du backend,

\- la sécurisation des générations,

\- la mise en place du RAG ciblé.



