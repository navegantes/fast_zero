from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='Test_User', email='test_user@email.com', password='123456'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Test_User'))

    assert user.username == 'Test_User'
