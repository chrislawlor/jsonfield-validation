import pytest
from django.core.exceptions import ValidationError

from .app.models import MyModel, ShortListModel


@pytest.mark.django_db
def test_model_save(valid_data):
    instance = MyModel.objects.create(data=valid_data)
    assert instance.id is not None


def test_fails_on_model_clean_fields():
    invalid_data = {"status": "invalid"}
    instance = MyModel(data=invalid_data)
    with pytest.raises(ValidationError):
        instance.clean_fields()


def test_output():
    instance = ShortListModel(data=[1, 2, "3"])
    with pytest.raises(ValidationError) as ve:
        instance.clean_fields()
        assert "data" in ve.message
        assert "data" in ve.error_dict
        assert len(ve.error_dict["data"]) == 2
        assert "'3' is not of type 'number'" in ve.error_dict["data"]
        assert "[1, 2, '3'] is too long" in ve.error_dict["data"]
