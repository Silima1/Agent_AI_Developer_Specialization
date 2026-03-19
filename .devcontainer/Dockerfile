FROM mcr.microsoft.com/devcontainers/python:3.12

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Instala pacotes básicos úteis (opcional mas recomendado)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /workspace

# Copia arquivos do projeto
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip && \
    pip install litellm

# Comando padrão (opcional)
CMD ["python", "main.py"]