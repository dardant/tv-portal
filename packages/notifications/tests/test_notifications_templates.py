from notifications import shipped_body, shipped_subject


def test_subject_names_the_order_and_its_tracking_number():
    assert shipped_subject({"id": "A-100", "tracking": "1Z999"}) == "Your order A-100 has shipped (tracking 1Z999)"


def test_body_greets_the_customer_by_name():
    assert shipped_body({"id": "A-100", "customer_name": "Ada"}).startswith("Hi Ada,")


def test_body_omits_tracking_when_there_is_none():
    assert "Track it" not in shipped_body({"id": "A-100"})
