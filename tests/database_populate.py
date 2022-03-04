from flask import Flask
from app.models import BooksModel, ClassroomModel, StudentsModel, GradesModel, AbsenceModel, EmployeeModel, SchoolSubjectsModel, LibraryModel


def populate_database(app:Flask):
    with app.app_context():
        app.db.session.add_all([
                #Populate books
                BooksModel (book_id='2fc09626-8a2c-4ef7-b59d-4a56e77e5714', title='Harry Potter - E a pedra filosofal', author='J.K. Rowling',quantity=5),
                BooksModel ('081c575b-a38f-4f41-bf15-2593cd58ab93', 'Harry Potter e a Câmara dos Segredos', 'J.K. Rowling', 3),
                BooksModel ('cc733168-68ae-45b8-b4c2-434901ccea0f', 'Harry Potter e a Criança Amaldiçoada - Parte 1', 'J.K. Rowling', 5),
                BooksModel ('9c638ca2-901c-4028-91d4-c34209eff719', 'Harry Potter e a Criança Amaldiçoada - Parte 2', 'J.K. Rowling', 5),

                BooksModel ('Harry Potter - E a pedra filosofal', 'J.K. Rowling', 5),
                BooksModel ('Harry Potter e a Câmara dos Segredos', 'J.K. Rowling', 3),
                BooksModel ('Harry Potter e a Criança Amaldiçoada - Parte 1', 'J.K. Rowling', 5),
                BooksModel ('Harry Potter e a Criança Amaldiçoada - Parte 2', 'J.K. Rowling', 5),


                #Populate classrooms
                ClassroomModel ('51df51e0-00a7-49e3-9f2e-0405574f5c20', '1A'),
                ClassroomModel ('1446d11e-6985-4979-8e7f-15d5ddf0a81f', '1B'),
                ClassroomModel ('cf43d8ca-37a8-4140-bc97-32192e151a27', '2A'),
                ClassroomModel ('3df783ee-d140-47cd-9c65-213b830a7ca6', '2B'),

                # Populate students
                StudentsModel ('51df51e0-00a7-49e3-9f2e-0405574f5c20', 'felipe', 'Rosita',
                    'rosita@email.com', '11111111111', '2000-02-20', 'Feminino', 
                    'pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    '1234', '51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                StudentsModel ('1d5225ef-5638-4397-9989-e604a2cceca0', 'matheus', 'Sirlei', 
                    'sirlei@email.com', '11111111112', '2000-02-20', 'Feminino', 
                    'pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    '1234',  '51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                StudentsModel ('7dc82c28-4766-4bff-829b-2198a2e1ef98', 'rafael', 'Maria',
                    'maria@email.com', '11111111113', '2000-02-20', 'Feminino',
                    'pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    '1234',  '1446d11e-6985-4979-8e7f-15d5ddf0a81f'
                ),
                StudentsModel ('2a465bd0-22cd-45e7-9fd1-142dee2cca78', 'renato', 'Maria',
                    'mariaa@email.com', '11111111114', '2000-02-20', 'Feminino', 
                    'pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    '1234','cf43d8ca-37a8-4140-bc97-32192e151a27'  
                ),

                # Populate grades
                GradesModel ('14cff389-868d-4858-8e3b-466ab29c8137', 'codar', 9.0, '51df51e0-00a7-49e3-9f2e-0405574f5c20', '51df51e0-00a7-49e3-9f2e-0405574f5c20'),
                GradesModel ('7269be99-8a06-4e40-9179-bce1c622c505', 'codar', 3.5, '1d5225ef-5638-4397-9989-e604a2cceca0', '51df51e0-00a7-49e3-9f2e-0405574f5c20'),
                GradesModel ('a80631f9-c520-44ab-b128-0c432fb59bb2', 'codar', 10.0, '2a465bd0-22cd-45e7-9fd1-142dee2cca78', 'cf43d8ca-37a8-4140-bc97-32192e151a27'),
                GradesModel ('cf43d8ca-37a8-4140-bc97-32192e151a27', 'codar', 8.5, '7dc82c28-4766-4bff-829b-2198a2e1ef98', '1446d11e-6985-4979-8e7f-15d5ddf0a81f'),

                # Populate absence
                AbsenceModel ('b20dfcbb-f121-41ef-bf96-cb988d68a35a', '2020-02-15', False, '51df51e0-00a7-49e3-9f2e-0405574f5c20', '1d5225ef-5638-4397-9989-e604a2cceca0'),
                AbsenceModel ('9cf30ce0-6925-4ff1-9bbf-f27bd7916782', '2020-02-15', True, '51df51e0-00a7-49e3-9f2e-0405574f5c20', '1d5225ef-5638-4397-9989-e604a2cceca0'),
                AbsenceModel ('494925c7-7399-44e2-a00e-653581145979', '2020-02-15', False, '51df51e0-00a7-49e3-9f2e-0405574f5c20', '51df51e0-00a7-49e3-9f2e-0405574f5c20'),
                AbsenceModel ('d98c6e17-d6ce-4432-bc31-b10418a7cf44', '2020-02-15', False, 'cf43d8ca-37a8-4140-bc97-32192e151a27', '2a465bd0-22cd-45e7-9fd1-142dee2cca78'),

                # Populate employee 
                EmployeeModel ('b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4', 'lucira', 'lucira@email.com', 4000.00,
                    'pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', '1234', 'teacher'
                ),
                EmployeeModel ('6d4b0f4d-a418-432e-a112-b44527ea33d4', 'chrystian', 'chrystian@email.com', 10000.00, 
                        'pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', '1234', 'teacher'
                ),
                EmployeeModel ('b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', 'matheus' , 'matheus@email.com', 2000.00, 
                        'pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', '1234', 'librarian'
                ),
                EmployeeModel ('3f5e5df3-651b-46ec-9c42-be4a863f974a', 'paulo' , 'paulo@email.com', 2000.00,
                        'pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', '1234', 'teacher'
                ),

                # Populate school subjects 
                SchoolSubjectsModel ('62921285-ac00-4f38-ab44-356cdea16631', 'react', 'b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4', '51df51e0-00a7-49e3-9f2e-0405574f5c20'),
                SchoolSubjectsModel ('19c9807c-d818-4bc5-8d80-c66ad5ff253f', 'python', '6d4b0f4d-a418-432e-a112-b44527ea33d4', '1446d11e-6985-4979-8e7f-15d5ddf0a81f'),
                SchoolSubjectsModel ('c3280110-1a25-40cb-8573-b20f9f14b200', 'node', '3f5e5df3-651b-46ec-9c42-be4a863f974a', 'cf43d8ca-37a8-4140-bc97-32192e151a27'),
                SchoolSubjectsModel ('73e8e3e6-db7a-4cae-9ae6-74f4d0e87d66', 'python', '6d4b0f4d-a418-432e-a112-b44527ea33d4', '3df783ee-d140-47cd-9c65-213b830a7ca6'),

                # Populate library
                LibraryModel ('3554e9f0-8208-4e99-81c1-d79f3caf891c', '2020-02-01', '2020-02-15', '2020-02-15', 
                        'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', '3fc09626-8a2c-4ef7-b59d-4a56e77e5714', '51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                LibraryModel ('201e6867-ec20-4834-b4ce-1f01b0b9e8db', '2020-02-01', '2020-02-15', '2020-02-15', 
                        'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', '3fc09626-8a2c-4ef7-b59d-4a56e77e5714','1d5225ef-5638-4397-9989-e604a2cceca0'
                ),
                LibraryModel ('23c3c4c8-d923-43d3-bc1b-c47d7b741ee1', '2020-02-01', '2020-02-15', '2020-02-15', 
                        'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', '082c575b-a38f-4f41-bf15-2593cd58ab93','7dc82c28-4766-4bff-829b-2198a2e1ef98'
                ),
                LibraryModel ('023b926d-8f03-460d-be7b-840d80f91f6e', '2020-02-01', '2020-02-15', '2020-02-15', 
                        'b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', 'cc733169-68ae-45b8-b4c2-434901ccea0f','2a465bd0-22cd-45e7-9fd1-142dee2cca78'
                )
           ])
        app.db.session.commit()
