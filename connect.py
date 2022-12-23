import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-BNEAF7Q5\MSSQLSERVER02;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')
# print("done..")

cursor = conn.cursor()
# cursor.execute('SELECT * FROM Employees')

# for i in cursor:
#     print(i)
cursor.execute('''
                INSERT INTO F_Game(QuestionID, Question, Answer, Catagory,Options)
                VALUES
                (1,'What is the currency of Qatar? ','Riyal','General_Knowledge', 'A. Pound  B. Euro  C. Riyal  D. Dollar'),
                (2,'What is the average weight of the human brain? ', '4 kg', 'General_Knowledge', 'A. 14 g  B. 2.4 g  C. 4 kg   D. 1.4 kg'),
                (3,'Queen Elizabeth III has been reigning on the British Royal Kingdom as Queen for how many years? ', '60', 'General_Knowledge', 'A. 50  B. 60  C. 70 D. 80'),
                (4,'Which is the closest planet to earth? ', 'jupter', 'General_Knowledge', 'A. Mars  B. plto  C. jupter  D. satern'),
                (5,'What native country is Brazil? ',  'North America', 'General_Knowledge', 'A. South America  B. North America  C. East America   D. West America')
                ''')
conn.commit()

cursor = conn.cursor()
cursor.execute('''
                 INSERT INTO F_Game(QuestionID, Question, Answer, Catagory,Options)
                 VALUES
                 (1,'What is the National Sports of Brazil? ', 'Capoeira', 'Sport', 'A. Football B. Pato C. Capoeira D.  Oina'),
                 (2,'Who won the FIFA World Cup in 2018? ', 'France',  'Sport', 'A. Argentina B. France C. Italy D. Brazil'),
                 (3,'What is the 100m World Record of Usain Bolt? ', '9.58 Sec', 'Sport', 'A. 14.35 Sec B. 9.58 Sec C. 9.05 Sec D. 10.12 Sec'),
                 (4,'What is the National Game of the USA? ', 'Baseball', 'Sport', 'A. Tennis B. Soccer C. Baseball D. Basket Ball'),
                 (5,'Which Country Won the most FIFA World Cups? ', 'Brazil', 'Sport', 'A. Germany B. Argentina C.  Brazil D. France')
                  ''')
conn.commit()

cursor = conn.cursor()
cursor.execute('''
                 INSERT INTO F_Game(QuestionID, Question, Answer, Catagory,Options)
                 VALUES
                 (1,'In which Hollywood movie did the actor Bill Paxton portray the role of Fred Haise? ', 'Apollo 11', 'Movie', 'A. Apollo 11 B. Matrix C. Gladiator D.  Solo'),
                 (2,'In 2016, Game of Thrones resurrected which famous and popular character? ', 'Jon Snow',  'Movie', 'A. Jon Snow B. Bad Snow C. Oliver Snow D. Wiliam Snow'),
                 (3,'Who actually drew the sketch of Rose in Titanic? ', 'James Cameron', 'Movie', 'A. Leonardo DiCaprio B. Billy Zane C. James Cameron D.  Kathy Bates'),
                 (4,'What is the highest-grossing movie of all time? ', 'Titanic', 'Movie', 'A. Titanic B. Avatar C. Avengers: Endgame D. Star Wars: The Force Awakens'),
                 (5,'The code in The Matrix comes from what food recipes? ', 'Pad thai recipes','Movie', 'A. Sushi recipes B. Dumpling recipes C. Stir-fry recipes D. Pad thai recipes')
                 ''')
conn.commit()

cursor = conn.cursor()

cursor.execute('''
                 INSERT INTO F_Game(QuestionID, Question, Answer, Catagory,Options)
                 VALUES
                 (1,'In which spectral region is it possible for astronomers to observe through cloud? ','X-ray', 'Astronemy', 'A. visual  B. radio C. ultraviolet D. X-ray'),
                 (2,'In kilometers the earths average distance from the sun is roughlwhich of the following distances? ','150 million',  'Astronemy', 'A. 250 million  B. 91 million  C. 150 million D. 350 million'),
                 (3,'Which of the following planets has the lowest density? ', 'Saturn', 'Astronemy', 'A. Saturn  B. Mars  C.  Mercury D.  Venus'),
                 (4,'Which one of the following planets has no moons? ', 'Venus', 'Astronemy', 'A. Mars  B. Neptune  C. Venus D. Jupiter'),
                 (5,'The atmosphere of Venus contains mostly? ', 'carbon dioxide','Astronemy', 'A. oxygen  B. carbon dioxide C. nitrogen D. water')
                 ''')
conn.commit()

