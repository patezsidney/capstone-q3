from flask import Flask

from app.models import (AbsenceModel, BooksModel, ClassroomModel,
                        EmployeeModel, GradesModel, LibraryModel,
                        SchoolSubjectsModel, StudentsModel)


def populate_database(app:Flask):
    with app.app_context():
        app.db.session.add_all([
                #Populate books
                BooksModel (book_id='2fc09626-8a2c-4ef7-b59d-4a56e77e5714', title='Harry Potter - E a pedra filosofal', author='J.K. Rowling',quantity=5),
                BooksModel (book_id='081c575b-a38f-4f41-bf15-2593cd58ab93', title='Harry Potter e a Câmara dos Segredos', author='J.K. Rowling', quantity=3),
                BooksModel (book_id='cc733168-68ae-45b8-b4c2-434901ccea0f',title='Harry Potter e a Criança Amaldiçoada - Parte 1',author='J.K. Rowling', quantity= 5),
                BooksModel (book_id='9c638ca2-901c-4028-91d4-c34209eff719',title='Harry Potter e a Criança Amaldiçoada - Parte 2',author='J.K. Rowling', quantity= 5),

                #Populate classrooms
                ClassroomModel (classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20',name='1A'),
                ClassroomModel (classroom_id='1446d11e-6985-4979-8e7f-15d5ddf0a81f',name='1B'),
                ClassroomModel (classroom_id='cf43d8ca-37a8-4140-bc97-32192e151a27',name='2A'),
                ClassroomModel (classroom_id='3df783ee-d140-47cd-9c65-213b830a7ca6',name='2B'),

                # Populate students
                StudentsModel (registration_student_id='51df51e0-00a7-49e3-9f2e-0405574f5c20', name='felipe', contact_name='Rosita',
                    contact_email='rosita@email.com', cpf='11111111111', birth_date='2000-02-20', gender='Feminino', 
                    password_hash='pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    api_key='1230', classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20', photo=None
                ),
                StudentsModel (registration_student_id='1d5225ef-5638-4397-9989-e604a2cceca0', name='matheus', contact_name='Sirlei', 
                    contact_email='sirlei@email.com', cpf='11111111112', birth_date='2000-02-20', gender='Feminino', 
                    password_hash='pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    api_key='1231',  classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20', photo=None
                ),
                StudentsModel (registration_student_id='7dc82c28-4766-4bff-829b-2198a2e1ef98', name='rafael', contact_name='Maria',
                    contact_email='maria@email.com', cpf='11111111113', birth_date='2000-02-20', gender='Feminino',
                    password_hash='pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    api_key='1232',  classroom_id='1446d11e-6985-4979-8e7f-15d5ddf0a81f', photo=None
                ),
                StudentsModel (registration_student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78', name='renato', contact_name='Maria',
                    contact_email='mariaa@email.com', cpf='11111111114', birth_date='2000-02-20', gender='Feminino', 
                    password_hash='pbkdf2:sha256:260000$Qm0vHzt1WUw2GEE3$0133835de0c8006712fdad354ead0112aee9c77984e6c19ee24d3805d8c05614',
                    api_key='1233',classroom_id='cf43d8ca-37a8-4140-bc97-32192e151a27', photo=None
                ),

                # Populate grades
                GradesModel (grade_id='14cff389-868d-4858-8e3b-466ab29c8137',ativity='codar',grade=9.0, 
                    student_id='51df51e0-00a7-49e3-9f2e-0405574f5c20',classrom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                GradesModel (grade_id='7269be99-8a06-4e40-9179-bce1c622c505',ativity='codar',grade=3.5, 
                    student_id='1d5225ef-5638-4397-9989-e604a2cceca0',classrom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                GradesModel (grade_id='a80631f9-c520-44ab-b128-0c432fb59bb2',ativity='codar',grade=10.0,
                    student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78',classrom_id='cf43d8ca-37a8-4140-bc97-32192e151a27'
                ),
                GradesModel (grade_id='cf43d8ca-37a8-4140-bc97-32192e151a27',ativity='codar',grade=8.5, 
                    student_id='7dc82c28-4766-4bff-829b-2198a2e1ef98',classrom_id='1446d11e-6985-4979-8e7f-15d5ddf0a81f'
                ),

                # Populate absence
                AbsenceModel (absence_id='b20dfcbb-f121-41ef-bf96-cb988d68a35a',date='2020-02-15',justify=False,
                        classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20',student_id='1d5225ef-5638-4397-9989-e604a2cceca0'
                ),
                AbsenceModel (absence_id='9cf30ce0-6925-4ff1-9bbf-f27bd7916782',date='2020-02-15',justify=True, 
                        classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20',student_id='1d5225ef-5638-4397-9989-e604a2cceca0'
                ),
                AbsenceModel (absence_id='494925c7-7399-44e2-a00e-653581145979',date='2020-02-15',justify=False,
                        classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20',student_id='51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                AbsenceModel (absence_id='d98c6e17-d6ce-4432-bc31-b10418a7cf44',date='2020-02-15',justify=False,
                        classroom_id='cf43d8ca-37a8-4140-bc97-32192e151a27',student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78'
                ),

                # Populate employee 
                EmployeeModel ( employee_id='b70c93e0-a6c0-43f1-8c7b-ea3b1b3f00f4', name='lucira', email='lucira@email.com', wage=4000.00,
                        password_hash='pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', api_key='1234', access_level='admin'
                ),
                EmployeeModel ( employee_id='6d4b0f4d-a418-432e-a112-b44527ea33d4', name='chrystian', email='chrystian@email.com', wage=10000.00, 
                        password_hash='pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', api_key='1235', access_level='teacher'
                ),
                EmployeeModel (employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', name='matheus' , email='matheus@email.com', wage=2000.00, 
                        password_hash='pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', api_key='1236', access_level='librarian'
                ),
                EmployeeModel (employee_id='3f5e5df3-651b-46ec-9c42-be4a863f974a', name='paulo' , email='paulo@email.com', wage=2000.00,
                        password_hash='pbkdf2:sha256:260000$CGnI1ihhhndhuDTJ$56a23d6eedf63f1745d5ddb40315705101692bb0cd16c25b0e6e1d910c17d06e', api_key='1237', access_level='teacher'
                ),

                # Populate school subjects 
                SchoolSubjectsModel (school_subject_id='62921285-ac00-4f38-ab44-356cdea16631',school_subject='react', employee_id='3f5e5df3-651b-46ec-9c42-be4a863f974a', classroom_id='51df51e0-00a7-49e3-9f2e-0405574f5c20'),
                SchoolSubjectsModel (school_subject_id='19c9807c-d818-4bc5-8d80-c66ad5ff253f',school_subject='python', employee_id='6d4b0f4d-a418-432e-a112-b44527ea33d4', classroom_id='1446d11e-6985-4979-8e7f-15d5ddf0a81f'),
                SchoolSubjectsModel (school_subject_id='c3280110-1a25-40cb-8573-b20f9f14b200',school_subject='node', employee_id='3f5e5df3-651b-46ec-9c42-be4a863f974a', classroom_id='cf43d8ca-37a8-4140-bc97-32192e151a27'),
                SchoolSubjectsModel (school_subject_id='73e8e3e6-db7a-4cae-9ae6-74f4d0e87d66',school_subject='python', employee_id='6d4b0f4d-a418-432e-a112-b44527ea33d4', classroom_id='3df783ee-d140-47cd-9c65-213b830a7ca6'),

            
           ])
        app.db.session.commit()

        app.db.session.add_all([
                    # Populate library
                LibraryModel (library_id='3554e9f0-8208-4e99-81c1-d79f3caf891c', date_withdrawal='2020-02-01', date_return='2020-02-15', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='2fc09626-8a2c-4ef7-b59d-4a56e77e5714', student_id='51df51e0-00a7-49e3-9f2e-0405574f5c20'
                ),
                LibraryModel (library_id='201e6867-ec20-4834-b4ce-1f01b0b9e8db', date_withdrawal='2020-02-01', date_return='2020-02-15', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='2fc09626-8a2c-4ef7-b59d-4a56e77e5714', student_id='1d5225ef-5638-4397-9989-e604a2cceca0'
                ),
                LibraryModel (library_id='23c3c4c8-d923-43d3-bc1b-c47d7b741ee1', date_withdrawal='2020-02-01', date_return='2020-02-15', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='081c575b-a38f-4f41-bf15-2593cd58ab93', student_id='7dc82c28-4766-4bff-829b-2198a2e1ef98'
                ),
                LibraryModel (library_id='023b926d-8f03-460d-be7b-840d80f91f6e', date_withdrawal='2020-02-01', date_return='2020-02-15', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='cc733168-68ae-45b8-b4c2-434901ccea0f', student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78'
                ),
                LibraryModel (library_id='872bda57-7606-40e6-a05c-47d38926ed9b', date_withdrawal='2020-02-01', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='cc733168-68ae-45b8-b4c2-434901ccea0f', student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78'
                ),
                LibraryModel (library_id='dd2af223-8f20-4019-90da-00c07aa3f1fe', date_withdrawal='2020-02-01', date_return='2020-02-15', date_accurancy='2020-02-15', 
                        employee_id='b3298cfc-7fb8-47af-91ed-f2d8c4545cdd', book_id='cc733168-68ae-45b8-b4c2-434901ccea0f', student_id='2a465bd0-22cd-45e7-9fd1-142dee2cca78'
                )
        ])
        app.db.session.commit()