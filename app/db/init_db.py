from app.database import engine, Base
from app.module1 import models as module1_models
from app.module2 import models as module2_models

def init_db():
    """
    Cria as tabelas no banco de dados, se ainda não existirem.
    """
    Base.metadata.create_all(bind=engine)
