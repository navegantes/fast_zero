from sqlalchemy import select

from fast_zero.models import Todo, User


def test_create_user(session):
    new_user = User(
        username='Test_User', email='test_user@email.com', password='123456'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Test_User'))

    assert user.username == 'Test_User'


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Description',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
