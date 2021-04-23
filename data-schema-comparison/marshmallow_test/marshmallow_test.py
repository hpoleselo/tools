import json
from marshmallow import Schema, fields, validate, post_load, exceptions

# With marshmallow we're comparing dict to dict

class DataValidation():
    def __init__(self):
        self.UserSchema = self.createSchema()
        self.fileToValidate = '../user_wrong.json'

    def createSchema(self):
        """ Creating our Data Schema Pattern to be validated against the incoming data """
        
        def validate_isbn(isbn: str) -> None:
            """ Validates the isbn with some code (omitted), raise marshmallow.ValidationError if validation did not pass """

        class BookSchema(Schema):
            title = fields.String(required=True, validate=validate.Length(max=120))
            isbn = fields.String(required=True, validate=validate_isbn)

        class UserSchema(Schema):
            email = fields.Email(required=True)
            books = fields.Nested(BookSchema, many=True, required=False)

        return UserSchema

    def retrieveData(self):
        jsonFile = self.fileToValidate
        # Retrieved Data will Come as JSON, so we have to desserialize it
        with open(jsonFile) as json_file:
            json_data = json.load(json_file)
        return json_data

    def validateData(self, json_data):
        # json_data is now a dict, which our userSchema can inherit from
        schema = self.UserSchema()
        try:
            user = schema.load(json_data)
            print("[LOGGING]: Validation went good, proceeding to next step from pipeline...")
            return True
        except exceptions.ValidationError as error:
            print(f"[ERROR]: Validation went wrong, cause: {error}")
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
