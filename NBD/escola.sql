-- ============================================
-- SISTEMA ESCOLAR - VERSÃO CORRIGIDA
-- ============================================

DROP DATABASE IF EXISTS escola;
CREATE DATABASE escola;
USE escola;

-- ============================================
-- TABELAS
-- ============================================

CREATE TABLE professores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
) ENGINE=InnoDB;

CREATE TABLE disciplinas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    professor_id INT NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores(id) ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE cursos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    serie VARCHAR(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    curso_id INT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE avaliacoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    bimestre INT NOT NULL,
    media DECIMAL(5, 2),
    UNIQUE (aluno_id, disciplina_id, bimestre),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE,
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- INSERIR 50 PROFESSORES (suficientes para as disciplinas)
-- ============================================

INSERT INTO professores (nome, email) VALUES
('Dr. Carlos Mendes', 'carlos.mendes@escola.com'),
('Dra. Ana Silva', 'ana.silva@escola.com'),
('Prof. Roberto Santos', 'roberto@escola.com'),
('Profa. Juliana Costa', 'juliana@escola.com'),
('Prof. Pedro Oliveira', 'pedro.oliveira@escola.com'),
('Profa. Marina Gomes', 'marina.gomes@escola.com'),
('Prof. Lucas Ferreira', 'lucas.ferreira@escola.com'),
('Profa. Beatriz Lima', 'beatriz.lima@escola.com'),
('Prof. Fernando Castro', 'fernando.castro@escola.com'),
('Profa. Patricia Moura', 'patricia.moura@escola.com'),
('Prof. Ricardo Alves', 'ricardo.alves@escola.com'),
('Profa. Camila Rocha', 'camila.rocha@escola.com'),
('Prof. Gustavo Perez', 'gustavo.perez@escola.com'),
('Profa. Isabella Martins', 'isabella.martins@escola.com'),
('Prof. Thiago Dias', 'thiago.dias@escola.com'),
('Profa. Fernanda Barbosa', 'fernanda.barbosa@escola.com'),
('Prof. Alexandre Santos', 'alexandre.santos@escola.com'),
('Profa. Leticia Cardoso', 'leticia.cardoso@escola.com'),
('Prof. Marcelo Teixeira', 'marcelo.teixeira@escola.com'),
('Profa. Sophia Rezende', 'sophia.rezende@escola.com'),
('Prof. Felipe Nunes', 'felipe.nunes@escola.com'),
('Profa. Larissa Mendonca', 'larissa.mendonca@escola.com'),
('Prof. Wagner Costa', 'wagner.costa@escola.com'),
('Profa. Natalia Pinto', 'natalia.pinto@escola.com'),
('Prof. Cristiano Ribeiro', 'cristiano.ribeiro@escola.com'),
('Profa. Vanessa Sousa', 'vanessa.sousa@escola.com'),
('Prof. Bruno Herrera', 'bruno.herrera@escola.com'),
('Profa. Adriana Monteiro', 'adriana.monteiro@escola.com'),
('Prof. Fabio Salazar', 'fabio.salazar@escola.com'),
('Profa. Renata Vieira', 'renata.vieira@escola.com'),
('Prof. Sergio Duarte', 'sergio.duarte@escola.com'),
('Profa. Gabriela Rios', 'gabriela.rios@escola.com'),
('Prof. Otavio Lourenço', 'otavio.lourenco@escola.com'),
('Profa. Victoria Delgado', 'victoria.delgado@escola.com'),
('Prof. Raul Fonseca', 'raul.fonseca@escola.com'),
('Profa. Tatiana Luz', 'tatiana.luz@escola.com'),
('Prof. Davi Azevedo', 'davi.azevedo@escola.com'),
('Profa. Priscila Gama', 'priscila.gama@escola.com'),
('Prof. Leandro Rocha', 'leandro.rocha@escola.com'),
('Profa. Yasmin Soares', 'yasmin.soares@escola.com'),
('Prof. Julio Cesar', 'julio.cesar@escola.com'),
('Profa. Milena Braga', 'milena.braga@escola.com'),
('Prof. Vitor Leal', 'vitor.leal@escola.com'),
('Profa. Elisa Franco', 'elisa.franco@escola.com'),
('Prof. Romulo Neves', 'romulo.neves@escola.com'),
('Profa. Simone Aguiar', 'simone.aguiar@escola.com'),
('Prof. Emilio Moraes', 'emilio.moraes@escola.com'),
('Profa. Lorena Ferraz', 'lorena.ferraz@escola.com'),
('Prof. Damiao Olivares', 'damiao.olivares@escola.com'),
('Profa. Neuza Paiva', 'neuza.paiva@escola.com'),
('Prof. Cesario Leite', 'cesario.leite@escola.com');

-- ============================================
-- INSERIR 100 DISCIPLINAS (professor_id 1-50, distribuídas)
-- ============================================

INSERT INTO disciplinas (nome, professor_id) VALUES
('Matemática I', 1), ('Matemática II', 2), ('Português I', 3), ('Português II', 4),
('Física I', 5), ('Física II', 6), ('Química I', 7), ('Química II', 8),
('Biologia I', 9), ('Biologia II', 10), ('História I', 11), ('História II', 12),
('Geografia I', 13), ('Geografia II', 14), ('Inglês I', 15), ('Inglês II', 16),
('Espanhol', 17), ('Artes', 18), ('Educação Física', 19), ('Informática', 20),
('Filosofia', 21), ('Sociologia', 22), ('Economia', 23), ('Direito', 24),
('Psicologia', 25), ('Antropologia', 26), ('Estatística', 27), ('Lógica', 28),
('Geometria', 29), ('Álgebra', 30), ('Cálculo I', 31), ('Cálculo II', 32),
('Trigonometria', 33), ('Probabilidade', 34), ('Análise Combinatória', 35), ('Teoria dos Números', 36),
('Astronomia', 37), ('Óptica', 38), ('Termodinâmica', 39), ('Mecânica Clássica', 40),
('Eletromagnetismo', 41), ('Ondulatória', 42), ('Termologia', 43), ('Acústica', 44),
('Dinâmica', 45), ('Estática', 46), ('Cinemática', 47), ('Hidráulica', 48),
('Pneumática', 49), ('Reações Químicas', 1), ('Ácidos e Bases', 2), ('Ligações Químicas', 3),
('Tabela Periódica', 4), ('Estequiometria', 5), ('Soluções', 6), ('Equilíbrio Químico', 7),
('Oxidação e Redução', 8), ('Química Orgânica I', 9), ('Química Orgânica II', 10), ('Bioquímica', 11),
('Genética', 12), ('Evolução', 13), ('Ecologia', 14), ('Citologia', 15),
('Botânica', 16), ('Zoologia', 17), ('Microbiologia', 18), ('Anatomia', 19),
('Fisiologia', 20), ('Imunologia', 21), ('Farmacologia', 22), ('Patologia', 23),
('Idade Média', 24), ('Renascença', 25), ('Iluminismo', 26), ('Revolução Francesa', 27),
('Independência Brasileira', 28), ('Império Brasileiro', 29), ('República Velha', 30), ('Era Vargas', 31),
('Ditadura Militar', 32), ('Redemocratização', 33), ('Descobertas Geográficas', 34), ('Colonização Americana', 35),
('Capitalismo', 36), ('Socialismo', 37), ('Globalização', 38), ('Geopolítica', 39),
('Clima e Vegetação', 40), ('Hidrografia', 41), ('Solos', 42), ('Cartografia', 43),
('Urbanização', 44), ('Agricultura', 45), ('Indústria', 46), ('Tecnologia da Informação', 47),
('Programação', 48), ('Redes de Computadores', 49), ('Segurança da Informação', 50), ('Banco de Dados', 1);

-- ============================================
-- INSERIR 100 CURSOS
-- ============================================

INSERT INTO cursos (nome, serie) VALUES
('1A', '1º ano'), ('1B', '1º ano'), ('1C', '1º ano'), ('1D', '1º ano'), ('1E', '1º ano'),
('2A', '2º ano'), ('2B', '2º ano'), ('2C', '2º ano'), ('2D', '2º ano'), ('2E', '2º ano'),
('3A', '3º ano'), ('3B', '3º ano'), ('3C', '3º ano'), ('3D', '3º ano'), ('3E', '3º ano'),
('4A', '4º ano'), ('4B', '4º ano'), ('4C', '4º ano'), ('4D', '4º ano'), ('4E', '4º ano'),
('5A', '5º ano'), ('5B', '5º ano'), ('5C', '5º ano'), ('5D', '5º ano'), ('5E', '5º ano'),
('6A', '6º ano'), ('6B', '6º ano'), ('6C', '6º ano'), ('6D', '6º ano'), ('6E', '6º ano'),
('7A', '7º ano'), ('7B', '7º ano'), ('7C', '7º ano'), ('7D', '7º ano'), ('7E', '7º ano'),
('8A', '8º ano'), ('8B', '8º ano'), ('8C', '8º ano'), ('8D', '8º ano'), ('8E', '8º ano'),
('9A', '9º ano'), ('9B', '9º ano'), ('9C', '9º ano'), ('9D', '9º ano'), ('9E', '9º ano'),
('10A', '10º ano'), ('10B', '10º ano'), ('10C', '10º ano'), ('10D', '10º ano'), ('10E', '10º ano'),
('11A', '11º ano'), ('11B', '11º ano'), ('11C', '11º ano'), ('11D', '11º ano'), ('11E', '11º ano'),
('12A', '12º ano'), ('12B', '12º ano'), ('12C', '12º ano'), ('12D', '12º ano'), ('12E', '12º ano'),
('TI-A', 'Técnico'), ('TI-B', 'Técnico'), ('TI-C', 'Técnico'), ('TI-D', 'Técnico'), ('TI-E', 'Técnico'),
('ADM-A', 'Técnico'), ('ADM-B', 'Técnico'), ('ADM-C', 'Técnico'), ('ADM-D', 'Técnico'), ('ADM-E', 'Técnico'),
('ENG-A', 'Técnico'), ('ENG-B', 'Técnico'), ('ENG-C', 'Técnico'), ('ENG-D', 'Técnico'), ('ENG-E', 'Técnico'),
('MAQ-A', 'Técnico'), ('MAQ-B', 'Técnico'), ('MAQ-C', 'Técnico'), ('MAQ-D', 'Técnico'), ('MAQ-E', 'Técnico'),
('ELE-A', 'Técnico'), ('ELE-B', 'Técnico'), ('ELE-C', 'Técnico'), ('ELE-D', 'Técnico'), ('ELE-E', 'Técnico'),
('CON-A', 'Técnico'), ('CON-B', 'Técnico'), ('CON-C', 'Técnico'), ('CON-D', 'Técnico'), ('CON-E', 'Técnico');

-- ============================================
-- INSERIR 100 ALUNOS
-- ============================================

INSERT INTO alunos (nome, curso_id) VALUES
('João Silva', 1), ('Maria Santos', 1), ('Carlos Oliveira', 2), ('Ana Costa', 2),
('Pedro Gomes', 3), ('Fernanda Pereira', 3), ('Lucas Martins', 4), ('Juliana Rocha', 4),
('Bruno Alves', 5), ('Camila Souza', 5), ('Ricardo Dias', 6), ('Isabella Mendes', 6),
('Thiago Santos', 7), ('Beatriz Lima', 7), ('Felipe Castro', 8), ('Natalia Ferreira', 8),
('Gustavo Ribeiro', 9), ('Sofia Barbosa', 9), ('Fabio Teixeira', 10), ('Larissa Pinto', 10),
('Marcelo Duarte', 11), ('Vanessa Moura', 11), ('Diego Monteiro', 12), ('Patricia Neves', 12),
('Sergio Lourenço', 13), ('Leticia Gama', 13), ('Roberto Couto', 14), ('Simone Paiva', 14),
('Fernando Luz', 15), ('Yasmin Reis', 15), ('Alexandre Braga', 16), ('Elisa Franco', 16),
('Wagner Leal', 17), ('Lorena Olivares', 17), ('Cristiano Moraes', 18), ('Neuza Aguiar', 18),
('Raul Ferraz', 19), ('Cleuza Sousa', 19), ('Emilio Leite', 20), ('Odete Paes', 20),
('Benilson Gomes', 21), ('Morgana Mendes', 21), ('Euzebio Rosa', 22), ('Penelope Silva', 22),
('Feliciano Vargas', 23), ('Rosilda Lopes', 23), ('Gilson Couto', 24), ('Solange Ramos', 24),
('Heitor Barros', 25), ('Terezinha Prado', 25), ('Idalberto Brito', 26), ('Urania Mota', 26),
('Jarmo Muniz', 27), ('Veronica Santos', 27), ('Karlos Teles', 28), ('Wanda Nunes', 28),
('Leobino Franco', 29), ('Xuân Tran', 29), ('Mirko Petrov', 30), ('Yulia Ivanova', 30),
('Zsolt Nagy', 31), ('Alma Voss', 31), ('Bogdan Kowalski', 32), ('Cristina Baciu', 32),
('Dragan Antic', 33), ('Elvira Novak', 33), ('Florian Koss', 34), ('Greta Richter', 34),
('Henrik Sjoland', 35), ('Ingrid Larsen', 35), ('Jozef Varga', 36), ('Katarina Kovacs', 36),
('Ladislav Mraz', 37), ('Margot Dupont', 37), ('Nikolai Volkov', 38), ('Olga Smirnov', 38),
('Pavel Petrov', 39), ('Quirina Rossi', 39), ('Rupert Mann', 40), ('Sigrid Bergman', 40),
('Tomas Kucera', 41), ('Ulrika Johansson', 41), ('Viktor Sokolov', 42), ('Waltraud Hoffmann', 42),
('Xander Müller', 43), ('Yvonne Schmidt', 43), ('Zeno Wagner', 44), ('Antonia Fischer', 44),
('Baltazar König', 45), ('Constanza Berger', 45), ('Dagmar Hoffmann', 46), ('Erasmus Weber', 46),
('Fiona Schulz', 47), ('Gerson Schneider', 47), ('Hilária Neumann', 48), ('Ivan Krüger', 48),
('Jasmine Stein', 49), ('Klaus Schmidt', 49), ('Leonie Hoffmann', 50), ('Manfred Krämer', 50);

-- ============================================
-- INSERIR 100 AVALIAÇÕES
-- ============================================

INSERT INTO avaliacoes (aluno_id, disciplina_id, bimestre, media) VALUES
(1, 1, 1, 8.5), (1, 2, 1, 7.8), (2, 1, 1, 9.2), (2, 3, 1, 8.1),
(3, 4, 1, 7.5), (3, 5, 1, 8.9), (4, 6, 1, 7.2), (4, 7, 1, 8.6),
(5, 8, 1, 9.1), (5, 9, 1, 7.9), (6, 10, 1, 8.3), (6, 11, 1, 8.7),
(7, 12, 1, 7.6), (7, 13, 1, 9.0), (8, 14, 1, 8.4), (8, 15, 1, 7.7),
(9, 16, 1, 8.8), (9, 17, 1, 7.4), (10, 18, 1, 9.3), (10, 19, 1, 8.2),
(11, 20, 1, 7.9), (11, 21, 1, 8.5), (12, 22, 1, 8.1), (12, 23, 1, 9.2),
(13, 24, 1, 7.8), (13, 25, 1, 8.6), (14, 26, 1, 9.0), (14, 27, 1, 7.3),
(15, 28, 1, 8.7), (15, 29, 1, 8.4), (16, 30, 1, 7.5), (16, 31, 1, 9.1),
(17, 32, 1, 8.2), (17, 33, 1, 7.9), (18, 34, 1, 8.8), (18, 35, 1, 8.0),
(19, 36, 1, 9.3), (19, 37, 1, 7.6), (20, 38, 1, 8.5), (20, 39, 1, 8.3),
(1, 1, 2, 8.7), (1, 2, 2, 8.1), (2, 1, 2, 9.0), (2, 3, 2, 8.4),
(3, 4, 2, 7.8), (3, 5, 2, 9.0), (4, 6, 2, 7.5), (4, 7, 2, 8.8),
(5, 8, 2, 9.2), (5, 9, 2, 8.2), (6, 10, 2, 8.5), (6, 11, 2, 8.9),
(7, 12, 2, 7.9), (7, 13, 2, 9.1), (8, 14, 2, 8.6), (8, 15, 2, 8.0),
(9, 16, 2, 8.9), (9, 17, 2, 7.7), (10, 18, 2, 9.4), (10, 19, 2, 8.5),
(11, 20, 2, 8.1), (11, 21, 2, 8.7), (12, 22, 2, 8.3), (12, 23, 2, 9.3),
(13, 24, 2, 8.0), (13, 25, 2, 8.8), (14, 26, 2, 9.2), (14, 27, 2, 7.6),
(15, 28, 2, 8.9), (15, 29, 2, 8.6), (16, 30, 2, 7.8), (16, 31, 2, 9.2),
(17, 32, 2, 8.4), (17, 33, 2, 8.1), (18, 34, 2, 9.0), (18, 35, 2, 8.2),
(19, 36, 2, 9.4), (19, 37, 2, 7.9), (20, 38, 2, 8.7), (20, 39, 2, 8.5),
(21, 40, 1, 8.6), (22, 41, 1, 7.9), (23, 42, 1, 9.1), (24, 43, 1, 8.2),
(25, 44, 1, 7.7), (26, 45, 1, 8.8), (27, 46, 1, 8.3), (28, 47, 1, 9.0),
(29, 48, 1, 8.5), (30, 49, 1, 7.8), (31, 50, 1, 8.9), (32, 1, 1, 8.1),
(33, 2, 1, 9.2), (34, 3, 1, 7.6), (35, 4, 1, 8.7), (36, 5, 1, 8.4),
(37, 6, 1, 9.3), (38, 7, 1, 7.9), (39, 8, 1, 8.6), (40, 9, 1, 8.0);

-- ============================================
-- QUERIES DE EXEMPLO
-- ============================================

-- 1. Listar alunos de um curso específico
SELECT a.id, a.nome, c.nome AS curso, c.serie
FROM alunos a
JOIN cursos c ON a.curso_id = c.id
WHERE c.id = 1
ORDER BY a.nome;

-- 2. Média de cada aluno em cada disciplina
SELECT a.nome, d.nome AS disciplina, AVG(av.media) AS media
FROM alunos a
JOIN avaliacoes av ON a.id = av.aluno_id
JOIN disciplinas d ON av.disciplina_id = d.id
GROUP BY a.id, d.id, a.nome, d.nome
ORDER BY a.nome, d.nome;

-- 3. Top 10 melhores alunos
SELECT a.nome, ROUND(AVG(av.media), 2) AS media_geral
FROM alunos a
JOIN avaliacoes av ON a.id = av.aluno_id
GROUP BY a.id, a.nome
ORDER BY media_geral DESC
LIMIT 10;

-- 4. Alunos com média < 7 (em recuperação)
SELECT DISTINCT a.nome, d.nome, av.media
FROM alunos a
JOIN avaliacoes av ON a.id = av.aluno_id
JOIN disciplinas d ON av.disciplina_id = d.id
WHERE av.media < 7
ORDER BY av.media ASC;

-- 5. Desempenho médio por série
SELECT c.serie, COUNT(DISTINCT a.id) AS total_alunos, ROUND(AVG(av.media), 2) AS media_serie
FROM cursos c
JOIN alunos a ON c.id = a.curso_id
JOIN avaliacoes av ON a.id = av.aluno_id
GROUP BY c.serie
ORDER BY media_serie DESC;

-- 6. Disciplinas com maior média
SELECT d.nome, COUNT(av.id) AS total_avaliacoes, ROUND(AVG(av.media), 2) AS media
FROM disciplinas d
LEFT JOIN avaliacoes av ON d.id = av.disciplina_id
GROUP BY d.id, d.nome
ORDER BY media DESC
LIMIT 10;

-- 7. Professor com alunos de melhor desempenho
SELECT p.nome, p.email, ROUND(AVG(av.media), 2) AS media_alunos
FROM professores p
JOIN disciplinas d ON p.id = d.professor_id
JOIN avaliacoes av ON d.id = av.disciplina_id
GROUP BY p.id, p.nome, p.email
ORDER BY media_alunos DESC
LIMIT 10;

-- 8. Quantidade de alunos por série
SELECT c.serie, COUNT(DISTINCT a.id) AS total_alunos
FROM cursos c
LEFT JOIN alunos a ON c.id = a.curso_id
GROUP BY c.serie
ORDER BY total_alunos DESC;

-- 9. Distribuição de notas
SELECT
  CASE
    WHEN media >= 9 THEN 'Excelente (9-10)'
    WHEN media >= 8 THEN 'Muito Bom (8-9)'
    WHEN media >= 7 THEN 'Bom (7-8)'
    WHEN media >= 6 THEN 'Satisfatório (6-7)'
    ELSE 'Insuficiente (<6)'
  END AS faixa_desempenho,
  COUNT(*) AS quantidade
FROM avaliacoes
GROUP BY faixa_desempenho
ORDER BY media DESC;

-- 10. Total de registros
SELECT
  (SELECT COUNT(*) FROM professores) AS total_professores,
  (SELECT COUNT(*) FROM disciplinas) AS total_disciplinas,
  (SELECT COUNT(*) FROM cursos) AS total_cursos,
  (SELECT COUNT(*) FROM alunos) AS total_alunos,
  (SELECT COUNT(*) FROM avaliacoes) AS total_avaliacoes;
