from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import or_
from ORM import Pessoa


def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

# x = session.query(Pessoa).all()
# x = session.query(Pessoa).filter(Pessoa.nome == 'wikten').filter(Pessoa.usuario == 'marcos')
# x=session.query(Pessoa).filter_by(usuario ='marcos', nome ='wikten').all()

x = session.query(Pessoa).filter(Pessoa.id == 1).one()

session.delete(x)
session.commit()