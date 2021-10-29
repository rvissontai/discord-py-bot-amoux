import random
import pyttsx3

from os import urandom
import requests
import json

class lerolero_service():
    def __init__(self):
        pass

    async def obter_frase_dilma(self):
        frases = [u"Eu, para ir, eu faço uma escala. Para voltar, eu faço duas, para voltar para o Brasil. Neste caso agora nós tínhamos uma discussão. Eu tinha que sair de Zurique, podia ir para Boston, ou pra Boston, até porque... vocês vão perguntar, mas é mais longe? Não é não, a Terra é curva, viu?",
                        u"É interessante que muitas vezes no Brasil, você é, como diz o povo brasileiro, muitas vezes você é criticado por ter o cachorro e, outras vezes, por não ter o mesmo cachorro. Esta é uma crítica interessante que acontece no Brasil",
                        u"E nós criamos um programa que eu queria falar para vocês, que é o Ciência sem Fronteiras. Por que eu queria falar do Ciência sem Fronteiras para vocês? É que em todas as demais... porque nós vamos fazer agora o Ciência sem Fronteiras 2. O 1 é o 100 000, mas vai ter de continuar fazendo Ciência sem Fronteiras no Brasil",
                        u"Eu dou dinheiro pra minha filha. Eu dou dinheiro pra ela viajar, então é... é... Já vivi muito sem dinheiro, já vivi muito com dinheiro. -Jornalista: Coloca esse dinheiro na poupança que a senhora ganha R$10 mil por mês. -Dilma: O que que é R$10 mil?",
                        u"A única área que eu acho, que vai exigir muita atenção nossa, e aí eu já aventei a hipótese de até criar um ministério. É na área de... Na área... Eu diria assim, como uma espécie de analogia com o que acontece na área agrícola.",
                        u"Primeiro eu queria cumprimentar os internautas. -Oi Internautas! Depois dizer que o meio ambiente é sem dúvida nenhuma uma ameaça ao desenvolvimento sustentável. E isso significa que é uma ameaça pro futuro do nosso planeta e dos nossos países. O desemprego beira 20%, ou seja, 1 em cada 4 portugueses.",
                        u"Se hoje é o dia das crianças... Ontem eu disse: o dia da criança é o dia da mãe, dos pais, das professoras, mas também é o dia dos animais, sempre que você olha uma criança, há sempre uma figura oculta, que é um cachorro atrás. O que é algo muito importante!",
                        u"Todos as descrições das pessoas são sobre a humanidade do atendimento, a pessoa pega no pulso, examina, olha com carinho. Então eu acho que vai ter outra coisa, que os médicos cubanos trouxeram pro brasil, um alto grau de humanidade.",
                        u"No meu xinélo da humildade eu gostaria muito de ver o Neymar e o Ganso. Por que eu acho que.... 11 entre 10 brasileiros gostariam. Você veja, eu já vi, parei de ver. Voltei a ver, e acho que o Neymar e o Ganso têm essa capacidade de fazer a gente olhar.",
                        u"A população ela precisa da Zona Franca de Manaus, porque na Zona franca de Manaus, não é uma zona de exportação, é uma zona para o Brasil. Portanto ela tem um objetivo, ela evita o desmatamento, que é altamente lucravito. Derrubar arvores da natureza é muito lucrativo!",
                        u"Ai você fala o seguinte: \"- Mas vocês acabaram isso?\" Vou te falar: -\"Não, está em andamento!\" Tem obras que \"vai\" durar pra depois de 2010. Agora, por isso, nós já não desenhamos, não começamos a fazer projeto do que nós \"podêmo fazê\"? 11, 12, 13, 14... Por que é que não?"
                        u"Eu queria destacar uma questão, que é uma questão que está afetando o Brasil inteiro, que é a questão da vigilância sanitária: gente, é o vírus Aedes aegypti, com as suas diferentes modalidades: chikungunya, zika vírus.",
                        u"A presidente falava sobre a distribuição de recursos explorados do pré-sal. “Não é 30% dos recursos da exploração [do pré-sal]. É 30% de 25%. Ou 30%… de 30%. Portanto, não é 30%. Está entre 7,5% e um pouco mais, 12,5%. Não se trata de 30%"];

        return random.choice(frases)

    async def obter_nova_frase(self):
        t0 = [  'Caros amigos, ',
        'Por outro lado, ',
        'Assim mesmo, ',
        'No entanto, não podemos esquecer que ',
        'Do mesmo modo, ',
        'A prática cotidiana prova que ',
        'Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ',
        'As experiências acumuladas demonstram que ',
        'Acima de tudo, é fundamental ressaltar que ',
        'O incentivo ao avanço tecnológico, assim como ',
        'Não obstante, ',
        'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ',
        'Pensando mais a longo prazo, ',
        'O que temos que ter sempre em mente é que ',
        'Ainda assim, existem dúvidas a respeito de como ',
        'Gostaria de enfatizar que ',
        'Todavia, ',
        'A nível organizacional, ',
        'O empenho em analisar ',
        'Percebemos, cada vez mais, que ',
        'No mundo atual, ',
        'É importante questionar o quanto ',
        'Neste sentido, ',
        'Evidentemente, ',
        'Por conseguinte, ',
        'É claro que ',
        'Podemos já vislumbrar o modo pelo qual ',
        'Desta maneira, ',
        'O cuidado em identificar pontos críticos n',
        'A certificação de metodologias que nos auxiliam a lidar com ' ]

        t1 = [	'a execução dos pontos do programa ',
        'a complexidade dos estudos efetuados ',
        'a contínua expansão de nossa atividade ',
        'a estrutura atual da organização ',
        'o novo modelo estrutural aqui preconizado ',
        'o desenvolvimento contínuo de distintas formas de atuação ',
        'a constante divulgação das informações ',
        'a consolidação das estruturas ',
        'a consulta aos diversos militantes ',
        'o início da atividade geral de formação de atitudes ',
        'o desafiador cenário globalizado ',
        'a mobilidade dos capitais internacionais ',
        'o fenômeno da Internet ',
        'a hegemonia do ambiente político ',
        'a expansão dos mercados mundiais ',
        'o aumento do diálogo entre os diferentes setores produtivos ',
        'a crescente influência da mídia ',
        'a necessidade de renovação processual ',
        'a competitividade nas transações comerciais ',
        'o surgimento do comércio virtual ',
        'a revolução dos costumes ',
        'o acompanhamento das preferências de consumo ',
        'o comprometimento entre as equipes ',
        'a determinação clara de objetivos ',
        'a adoção de políticas descentralizadoras ',
        'a valorização de fatores subjetivos ',
        'a percepção das dificuldades ',
        'o entendimento das metas propostas ',
        'o consenso sobre a necessidade de qualificação ',
        'o julgamento imparcial das eventualidades ' ]

        t2 = [  'nos obriga à análise ',
        'cumpre um papel essencial na formulação ',
        'exige a precisão e a definição ',
        'auxilia a preparação e a composição ',
        'garante a contribuição de um grupo importante na determinação ',
        'assume importantes posições no estabelecimento ',
        'facilita a criação ',
        'obstaculiza a apreciação da importância ',
        'oferece uma interessante oportunidade para verificação ',
        'acarreta um processo de reformulação e modernização ',
        'pode nos levar a considerar a reestruturação ',
        'representa uma abertura para a melhoria ',
        'ainda não demonstrou convincentemente que vai participar na mudança ',
        'talvez venha a ressaltar a relatividade ',
        'prepara-nos para enfrentar situações atípicas decorrentes ',
        'maximiza as possibilidades por conta ',
        'desafia a capacidade de equalização ',
        'agrega valor ao estabelecimento ',
        'é uma das consequências ',
        'promove a alavancagem ',
        'não pode mais se dissociar ',
        'possibilita uma melhor visão global ',
        'estimula a padronização ',
        'aponta para a melhoria ',
        'faz parte de um processo de gerenciamento ',
        'causa impacto indireto na reavaliação ',
        'apresenta tendências no sentido de aprovar a manutenção ',
        'estende o alcance e a importância ',
        'deve passar por modificações independentemente ',
        'afeta positivamente a correta previsão ' ]


        t3 = [  'das condições financeiras e administrativas exigidas.',
        'das diretrizes de desenvolvimento para o futuro.',
        'do sistema de participação geral.',
        'das posturas dos órgãos dirigentes com relação às suas atribuições.',
        'das novas proposições.',
        'das direções preferenciais no sentido do progresso.',
        'do sistema de formação de quadros que corresponde às necessidades.',
        'das condições inegavelmente apropriadas.',
        'dos índices pretendidos.',
        'das formas de ação.',
        'dos paradigmas corporativos.',
        'dos relacionamentos verticais entre as hierarquias.',
        'do processo de comunicação como um todo.',
        'dos métodos utilizados na avaliação de resultados.',
        'de todos os recursos funcionais envolvidos.',
        'dos níveis de motivação departamental.',
        'da gestão inovadora da qual fazemos parte.',
        'dos modos de operação convencionais.',
        'de alternativas às soluções ortodoxas.',
        'dos procedimentos normalmente adotados.',
        'dos conhecimentos estratégicos para atingir a excelência.',
        'do fluxo de informações.',
        'do levantamento das variáveis envolvidas.',
        'das diversas correntes de pensamento.',
        'do impacto na agilidade decisória.',
        'das regras de conduta normativas.',
        'do orçamento setorial.',
        'do retorno esperado a longo prazo.',
        'do investimento em reciclagem técnica.',
        'do remanejamento dos quadros funcionais.' ]

        frase = random.choice(t0)+random.choice(t1)+random.choice(t2)+random.choice(t3)

        return '`' + frase + '`'

