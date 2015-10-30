# -*- coding: UTF-8 -*-
import pytest

from yelp.errors import BusinessUnavailable
from yelp.errors import MissingParameter
from yelp.obj.business_response import BusinessResponse
from yelp.tests.integration.integration_test import IntegrationTest


class TestBusinessIntegration(IntegrationTest):

    int_vcr = IntegrationTest.int_vcr
    cassette_params = IntegrationTest.cassette_params

    @int_vcr.use_cassette(**cassette_params)
    def test_url_with_no_params(self):
        with pytest.raises(MissingParameter):
            self.client.get_business('')

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_returns_correct_result(self):
        id = "yelp-san-francisco"
        resp = self.client.get_business(id)
        assert type(resp) is BusinessResponse
        assert resp.business.id == id

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_with_bad_id(self):
        with pytest.raises(BusinessUnavailable):
            id = "does-not-exist"
            self.client.get_business(id)

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_with_unicode_chars(self):
        id = u'weingalerie-und-café-nö-berlin'
        resp = self.client.get_business(id)
        assert resp.business.id == id
