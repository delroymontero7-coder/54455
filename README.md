# BUNKER ELITE DEPLOY READY

Esta versión está preparada para desplegar directamente en Streamlit Cloud sin procesos en segundo plano obligatorios.

## Qué sí hace en deploy
- Login
- Scanner multi mercado
- Noticias
- Biblioteca PDF
- MELI
- Journal
- Stats
- Telegram
- Visual embebido
- Order flow modo fallback (si no hay feed externo, no rompe)

## Deploy
1. Sube todo el repo a GitHub.
2. En Streamlit Cloud selecciona `app.py`.
3. En Secrets pega:

```toml
[telegram]
bot_token = "TU_TOKEN"
chat_id = "TU_CHAT_ID"
[security]
password = "062711.M"
```

## Local
```bash
pip install -r requirements.txt
streamlit run app.py
```
