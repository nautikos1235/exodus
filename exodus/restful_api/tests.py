# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase
from rest_framework import status
from django.conf.urls import url, include
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from trackers.models import Tracker
import datetime


class TrackersApiTests(APITestCase):
    urlpatterns = [url('api/', include('restful_api.urls'))]

    def test_GET_returns_200(self):
        response = self.client.get('/api/trackers')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_returns_saved_tracker(self):
        tracker_1 = Tracker(name='tracker_1')
        tracker_1.save()
        response = self.client.get('/api/trackers')
        now = datetime.datetime.now()
        expected_response = {'trackers': {
            '1': {
                'code_signature': '',
                'creation_date': now.strftime("%Y-%m-%d"),
                'description': '',
                'id': 1,
                'name': tracker_1.name,
                'network_signature': '',
                'website': ''}}
            }
        self.assertEqual(response.json(), expected_response)

    def test_PUT_returns_unauthenticated(self):
        response = self.client.put('/api/trackers/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_PUT_answers_not_found(self):
        admin = User(username='admin', is_superuser=True, is_staff=True)
        admin.save()
        tracker_1 = Tracker(name='tracker_1')
        tracker_1.save()
        token, created = Token.objects.get_or_create(user=admin)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.key)
        response = self.client.put('/api/trackers/1', {'code_signature': 'my.signature'})
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_PUT_updates_model(self):
    #     # TODO
