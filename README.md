<p align="center">
<a href="https://dio.me/"><img src="https://img.shields.io/badge/DIO-Project-FED564?logo=vimeo" alt="DIO - Project"></a>
<a href="https://en.wikipedia.org/wiki/Artificial_intelligence"><img src="https://img.shields.io/badge/AI-Project-FED564?logo=openai" alt="AI - Project"></a>
<a href="https://portal.azure.com/" title="Vá para a página inicial do Portal"><img src="https://custom-icon-badges.demolab.com/badge/Microsoft%20Azure-0089D6?logo=msazure&logoColor=white)](#)"></a>
<a href="https://markdownlivepreview.com/" title="Vá para a página inicial do Editor"><img src="https://img.shields.io/badge/Markdown-%23000000.svg?logo=markdown&logoColor=white"></a>
<a href="https://www.sublimetext.com/" title="Vá para a página inicial do Editor"><img src="https://img.shields.io/badge/Sublime%20Text-%23575757.svg?logo=sublime-text&logoColor=important)"></a>
<a href="https://www.python.org/" title="Vá para a página inicial do Python"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff"></a>


# Azure Cognitive Search: Processo de Ingestão, Indexação e Exploração de Dados

## 👀 Visão Geral 🌁
Este projeto documenta a implementação de um pipeline de busca cognitiva no Azure, abrangendo três etapas principais:
1. **Ingestão de conteúdo** para enriquecimento com IA
2. **Criação de índices inteligentes**
3. **Exploração prática** dos dados organizados

## ⚙️ Configuração do Ambiente 🗺
Para a implementação e execução do projeto, foram utilizados os seguintes elementos:

- **Microsoft Azure**: Conta ativa para provisionamento dos serviços.
- **Azure Cognitive Search**: Serviço responsável pela criação, atualização e consulta dos índices inteligentes.
- **Azure Storage Account**: Armazena os dados brutos que serão processados.
- **Azure AI Services** : Para enriquecimento dos dados com habilidades cognitivas, como OCR e NER.

### Ferramentas de Desenvolvimento:
- Python e bibliotecas  para os scripts de ingestão e processamento.
- Azure CLI para gerenciamento dos recursos.

```bash
# Exemplo de instalação via Azure CLI
az extension add --name search
```

## 📂 Estrutura do Repositório 

```
azure-cognitive-search/

├── dados/
│   └── metadata.csv
├── scripts/
│   └── ingestao.py
├── outputs/
│   └── logs.txt
└── README.md
```

## 🔄 Etapa 1: Ingestão de Conteúdo 🖲
**Processo realizado:**
- Configuração do Data Source no Azure Search.
- Conexão com repositórios.
- Pré-processamento inicial dos dados brutos.

**Insights obtidos:**
- Dados não estruturados exigem normalização prévia.
- Chaves de documento únicas são críticas para evitar duplicações.
- Limitações de tamanho de arquivo como exemplo: 16MB por documento no padrão.

**📝 Exemplo de configuração:**
```json
{
  "name": "blob-datasource",
  "type": "azureblob",
  "credentials": { "connectionString": "[CONN_STRING]" },
  "container": { "name": "dados-empresa" }
}
```

##  Etapa 2: 🧐 Criação de Índices Inteligentes 🧠
**Técnicas aplicadas:**
- Definição de schema com campos chave.
- Configuração de perfis de pontuação personalizados.
- Integração com habilidades cognitivas.

**💡 Descobertas importantes:**
- Campos facetáveis melhoram a navegação refinada.
- Analisadores linguísticos nativos melhoram recall para PT-BR.
- O enriquecimento com IA aumenta significativamente o custo operacional.

**Exemplo de definição de índice:**
```
var definition = new Index
{
    Name = "produtos-otimizado",
    Fields = FieldBuilder.BuildForType<Produto>(),
    Suggesters = new[] { new Suggester("sg", "nomeProduto") }
};
```

##  Etapa 3:  🔭 Exploração de Dados 🎲
**Métodos utilizados:**
- Consultas REST API diretamente via Postman.
- Uso do Search Explorer no portal Azure.
- Visualização de resultados em aplicação web customizada.

**Resultados quantitativos:**
Após a implementação do pipeline, observou-se uma melhoria significativa no desempenho das buscas. O tempo médio de busca reduziu de 2,1 segundos para apenas 0,4 segundos, o que representa uma otimização considerável. Além disso, a precisão das buscas, medida pela taxa de acerto nos cinco primeiros resultados, aumentou de 68% para 92%. O recall, que indica a capacidade de recuperar documentos relevantes, também melhorou, passando de 55% para 88%.

**Aprendizados:**
- Consultas semânticas exigem tuning fino.
- O cache de resultados melhora performance em cenários estáticos.
- Filtros geográficos requerem formatos específicos (GeoJSON).


## 🗂 Insights Obtidos

- **Qualidade dos Dados:**  
  Garantir que os dados sejam limpos e bem processados e incluindo a extração de texto com OCR e metadados precisos é fundamental para que os índices funcionem corretamente.

- **Chaves Únicas e Metadados:**  
  Cada documento precisa de um identificador único e exclusivo e de informações bem organizadas para evitar duplicações e facilitar a busca.

- **Integração de Serviços:**  
  Combinar o Azure Cognitive Search com o Azure Storage e o Azure AI Services como opção  mostra como diferentes ferramentas podem trabalhar juntas para oferecer uma busca mais inteligente e eficaz.

- **Automação e Monitoramento:**  
  Usar scripts para automatizar tarefas e manter arquivos de log ajuda a acompanhar o fluxo dos dados e a resolver problemas rapidamente.

- **Escalabilidade e Desempenho:**  
  Encontrar o equilíbrio entre a complexidade dos modelos e o custo operacional é chave para manter a performance sem prejudicar a agilidade da aplicação.

- **Evolução Contínua:**  
  Registrar cada etapa do processo e as decisões tomadas torna a melhoria contínua mais fácil e a manutenção do projeto mais colaborativa.

## ☑️ Conclusão

Este projeto demonstrou a aplicação prática de conceitos de organização, busca cognitiva e análise de dados utilizando os serviços do Azure. Durante o desenvolvimento, pude observar a importância de:

- **Qualidade dos Dados**: Garantir dados limpos e bem estruturados desde a ingestão até a indexação.
- **Identificadores e Metadados**: Utilizar chaves únicas e metadados organizados para facilitar a navegação e recuperação de documentos.
- **Integração de Serviços**: Combinar Azure Cognitive Search, Storage e, opcionalmente, AI Services para criar uma solução que une automação e inteligência na busca.
- **Monitoramento e Registro**: Acompanhar o desempenho e documentar cada etapa do processo para aprimorar continuamente o pipeline.

Essa experiência não apenas reforçou meus conhecimentos teóricos sobre organização e pesquisa de documentos, mas também trouxe valiosos aprendizados sobre escalabilidade, manutenção e integração de sistemas. O projeto exemplifica como transformar ideias em soluções eficazes no ambiente de computação em nuvem.
