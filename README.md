# ASCII Spinning Donut (Projeto DevOps)

Este projeto implementa a clássica animação do "Donut Giratório" (Rotating Donut) usando Python e Pygame. Ele serve como uma demonstração prática da aplicação de um ciclo de vida de software completo (DevOps), desde o versionamento até a entrega contínua.

---

## Stack Tecnológica e Conceitos de DevOps Aplicados

| Conceito | Ferramenta/Recurso | Descrição da Aplicação |
| :--- | :--- | :--- |
| **Containerização** | Docker, Dockerfile | O aplicativo é empacotado em uma imagem Docker (`carlosevan/ascii-spinning-donut`). |
| **CI/CD Pipeline** | GitHub Actions | Configuração de um fluxo de trabalho que automatiza o **Build** da imagem e o **Push** para o Container Registry a cada commit na `main`. |
| **Versionamento** | Commits Semânticos | Uso de prefixos (`feat:`, `chore:`, `ci:`, `refactor:`, `docs:`) para manter um histórico de commits limpo e significativo. |
| **Otimização de Build** | Docker Cache | O Pipeline utiliza o cache do Docker Registry para acelerar as construções futuras (`cache-from` e `cache-to`). |
| **Monitoramento** | Dependabot | Configurado para monitorar e propor Pull Requests (`chore:`) automáticos para atualizações de dependências do Python. |

---

## Como Rodar a Aplicação (Prova de Conceito)

Para rodar a aplicação, você só precisa ter o **Docker Desktop** instalado. O processo de *build* e *push* para o Container Registry já foi automatizado.

### 1. Puxar a Imagem

A imagem mais recente foi enviada pelo nosso Pipeline de CI/CD para o Docker Hub:

```bash
docker pull carlosevan/ascii-spinning-donut:latest

```
### 2. Para rodar pelo WSL, basta acessar o linux pelo terminal Powershell e executar o seguinte comando:

```Powershell
docker run -it --rm \
    --net=host \
    -e DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native \
    -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native \
    carlosevan/ascii-spinning-donut:latest

```
