@echo off
echo =========================================
echo 🚀 Construindo a imagem Docker...
echo =========================================
docker build -t meu-app .

echo.
echo =========================================
echo 🟢 Subindo o container na porta 8080...
echo =========================================
docker run -d --name container-minha-ia -p 8080:8080 meu-app

echo.
echo ✅ Tudo pronto! Acesse: http://localhost:8080
pause