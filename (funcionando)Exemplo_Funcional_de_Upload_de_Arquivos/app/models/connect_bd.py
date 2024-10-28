from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from app.models.model import Person, Token
from app.models.utils_bd import connecting_bd
from hashlib import sha256


#________________________________Pessoas___________________________________#

def get_person_by_cpf(cpf):
        
    '''Lista todas as pessoas'''
    
    session = connecting_bd()
    
    try:
    
        if session is not None:
    
            query = session.query(Person).filter(Person.cpf == cpf)
    
            person = query.one()
                
            return person
        
    except Exception as e:
    
        print("Erro na consulta:", e)
    
    finally:
    
        if session:
    
            session.close()

#FUNCIONANDO
def login(login, password):

    '''Faz login de uma pessoa'''

    try:

        session = connecting_bd()
        
        if session is not None:
        
            query = session.query(Person).filter((Person.email == login) | (Person.cpf == login)).filter(Person.password == sha256(password.encode()).digest())
        
            person = query.one()
        
            return person
    
    except NoResultFound:
    
        print("Combinação de email/cpf e senha não encontrada")
    
    except SQLAlchemyError as e:
    
        print("Erro ao fazer login:", e)
    
    finally:
    
        if session:
    
            session.close()

#FUNCIONANDO
def register_person(**kwargs):

    '''Adiciona uma pessoa na lista'''
    
    try:
    
        session = connecting_bd()
    
        if session is not None:
    
            person = Person(**kwargs)
    
            session.add(person)
    
            session.commit()
    
            print("Cadastro da pessoa realizado com sucesso")
    
    except SQLAlchemyError as e:

        print("Erro ao cadastrar pessoa:", e)

        session.rollback()
        
        raise e 
    
    finally:
    
        if session:
    
            session.close()

#VERIFICAR SE FUNCIONA
def edit_person(login1,password1,**kwargs):

    '''Edita um ou mais campos de uma pessoa'''

    try:
        
        session = connecting_bd()

        person = login(login=login1,password=password1)

        for key, value in kwargs.items():

            setattr(person, key, value)

        session.commit()

        print("Pessoa editada com sucesso")
    
    except Exception as e:
    
        print("Erro ao editar pessoa:", e)
    
        session.rollback()
    
    finally:
    
        if session:
    
            session.close()

#________________________________Token___________________________________#

#FUNCIONANDO
def register_token(token, person_cpf):
    
        '''Adiciona um token na lista'''
        
        try:
        
            session = connecting_bd()
        
            if session is not None:
        
                token1 = Token(token, person_cpf,state_of="Activated")
        
                session.add(token1)
        
                session.commit()
        
                print("Cadastro do token realizado com sucesso")
        
        except SQLAlchemyError as e:
        
            print("Erro ao cadastrar o token:", e)
        
            session.rollback()
            
            raise e 
        
        finally:
        
            if session:
        
                session.close()

#FUNCIONANDO
def transform_the_last_token_in_expired(person_cpf):
        
        '''Transforma o último token em expirado'''
        
        try:
        
            session = connecting_bd()
        
            if session is not None:
        
                query = session.query(Token).filter(Token.person_cpf == person_cpf).filter(Token.state_of == "Activated")
        
                token = query.one()
                print(token)
                token.state_of = "Expireted"
        
                session.commit()
        
                print("Token expirado com sucesso")
        
        except Exception as e:
        
            print("Erro ao expirar token:", e)
        
            session.rollback()
        
        finally:
        
            if session:
        
                session.close()

