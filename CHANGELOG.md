# CHANGELOG
## [2.05.03+20250813(063)] - 2025-08-13
* dodano zabezpieczenie year < 2000
* restart na komendę `mqttloggercommands`
* poprawiono logowanie do plików (końce linii)
* poprawiono logowanie do plików (append, a nie overwrite)
## [2.03.03+20250808(061)] - 2025-08-08
* dodano więcej informacji debugowych zapisywanych do pliku
* poprawiono definicję docker compose oraz adres do docker container registry
* naprawić przecinki i średniki - separatorem jest teraz ";" a nie ","
* miejsce gdzie zapisują się dane - to wynika z docker compose
## [2.02.03+20250721(058)] - 2025-07-21
* dodano obsługe plików CSV
* poprawiono formatowanie daty
* poprawiono logowanie białych znaków

# TODO:
* podział na pliki po 100MB
* poprawić pierwsze niepełne wadomości
* poprawić non-ascii znaki w wiadomościach
* lista śledzonych topicow
* wykryć datę 1970!