## [1.0.1] - YYYY-MM-DD

### Pridėta:
- Async/Await palaikymas `assistant_ui.py`
- Automatiniai testai `test_assistant_ui.py`
- Priverstinis `ai_instructions.json` tikrinimas

### Patobulinta:
- OpenAI užklausų valdymas su `backoff` mechanizmu
- Patobulinta žinutės formatavimo logika su JSON

### Ištaisyta:
- `assistant_ui.py` async funkcijų klaidos
- Testų neveikimas dėl `NoneType` grąžinimo
