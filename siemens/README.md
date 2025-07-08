Configuração do PLC Siemens para IMC-PID
	Este guia fornece instruções para implementar um controlador IMC-PID em um PLC Siemens usando o TIA Portal. O exemplo foi desenvolvido para os controladores S7-1200/S7-1500.

Passos para Implementação
	1. Criar um Novo Projeto no TIA Portal
	Abra o TIA Portal e crie um novo projeto.
	Selecione o controlador apropriado (S7-1200 ou S7-1500) e configure a rede.
	2. Configurar Bloco PID
	No navegador de projeto, adicione um novo bloco de organização (OB) ou bloco funcional (FB).
	Insira o código SCL do controlador IMC-PID fornecido em IMC_PID_Siemens.st.
	3. Definir Parâmetros
	Utilize a biblioteca de blocos para inserir um bloco PID (exemplo: PIDCompact).
	Configure os parâmetros Kp, Ti, Td de acordo com o código.
	4. Configurar Entradas e Saídas
	Certifique-se de que as variáveis PV_IN (Process Variable Input) e SP_INT (Set Point Input) estejam conectadas aos sinalizadores de entrada e saída desejados.
	Defina os limites de controle QM (saída máxima) e QN (saída mínima).
	5. Simulação e Validação
	Utilize a funcionalidade de simulação do TIA Portal para testar e validar a configuração antes da implementação no hardware real.
	Ajuste os parâmetros conforme necessário para otimizar o desempenho no ambiente simulado.
Considerações de Segurança
	Sempre realize testes em um ambiente simulado antes de aplicar no ambiente de produção.
	Certifique-se de que todas as normas de segurança relevantes sejam seguidas durante a implementação.
Recursos Adicionais
	Consulte a documentação oficial da Siemens para obter instruções detalhadas sobre o uso de blocos PID no TIA Portal.
	Instruções de Uso

Código SCL:
	IMC_PID_Siemens.st: Contém o exemplo de configuração do controlador IMC-PID que deve ser integrado ao TIA Portal.

Arquivo README.md:
	Fornece um guia passo a passo para configurar o PLC Siemens, definir parâmetros, simular e validar a implementação.

Precauções:
	Garantir que todas as configurações sejam testadas em ambiente simulado para evitar impactos em operações ao vivo.
