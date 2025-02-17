# APS ir Kliento AI Asistentų Struktūra

Šis dokumentas aprašo APS (Autonominės Projektų Sistemos) ir kliento AI asistentų struktūrą, 
bei nustato aiškią terminologiją ir tag’ų sistemą.

## Tag’ų sistema
#APS_core (Tavo APS)
 ├── #APS_client_manager (priima užsakymą iš X)
 │    ├── #APS_project_manager (sukuria naują projektą)
 │    │    ├── #APS_strategy (sudaro strategiją)
 │    │    ├── #APS_model_selection (parenka AI modelius)
 │    │    ├── #APS_testing (testuoja projektą)
 │    │    ├── #APS_delivery (pateikia rezultatą užsakovui X)
 │
 ├── #CL_client (užsakovas X)
 │    ├── #CL_project (AI asistento kūrimo procesas)
 │    │    ├── #CL_strategy (kliento užduoties strategija)
 │    │    ├── #CL_agent (sukurtas AI asistentas)
 │    │    ├── #CL_testing (galutiniai AI asistento testai)
 │    │    ├── #CL_delivery (paruošta AI asistento versija)


## AI Asistentų hierarchija pagal tag’us

Toliau pateikiama hierarchinė APS ir kliento AI asistento struktūra:

```
#APS_core (Tavo APS)
 ├── #APS_client_manager (priima užsakymą iš X)
 │    ├── #APS_project_manager (sukuria naują projektą)
 │    │    ├── #APS_strategy (sudaro strategiją)
 │    │    ├── #APS_model_selection (parenka AI modelius)
 │    │    ├── #APS_testing (testuoja projektą)
 │    │    ├── #APS_delivery (pateikia rezultatą užsakovui X)
 │
 ├── #CL_client (užsakovas X)
 │    ├── #CL_project (AI asistento kūrimo procesas)
 │    │    ├── #CL_strategy (kliento užduoties strategija)
 │    │    ├── #CL_agent (sukurtas AI asistentas)
 │    │    ├── #CL_testing (galutiniai AI asistento testai)
 │    │    ├── #CL_delivery (paruošta AI asistento versija)
```

