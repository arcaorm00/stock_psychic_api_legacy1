from com_stock_api.ext.db import db
from com_stock_api.memberChurn_pred.memberChurn_pred_dto import MemberChurnPredDto
import pandas as pd
import json

class MemberChurnPredDao(MemberChurnPredDto):

    @classmethod
    def find_all(cls):
        sql = cls.query
        df = pd.read_sql(sql.statement, sql.session.bind)
        return json.loads(df.to_json(orient='records'))

    @classmethod
    def find_by_email(cls, member):
        sql = cls.query.filter(cls.email.like(member.email))
        df = pd.read_sql(sql.statement, sql.session.bind)
        print(json.loads(df.to_json(orient='records')))
        return json.loads(df.to_json(orient='records'))
    
    @staticmethod
    def save(member):
        db.session.add(member)
        db.session.commit()
    
    @staticmethod
    def modify_member(member):
        db.session.add(member)
        db.commit()
    
    def delete_member(cls, email):
        data = cls.query.get(email)
        db.session.delete(data)
        db.session.commit()