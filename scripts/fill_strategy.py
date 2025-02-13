import json
import os

strategy_files = {
    "strategy/Co_strategy/co_strategy.json": {
        "name": "CoinArbitr strategy",
        "description": "Pagrindinė strategija, skirta ai.assist kūrimui ir valdymui.",
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
            "CoinArbitr strategy": "Pagrindinė ai.assist kūrimo strategija"
        },
        "hierarchy": {
            "1": {
                "name": "Co",
                "description": "ChatGPT projektas CoinArbitr, kuris valdo visą strategiją",
                "sub": {
                    "2": {
                        "name": "CoinArbitr strategy",
                        "description": "Pagrindinė strategija, nustatanti ai.assist kūrimo principus"
                    }
                }
            }
        }
    },
    "strategy/ai_assist_pr_strategy/ai_assist_strategy.json": {
        "name": "ai.assist strategy",
        "description": "Strategija, skirta ai.assist projekto vystymui.",
        "version": "v1.1",
        "objectives": [
            "Plėsti ai.assist funkcionalumą",
            "Automatizuoti API naudojimo optimizaciją",
            "Integruoti chato sąsają į ai.assist sistemą"
        ]
    }
}

# Sukuriame failus ir įrašome duomenis
for file_path, content in strategy_files.items():
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

print("✅ Strategijos failai sėkmingai užpildyti!")
