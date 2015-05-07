from contact import Contact

class ContactLoader:

    def load(self):
        return [
            Contact('testname', {'email': 'some@email.com', 'phone': '1234 5678', 'fbname': 'test', 'voipname': 'testname123', 'tubestation': 'Bank', 'contactless': True}),
            Contact('foobar', {'email': 'foo@bar.com', 'phone': '9876 5432', 'fbname': 'foo', 'voipname': 'foobar456', 'contactless': True, 'tubestation': 'Tooting Broadway', 'twitter': 'fbar123'}),
        ]
