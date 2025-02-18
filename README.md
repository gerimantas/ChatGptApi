Aivolt/
├── APS_core/                # Pagrindinė Aivoilt sistema (Autonominė Projektų Sistema)
│   ├── APS_client_manager/  # Užsakymų iš kliento valdymas
│   │   ├── order_handler.py       # Apdoroja naujus užsakymus
│   │   ├── client_communication.py # Bendrauja su užsakovu
│   │   ├── project_initializer.py  # Paruošia naują AI asistento projektą
│   │   ├── client_data.json        # Klientų užsakymų duomenų saugykla
│   │
│   ├── APS_project_manager/  # AI asistento projektų valdymas
│   │   ├── project_tracker.py      # Sekami aktyvūs projektai
│   │   ├── project_scheduler.py    # Planavimo ir užduočių skirstymo modulis
│   │   ├── project_database.json   # Projektų registracija
│   │
│   ├── APS_strategy/         # Strategijos kūrimas ir analizė
│   │   ├── strategy_analyzer.py   # AI strategijos analizė
│   │   ├── objective_definer.py   # Tikslų ir gairių nustatymas
│   │   ├── decision_maker.py      # AI strategijos pasirinkimas
│   │   ├── risk_management.py     # Rizikos vertinimas ir mažinimas
│   │
│   ├── APS_model_selection/  # AI modelių parinkimas projektams
│   │   ├── model_selector.py      # Parenka tinkamiausią modelį
│   │   ├── model_comparator.py    # Lygina skirtingus modelius
│   │   ├── dataset_handler.py     # Tvarko mokymo duomenis
│   │
│   ├── APS_testing/          # Testavimo sistema
│   │   ├── unit_tests/             # Vienetinių testų katalogas
│   │   │   ├── test_strategy.py
│   │   │   ├── test_model_selection.py
│   │   ├── integration_tests/       # Integracinių testų katalogas
│   │   │   ├── test_project_manager.py
│   │   │   ├── test_delivery.py
│   │   ├── validation_engine.py     # Užtikrina, kad AI sprendimai būtų patikrinti
│   │
│   ├── APS_delivery/         # Galutinės AI asistento versijos pateikimas klientui
│   │   ├── report_generator.py  # Sukuria kliento ataskaitą
│   │   ├── presentation_maker.py # Generuoja vizualią AI asistento demonstraciją
│   │   ├── deployment_handler.py  # Paruošia AI asistento įdiegimą
│   │
│   ├── APS_management/       # Administravimo modulis (vidaus procesų valdymas)
│   │   ├── system_monitor.py      # Stebi sistemos veikimą
│   │   ├── logs_handler.py        # Tvarko log failus ir įvykius
│   │   ├── security_manager.py    # Užtikrina APS saugumą
│   │
│   ├── APS_structure/        # Failų struktūros valdymas
│   │   ├── structure_optimizer.py # Automatiškai optimizuoja aplankus
│   │   ├── structure_snapshot.txt # Struktūros kopijos saugojimas
│   │   ├── structure_logger.py    # Registruoja pokyčius
│
├── CL_client/               # Kliento projektai (užsakovo procesai)
│   ├── CL_project/          # AI asistento kūrimo procesas
│   │   ├── client_requirements.json # Kliento reikalavimų duomenys
│   │   ├── project_blueprint.py    # AI asistento architektūros aprašas
│   │
│   ├── CL_strategy/         # Kliento strategijos kūrimas
│   │   ├── requirement_analysis.py # Analizuoja kliento poreikius
│   │   ├── client_feedback.py      # Tvarko kliento atsiliepimus
│   │
│   ├── CL_agent/            # Sukurtas AI asistentas
│   │   ├── agent_code.py    # Klientui sukurtas AI kodas
│   │   ├── agent_docs.md    # Klientui skirta AI asistento dokumentacija
│   │
│   ├── CL_testing/          # Kliento testai
│   │   ├── final_validation.py  # Paskutinis testavimas prieš pristatymą
│   │   ├── performance_tests.py  # AI asistento veikimo vertinimas
│   │
│   ├── CL_delivery/         # Galutinė AI asistento versija klientui
│   │   ├── final_report.pdf     # Galutinė AI asistento ataskaita
│   │   ├── installation_guide.md # Diegimo instrukcijos klientui
│
├── config/                  # Konfigūracijos failai
│   ├── .env
│   ├── ai_config.json
│   ├── ai_instructions.json
│   ├── logging_config.json
│   ├── settings.json
│
├── cache/                   # Kešavimo katalogas
│   ├── models/              # AI modelių cache
│   ├── sessions/            # Sesijų cache
│   ├── openai_cache.db
│
├── docs/                    # Dokumentacija
│   ├── APS_Kliento_Struktura.md
│   ├── Aivolt_struktūra.md
│
├── logs/                    # Log failai
│   ├── openai_client_errors.log
│   ├── strategy_log.json
│
├── tests/                   # Bendra testų sistema
│   ├── test_ai_core.py
│   ├── test_api.py
│   ├── test_assistant_ui.py
│   ├── test_openai_client.py
│
├── venv/                    # Virtuali aplinka
│   ├── .gitignore
│   ├── pyvenv.cfg
│
├── README.md                # Projekto aprašymas
├── CHANGELOG.md             # Pakeitimų istorija
├── requirements.txt         # Priklausomybės
├── setup.py                 # Projekto diegimo failas
