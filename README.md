# ft_linear_regression

Ce dépôt présente une implémentation from scratch d’un modèle de régression linéaire, sans utiliser de bibliothèques spécialisées en apprentissage automatique (scikit-learn, TensorFlow, PyTorch).  

L’objectif est de prédire le prix d’un véhicule en fonction de son kilométrage, en implémentant :  

- La fonction de coût (Mean Squared Error)  
- La mise à jour des paramètres via Gradient Descent
- La persistance du modèle entraîné  
- Une visualisation de la convergence et de la droite de régression  lancer la 

---
## Installation

Cloner le dépôt :  
```bash
git clone https://github.com/LeinaCorporan1/ft_linear_regression.git
cd ft_linear_regression
 ```

## Installation des dépendances
```bash
pip install -r requirements.txt
```
## entrainement
lancer l'entrainement sur data.csv
```bash
python train.py data.csv
```
Le script :

- Normalise les données

- Entraîne le modèle par descente de gradient

- Sauvegarde les paramètres dans un fichier theta.json

## Prédiction

Faire une prédiction pour un kilométrage donné :
```bash
  python predict.py 120000
```
