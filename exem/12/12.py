
class Meta(type):
    def __new__(cls, name, parents, attrs):
        print("Creat {}".format(name))

    if "class id" not in attrs:
        attrs["class_id"] = name.lower()

    return super().__new__(cls, name, parents, attrs)

class A(metaclass=Meta):
    pass

Creat A

print("A.class_id: "{}"".format(A.class_id))