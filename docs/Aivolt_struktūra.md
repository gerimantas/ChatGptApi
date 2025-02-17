Aivolt/
│
├── ai_core/  # Pagrindiniai APS komponentai
│   ├── project_manager.py      # AI projektų valdymas (#APS_project_manager)
│   ├── model_selection.py      # AI modelių parinkimas (#APS_model_selection)
│   ├── task_execution.py       # Užduočių vykdymas (#APS_core)
│   ├── instruction_loader.py   # AI instrukcijų valdymas
│   ├── workspace_setup.py      # Projekto aplinkos paruošimas
│
├── strategy/  # Strategijos valdymas
│   ├── APS_strategy/  # AI strategija
│   │   ├── model_optimization.md
│   │   ├── system_design.md
│   │   ├── automation_planning.md
│   │
│   ├── CL_strategy/  # Kliento AI strategija
│       ├── project_scope.md
│       ├── client_requirements.md
│
├── client_projects/  # Kliento AI projektų laikymas
│   ├── client_X_project/
│   │   ├── requirements.json
│   │   ├── strategy.md
│   │   ├── assistant_code.py
│
├── generated_agents/  # Sugeneruoti AI asistentai
│   ├── agent_001/
│   │   ├── main.py
│   │   ├── config.json
│
├── delivery/  # Baigtų projektų pateikimas klientui
│   ├── client_X_final.zip
│   ├── documentation.pdf
│
├── tests/  # Testavimo sistema
│   ├── ai_core/
│   │   ├── test_task_execution.py
│   │   ├── test_model_selection.py
│   ├── client_agents/
│       ├── test_generated_agents.py
│
├── session_management/  # Sesijų ir užduočių stebėjimas
│   ├── session_registry.py
│
├── docs/  # Dokumentacija
│   ├── README.md
│   ├── API_DOCUMENTATION.md
│   ├── STRUCTURE_OVERVIEW.md
│
├── logs/  # AI ir klaidų sekimo žurnalai
│   ├── openai_client_errors.log
│   ├── system_activity.log
│
├── config/  # Sistemos nustatymai ir konfigūracija
│   ├── ai_config.json
│   ├── logging_config.json
│   ├── settings.json
│
├── scripts/  # Pagalbiniai skriptai
│   ├── check_gpt_model.py
│   ├── automate_testing.py
│
├── automation/  # Automatiniai procesai
│   ├── automation.py
│
├── cache/  # Laikini failai ir AI modelių cache
│   ├── openai_cache.db
│
├── error_tracking/  # Klaidos ir jų analizė
│   ├── error_tracking.py
│
├── file_management/  # Failų tvarkymas
│   ├── file_management.py
│
├── .git/  # Versijų kontrolės sistema (jei naudojamas GitHub)
│
├── .env  # Konfigūracijos failai
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
