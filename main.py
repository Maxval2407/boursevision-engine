from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI()

class Action(BaseModel):
    ticker: str
    nom: str

class AnalyseIA(BaseModel):
    score_technique: float
    commentaire_technique: str
    score_fondamentale: float
    commentaire_fondamentale: str
    score_semantique: float
    commentaire_semantique: str
    potentiel_pct_min: float
    potentiel_pct_max: float
    horizon_jours_min: int
    horizon_jours_max: int
    conseil: str
    niveau_risque: str
    confiance_global: float

@app.post("/analyser")
def analyser_actions(actions: List[Action]) -> Dict[str, AnalyseIA]:
    reponses = {}
    for action in actions:
        potentiel_min = round(random.uniform(1.0, 3.0), 2)
        potentiel_max = round(potentiel_min + random.uniform(2.0, 5.0), 2)
        horizon_min = random.randint(3, 10)
        horizon_max = horizon_min + random.randint(5, 15)
        confiance = round(random.uniform(60, 90), 1)
        conseil = "Achat" if confiance > 75 else ("Vente" if confiance < 65 else "Attente")
        risque = "Faible" if confiance > 80 else ("Modéré" if confiance > 70 else "Élevé")

        reponses[action.ticker] = AnalyseIA(
            score_technique = round(random.uniform(6.0, 9.0), 1),
            commentaire_technique = "Tendance haussière détectée sur 5 séances, volumes en hausse.",
            score_fondamentale = round(random.uniform(6.5, 9.5), 1),
            commentaire_fondamentale = "Ratios financiers attractifs, croissance stable, endettement maîtrisé.",
            score_semantique = round(random.uniform(5.0, 8.5), 1),
            commentaire_semantique = "Ton globalement positif dans les dernières actualités.",
            potentiel_pct_min = potentiel_min,
            potentiel_pct_max = potentiel_max,
            horizon_jours_min = horizon_min,
            horizon_jours_max = horizon_max,
            conseil = conseil,
            niveau_risque = risque,
            confiance_global = confiance
        )
    return reponses
