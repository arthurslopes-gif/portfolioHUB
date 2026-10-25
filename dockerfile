# Usa a imagem oficial leve do Python 3.11
FROM python:3.11-slim

# Define o diretório de trabalho padrão dentro do contêiner
WORKDIR /app

# Garante que os prints e inputs do Python apareçam instantaneamente no terminal
ENV PYTHONUNBUFFERED=1

# Copia a pasta src para dentro do contêiner
COPY src/ /app/src/

# Comando padrão para rodar a sua aplicação CLI
CMD ["python", "src/main.py"]