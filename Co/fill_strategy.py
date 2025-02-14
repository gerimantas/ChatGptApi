import json
import os

strategy_files = {
    "strategy/Co_strategy/co_strategy.json": {
        "name": "CoinArbitr strategy",
        "description": "Pagrindinė strategija, skirta bot_aps kūrimui ir valdymui.",
        "version": "v1.1",
        "goals": [
            "Sekti CoinArbitr strategijos įgyvendinimą",
            "Automatizuoti strategijos fiksavimą ir progreso stebėjimą",
            "Užtikrinti sesijų konteksto perkėlimą tarp Co sesijų"
        ]
    },
    "strategy/Co_strategy/co_strategy_info.json": {
        "shortcuts": {
            "Co": "ChatGPT projektas CoinArbitr",
            "CoinArbitr strategy": "Pagrindinė bot_aps kūrimo strategija"
        },
        "hierarchy": {
            "1": {
                "name": "Co",
                "description": "ChatGPT projektas CoinArbitr, kuris valdo visą strategiją",
                "sub": {
                    "2": {
                        "name": "CoinArbitr strategy",
                        "description": "Pagrindinė strategija, nustatanti bot_aps kūrimo principus"
                    }
                }
            }
        }
    },
    "strategy/bot_aps_pr_strategy/bot_aps_strategy.json": {
        "name": "bot_aps strategy",
        "description": "Strategija, skirta bot_aps projekto vystymui.",
        "version": "v1.1",
        "objectives": [
            "Plėsti bot_aps funkcionalumą",
            "Automatizuoti API naudojimo optimizaciją",
            "Integruoti chato sąsają į bot_aps sistemą"
        ]
    }
}

# Sukuriame failus ir įrašome duomenis
for file_path, content in strategy_files.items():
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

print("✅ Strategijos failai sėkmingai užpildyti!")
