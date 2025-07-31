class Aluno:
    """_summary_ Entidade Aluno

    Attributes:
        nome(str):nome completo do aluno
        matricula(str):identificador do aluno
        presencas(list):lista de string armaenando datas
    """
     
    def __init__(self, nome, matricula):
        
        self.nome = nome
        self.matricula = matricula
        self.presencas = []  # Lista para armazenar datas de presença

    def adicionar_presenca(self, data):
        """Registra  a presença de um aluno

        Args:
            data (str): Data da presença em formato string 'YYYY-MM-DD'.

        Returns:
            str: Mensagem de confirmação

        """
        if data not in self.presencas:
            self.presencas.append(data)
            return f"Presença registrada para {self.nome} em {data}."
        return f"Presença já registrada para {self.nome} em {data}."

    def consultar_frequencia(self):
        """Lista as frequencias

        Returns:
            str: Mensagem de confirmação

        """
        total_aulas = len(self.presencas)
        return f"Aluno {self.nome} (Matrícula: {self.matricula}) - Total de presenças: {total_aulas}"