# ExercicioAPI2

## Docker

Para gerar a imagem:

```bash
docker build -t exercicioapi2 .
```

Para executar o container:

```bash
docker run --rm -p 8000:8000 exercicioapi2
```

A aplicação ficará disponível em `http://localhost:8000`.