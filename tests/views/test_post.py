import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert b'<title>' in response.content  # Verifique se o conteúdo HTML tem uma tag <title>
