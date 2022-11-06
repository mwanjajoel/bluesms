from bluesms.utils import validate_phone_number
import pytest


@pytest.mark.parametrize(
    "phone_number, is_valid",
    [
        (
            '+256703000000',
            True
        ),
        (
            '+1703000000',
            True
        ),
        (
            '000000',
            False
        )
    ]
)
def test_validate_phone_number(phone_number: False, is_valid: bool):
    assert validate_phone_number(phone_number) == is_valid
