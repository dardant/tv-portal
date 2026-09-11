from notifications import build_digest


def test_each_email_goes_to_the_event_customer():
    emails = build_digest([{"customer_email": "ada@example.com", "kind": "password_changed"}])
    assert emails[0]["to"] == "ada@example.com"


def test_one_email_per_event():
    events = [
        {"customer_email": "ada@example.com", "kind": "password_changed"},
        {"customer_email": "ada@example.com", "kind": "address_changed"},
    ]
    assert len(build_digest(events)) == 2
