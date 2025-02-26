<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com///compare/87659d3f84c493e38a5647edcaeea6deaecdb131...0.1.0) (2025-02-26)

### Features

- add parameters_embedder function for setting hyperparameters and API key validation ([da5e4bc](https://github.com///commit/da5e4bcbf471cbe79f8b082ba27158f9dbdba769))
- add Embedder class for OpenAI embeddings API integration ([52fb282](https://github.com///commit/52fb282fafbfff3cdda01aae18ac262ae6c519bd))
- add embedder page to layout with corresponding title and icon ([9318a5c](https://github.com///commit/9318a5c26c1712e435ae42144a5804dba4652d23))
- add embedder functionality with API key validation and text embedding ([4c3c53a](https://github.com///commit/4c3c53aef8076ca9897e938c3143ac4a76871d20))
- update chatbot functionality to use parameters_opener and add error handling for invalid API keys ([0a0d5d7](https://github.com///commit/0a0d5d7e48d947093b1e6cdffe236be04b7d516e))
- add PCA dimension reduction and 2D scatter plot functionality ([1d3846c](https://github.com///commit/1d3846c1296f681d061963ec6ea1179014991469))
- enhance chatbot functionality with API key validation and chat history management ([07a13df](https://github.com///commit/07a13df475d49856c45c052864d12505f3633843))
- implement API key validation and YAML configuration loading in tools.py ([4d7c917](https://github.com///commit/4d7c9175ea6ca5f8952a679c2304fdbefa9301dc))
- add pyyaml to requirements for enhanced YAML support ([9177d8c](https://github.com///commit/9177d8c94825c8e8758cea4b96750b840a378524))
- update model selection in chat completion to use dynamic model variable ([102287e](https://github.com///commit/102287e04b8c00c9c80978b658ea2bd2c50d060e))
- import parameters from utilis.tools for model configuration ([1a56dc8](https://github.com///commit/1a56dc87fc3d55760a5cb2438d49116cef0d9f5c))
- add configuration for OpenAI and DeepSeek system content with temperature settings ([3eb6808](https://github.com///commit/3eb68088758aca93dc293a4b6d885b877ab2bd35))
- integrate pages layout function into main execution flow ([de0c3f7](https://github.com///commit/de0c3f74fe18061596157a6200c6e11936a7f8b0))
- enhance home page with instructions and GitHub link for OpenAI model access ([336d02d](https://github.com///commit/336d02d9db73ead37ebbd144ec5f2a9e991b14e6))
- implement pages layout function for sidebar navigation ([afbfec9](https://github.com///commit/afbfec92b520f64518e8f7684e55adfff00f4153))
- add opener function and Opener class for OpenAI API integration ([640f6ad](https://github.com///commit/640f6ad6d328b2b02752ed8acf1c4da7721c50e3))
- add __init__.py file with initial main function and metadata ([7994db5](https://github.com///commit/7994db51c68084c865062e305e302726fb1c8fb4))
- add chatbot.py file with initial metadata and structure ([65a82fe](https://github.com///commit/65a82fe688ecd0699c0b3be2a516991f68e77585))
- add home.py file with initial metadata and structure ([e384643](https://github.com///commit/e384643e395a7f66e955a67024f13fbf84b5f019))
- add layout.py file with initial metadata and structure ([85fa7f4](https://github.com///commit/85fa7f490375f7f3c9899cff50e26fdef77a892a))
- add main.py file with initial main function structure ([a4113d7](https://github.com///commit/a4113d74fd697845bc59a3a7b595bdec946eeb08))
- add models.py file with initial structure and metadata ([78ead21](https://github.com///commit/78ead21d3b6ebdd3f74e9d6bb705b693acb5b677))
- add initial tools.py file with metadata ([7d19481](https://github.com///commit/7d194814ffb4c6a8f0275e9420b2ae4baf780618))

### Bug Fixes

- update tools.py to rename variables for clarity and handle three input parameters ([6cd474a](https://github.com///commit/6cd474ac03a76a381565f4f37f572773ac974a97))
- update embedder.py to handle three parameters and adjust scatter plot font size ([cccd4d2](https://github.com///commit/cccd4d2997a7534dc8b9a5c535dec95e35b7f359))
- update chart_plot.py to use 3D scatter plot and improve legend layout ([6e8eb96](https://github.com///commit/6e8eb96b815df935662accc8e6f70ec2ea4be609))
- update prompt variable in chatbot.py for correct API call ([c1a7fc0](https://github.com///commit/c1a7fc05f4495f0564d18e0f209a29a4bb7ed03f))
- remove duplicate empty_message initialization in chatbot.py ([b134ac1](https://github.com///commit/b134ac1a941fee9deee5336536e5d83c8d35e10c))

### Chore

- update PCALearnerDimensionsReducer to use 3 dimensions for PCA ([740bfdd](https://github.com///commit/740bfdd7bec6eff5e4b12325e2d978d3d9c5e755))
- add pyproject.toml for changelog configuration ([ccac9a1](https://github.com///commit/ccac9a17820383956916c665ca6e2d3e4ce3a1cd))

### Docs

- update CHANGELOG.md to include recent bug fixes ([c5af480](https://github.com///commit/c5af48035c76100d4fa10d50bbfe3e3af899ec57))
- update CHANGELOG.md to reflect recent changes and enhancements ([e2c75ac](https://github.com///commit/e2c75ac37d19de6eacd7241090a1a71add4e7965))
- update CHANGELOG.md to include recent feature additions and enhancements ([bf5eff2](https://github.com///commit/bf5eff2f4f2d97cd202ac74e35328b1d046b0821))
- update CHANGELOG.md to include recent enhancements and refactoring ([3c37abe](https://github.com///commit/3c37abe545c4d4adbd2a87a3ae41791dd6afc85a))
- update CHANGELOG.md with recent feature additions ([f64a51e](https://github.com///commit/f64a51e44f4afa615645c0a74e4eb713b610502e))
- add CHANGELOG.md with initial version 0.1.0 and feature list ([d686d5a](https://github.com///commit/d686d5a52fb5970e414689230ad1e5af9e79847b))
- add usage instructions and license information to README ([06a7f9b](https://github.com///commit/06a7f9b07697d4e480a37727d8e080368bb941cc))
- add requirements file with essential dependencies ([000ce17](https://github.com///commit/000ce17c1dac652b106e3ea90fbecbee632c1fa4))

### Code Refactoring

- remove unused import from tools.py ([f155a2e](https://github.com///commit/f155a2edc7efe8a9537264a785a60e1c5f7ff88c))

### Dependencies

- update requirements.txt with new dependencies for data processing and visualization ([548b064](https://github.com///commit/548b064cefc880028cfb11a96d289c2e3de5457c))

