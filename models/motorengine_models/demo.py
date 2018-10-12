from motorengine import Document, StringField

class Demo(Document):
    __collection__ = "Demo"  # optional. if no collection is specified, class name is used.

    name = StringField(required=True)
