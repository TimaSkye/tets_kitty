import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from .models import Breed, Kitten


@pytest.mark.django_db
def test_breed_list():
    client = APIClient()
    response = client.get('/api/breeds/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_kitten_list():
    client = APIClient()
    user = get_user_model().objects.create_user(username='testuser', password='password')
    client.force_authenticate(user=user)
    response = client.get('/api/kittens/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_kitten_create():
    client = APIClient()
    user = get_user_model().objects.create_user(username='testuser', password='password')
    client.force_authenticate(user=user)
    breed = Breed.objects.create(name='Test Breed')
    data = {'breed': breed.id, 'color': 'White', 'age_in_months': 6, 'description': 'Test kitten'}
    response = client.post('/api/kittens/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_kitten_update():
    client = APIClient()
    user = get_user_model().objects.create_user(username='testuser', password='password')
    client.force_authenticate(user=user)
    breed = Breed.objects.create(name='Test Breed')
    kitten = Kitten.objects.create(breed=breed, color='White', age_in_months=6, description='Test kitten', owner=user)
    data = {'color': 'Black'}
    response = client.patch(f'/api/kittens/{kitten.id}/', data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_kitten_delete():
    client = APIClient()
    user = get_user_model().objects.create_user(username='testuser', password='password')
    client.force_authenticate(user=user)
    breed = Breed.objects.create(name='Test Breed')
    kitten = Kitten.objects.create(breed=breed, color='White', age_in_months=6, description='Test kitten', owner=user)
    response = client.delete(f'/api/kittens/{kitten.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
