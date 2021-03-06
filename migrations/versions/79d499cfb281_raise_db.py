"""raise db

Revision ID: 79d499cfb281
Revises: 
Create Date: 2022-03-09 10:03:15.357207

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79d499cfb281'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('book_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('classrooms',
    sa.Column('classroom_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('classroom_id')
    )
    op.create_table('employees',
    sa.Column('employee_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('wage', sa.Float(), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(), nullable=True),
    sa.Column('api_key', sa.VARCHAR(), nullable=True),
    sa.Column('access_level', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('employee_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('schoolsubjects',
    sa.Column('school_subject_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('school_subject', sa.String(length=255), nullable=False),
    sa.Column('employee_id', postgresql.UUID(), nullable=False),
    sa.Column('classroom_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.classroom_id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], ),
    sa.PrimaryKeyConstraint('school_subject_id')
    )
    op.create_table('students',
    sa.Column('registration_student_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('contact_name', sa.String(length=255), nullable=False),
    sa.Column('contact_email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('classroom_id', postgresql.UUID(), nullable=False),
    sa.Column('api_key', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.classroom_id'], ),
    sa.PrimaryKeyConstraint('registration_student_id'),
    sa.UniqueConstraint('cpf')
    )
    op.create_table('absence',
    sa.Column('absence_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('justify', sa.Boolean(), nullable=True),
    sa.Column('classroom_id', postgresql.UUID(), nullable=False),
    sa.Column('student_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.classroom_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.registration_student_id'], ),
    sa.PrimaryKeyConstraint('absence_id')
    )
    op.create_table('grades',
    sa.Column('grade_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('ativity', sa.String(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=False),
    sa.Column('student_id', postgresql.UUID(), nullable=False),
    sa.Column('classrom_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['classrom_id'], ['classrooms.classroom_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.registration_student_id'], ),
    sa.PrimaryKeyConstraint('grade_id')
    )
    op.create_table('library',
    sa.Column('library_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_withdrawal', sa.Date(), nullable=False),
    sa.Column('date_return', sa.Date(), nullable=True),
    sa.Column('date_accurancy', sa.Date(), nullable=False),
    sa.Column('employee_id', postgresql.UUID(), nullable=False),
    sa.Column('book_id', postgresql.UUID(), nullable=False),
    sa.Column('student_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.book_id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.registration_student_id'], ),
    sa.PrimaryKeyConstraint('library_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library')
    op.drop_table('grades')
    op.drop_table('absence')
    op.drop_table('students')
    op.drop_table('schoolsubjects')
    op.drop_table('employees')
    op.drop_table('classrooms')
    op.drop_table('books')
    # ### end Alembic commands ###
