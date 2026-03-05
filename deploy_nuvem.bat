@echo off
echo =========================================
echo ☁️ Iniciando Deploy para o Google Cloud...
echo =========================================

gcloud run deploy meu-app --source . --region us-central1 --allow-unauthenticated

echo.
echo ✅ Deploy finalizado com sucesso!
pause