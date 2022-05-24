from helper.write_a_json import write_a_json
from pprintpp import pprint as pp
from db.database import Graph


class Naruto(object):
    def __init__(self):
        self.db = Graph(uri='bolt://34.239.104.135:7687',
                        user='neo4j', password='coxswains-wines-circumferences')

    def createArvoreGenealogicaNaruto(self):
        self.db.execute_query(
            "CREATE"
            "(:Alien:ProjenitoraDoChakra{nome:'Kaguya Otsutsuki',clan:'Otsutsuki',poder:['Rinne-Sharingan,Byakugan']}),"
            "(:Alien:SabioDosSeisCaminhos{nome:'Hagoromo Otsutsuki',clan:'Otsutsuki',poder:['Rinnegan','Sharingan']}),"
            "(:Alien:AncestralClanHyuga{nome:'Hamura Otsutsuki',clan:'Otsutsuki',poder:['Tenseigan','Byakugan']}),"
            "(:Ninja:AncestralClanUchiha{nome:'Indra Otsutsuki',clan:'Otsutsuki',poder:['Mangekyo Sharingan','Sharingan']}),"
            "(:Ninja:AncestralClanSenju{nome:'Ashura Otsutsuki',clan:'Otsutsuki',poder:'Estilo Madeira'}),"
            "(:Ninja:Medica{nome:'Sakura Haruno',clan:'Haruno',poder:'Byakugo no Jutsu'}),"
            "(:Ninja:HokageDasSombras{nome:'Sasuke Uchiha',clan:'Uchiha',poder:['Rinnegan Supremo','Mangekyo Sharingan Eterno','Sharingan']}),"
            "(:Ninja:Kunoichi{nome:'Sarada Uchiha',clan:['Uchiha','Haruno'],poder:'Sharingan'}),"
            "(:Ninja:PrincesaDoByakugan{nome:'Hinata Hyuga',clan:'Hyuga',poder:'Byakugan'}),"
            "(:Ninja:Hokage{nome:'Naruto Uzumaki',clan:'Uzumaki',poder:['Modo Kyubi','Modo Sabio','Modo Barion']}),"
            "(:Ninja:Kunoichi{nome:'Himawari Uzumaki',clan:['Uzumaki','Hyuga'],poder:'Byakugan'}),"
            "(:Ninja:Shinobi{nome:'Boruto Uzumaki',clan:['Uzumaki','Hyuga'],poder:['Karma','Jougan']})"
            )

    def createRelacionamento(self):
        self.db.execute_query(
            "MATCH"
            "(k:Alien:ProjenitoraDoChakra{nome:'Kaguya Otsutsuki'}),"
            "(h1:Alien:SabioDosSeisCaminhos{nome:'Hagoromo Otsutsuki'}),"
            "(h2:Alien:AncestralClanHyuga{nome:'Hamura Otsutsuki'}),"
            "(i:Ninja:AncestralClanUchiha{nome:'Indra Otsutsuki'}),"
            "(a:Ninja:AncestralClanSenju{nome:'Ashura Otsutsuki'}),"
            "(s1:Ninja:Medica{nome:'Sakura Haruno'}),"
            "(s2:Ninja:HokageDasSombras{nome:'Sasuke Uchiha'}),"
            "(s3:Ninja:Kunoichi{nome:'Sarada Uchiha'}),"
            "(h3:Ninja:PrincesaDoByakugan{nome:'Hinata Hyuga'}),"
            "(n:Ninja:Hokage{nome:'Naruto Uzumaki'}),"
            "(h4:Ninja:Kunoichi{nome:'Himawari Uzumaki'}),"
            "(b:Ninja:Shinobi{nome:'Boruto Uzumaki'})"
            "CREATE"
            "(k)-[:MAE_DE]->(h1),(k)-[:MAE_DE]->(h2),"
            "(h1)-[:PAI_DE]->(i),(h1)-[:PAI_DE]->(a),"
            "(s1)-[:MAE_DE]->(s3),(s2)-[:PAI_DE]->(s3),"
            "(h3)-[:MAE_DE]->(h4),(h3)-[:MAE_DE]->(b),(n)-[:PAI_DE]->(h4),(n)-[:PAI_DE]->(b),"
            "(s1)-[:CASADA_COM]->(s2),(h3)-[:CASADA_COM]->(n),"
            "(h1)-[:IRMAO_DE{tipo:'Gemeo'}]->(h2),(i)-[:IRMAO_DE]->(a),(h4)-[:IRMA_DE]->(b),"
            "(n)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s2),(n)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s1),(s2)-[:AMIGO_DE{tipo:'Equipe 7'}]->(s1),"
            "(s3)-[:AMIGA_DE]->(b),"
            "(n)-[:DESCENDENTE_DE]->(a),(s2)-[:DESCENDENTE_DE]->(i),(h3)-[:DESCENDENTE_DE]->(h2)"
        )

    def pergunta1(self):
        return self.db.execute_query(
            "MATCH"
            "(n:Alien)"
            "RETURN n.nome"
        )

    def pergunta2(self):
        return self.db.execute_query(
            "MATCH"
            "(:Ninja:HokageDasSombras{nome:'Sasuke Uchiha'})-[:DESCENDENTE_DE]->(n)"
            "RETURN n.nome"
        )

    def pergunta3(self):
        return self.db.execute_query(
            "MATCH"
            "(:Ninja:Hokage{nome:'Naruto Uzumaki'})-[:PAI_DE]->(n)"
            "RETURN n.nome"
        )

    def delete(self):
        self.db.execute_query("MATCH(n) DETACH DELETE n;")

def divider():
    print('\n' + '-' * 80 + '\n')

n = Naruto()
n.delete()
n.createArvoreGenealogicaNaruto()
n.createRelacionamento()

while 1:    
    option = input('Escolha uma pergunta!\n1. Quem do Anime Naruto é Alien?\n2. Sasuke Uchiha é descendente de quem?\n3. Naruto Uzumaki é pai de quem?\n4. sair\n\n')

    if option == '1':
        write_a_json(n.pergunta1(), "Perguta 1")
        pp(n.pergunta1())
        divider()

    elif option == '2':
        write_a_json(n.pergunta2(), "Perguta 2")
        pp(n.pergunta2())
        divider()

    elif option == '3':
        write_a_json(n.pergunta3(), "Perguta 3")
        pp(n.pergunta3())
        divider()

    elif option == '4':
        print("THANK YOU, SEE YOU LATER :)")
        divider()
        break

    else:
        print("Opção Inválida!")

n.db.close()