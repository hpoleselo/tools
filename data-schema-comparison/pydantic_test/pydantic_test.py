import json
from jsonschema import validate, ValidationError, SchemaError
class DataValidation():
    def __init__(self):
        self.createSchema()

    def createSchema(self):
        """ Creating our Data Schema Pattern to be validated against the incoming data """
        

        class BookSchema(BaseModel):
            title: str
            isbn: str

        class UserSchema(BaseModel):
            email: str



    def retrieveData(self):
        # Retrieved Data will Come as JSON, so we have to desserialize it
        with open('user_wrong.json') as json_file:
            json_data = json.load(json_file)
        return json_data

    def validateData(self, json_data):
        # json_data is now a dict, which our userSchema can inherit from
        schema = self.UserSchema()


        try:
            user = schema.load(json_data)
            print("Validation went Good, proceeding to next step from pipeline...")
            return True
        except():
            print("Validation went wrong")
            return False

    def exportData(self, json_data):
        print("Exporting data as JSON...")

    def testValidation(self):
        self.createSchema()
        json_data = self.retrieveData()
        if (self.validateData(json_data)):
            self.exportData(json_data)


if __name__ == "__main__":
    dv = DataValidation()
    dv.testValidation()
