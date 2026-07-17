from fastapi import FastAPI,Depends
from pydantic import BaseModel
from mongodb import get_collection
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

app=FastAPI()


class Data(BaseModel):
    name:str
    age:int

class Updateage(BaseModel):
    age:int


def get_users_detail(collection=Depends(get_collection)):
    return list(collection.find({}))
   

@app.get("/users")
def get_users(collection=Depends(get_users_detail)):
    return jsonable_encoder(
        collection,
        custom_encoder={ObjectId: str}
    )

@app.post("/adduser")
def add_user(useradd:Data,collection=Depends(get_collection)):
    result=collection.insert_one(useradd.model_dump())
    return{
        "Message":"User add sucessfully",
        "_id": str(result.inserted_id)
    }

@app.get("/user/{name}")
def search_user(name:str,collection=Depends(get_collection)):
    user=collection.find_one({"name":name})
    if user:
        return jsonable_encoder(user,custom_encoder={
            ObjectId:str
        })
    return{
        "meassage":"User not Found"
    }


@app.delete("/userdel")
def del_user(name:str,collection=Depends(get_collection)):
    users=list(collection.find({"name":name},{"_id":0,"name":1}))
    print(users)
    if any(user["name"]== name for user in users):
        delet_user=collection.delete_one({"name":name})
        return{
            "message":"User delete"
        }
    else:
        return{
            "message":"user not delete"
        }

@app.put("/updateuser")
def update_age(name:str,age:Updateage,collection=Depends(get_collection)):
    result=collection.update_one({"name":name},{"$set":{"age":age.age}})

    if result.matched_count == 0:
        return{
            "Mesaage":"User not found"
        }
    return{
        "Message":"User Update successfully"
    }

