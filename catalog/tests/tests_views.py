from django.test import TestCase, RequestFactory
from catalog import views
from django.utils import timezone


# Added mixin to verify whether a view is callable or not
class view_request_factory_test_mixin(object):
    """Mixin with shortcuts for view tests."""
    longMessage = True  # More verbose messages
    view_class = None
    def get_response(self, method):
        factory = RequestFactory()
        req = getattr(factory, method)('/')
        return self.view_class.as_view()(req, *[], **{})
    def is_callable(self):
        resp = self.get_response('get')
        self.assertEqual(resp.status_code, 200)

class get_test_list(view_request_factory_test_mixin, TestCase):
    view_class = views.get_test_list
    
    def test_get(self):
        expected_value = True
        self.assertEqual(expected_value, callable(self.view_class))
    
    def test_get_all_clients_list(self):
        response = self.client.get('http://127.0.0.1:8000/get_test_list/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_client_list(self):
        response = self.client.get('http://127.0.0.1:8000/get_test_list/?client="CIBC"')
        self.assertEqual(response.status_code, 200)

    def test_get_technology_list(self):
        response = self.client.get('http://127.0.0.1:8000/get_test_list/?client="CIBC"&technology="genesys"')
        self.assertEqual(response.status_code, 200)
    
    def test_get_workflow_list(self):
        response = self.client.get('http://127.0.0.1:8000/get_test_list/?client="CIBC"&technology="genesys"&workflow="WORKF 1"')
        self.assertEqual(response.status_code, 200)

class get_test_by_id(TestCase):
   
    view_class = views.get_test_by_id
    def test_get(self):
        expected_value = True
        self.assertEqual(expected_value, callable(self.view_class))

    def test_get_by_id(self):
        response = self.client.get('http://127.0.0.1:8000/get_test_by_id/?testid=117')
        self.assertEqual(response.status_code, 200)

class get_client_state_counts(TestCase):
    
    view_class = views.get_client_state_counts
    def test_get(self):
        expected_value = True
        self.assertEqual(expected_value, callable(self.view_class))

    def test_get_client_success(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?client="CIBC"&state="Success"')
        self.assertEqual(response.status_code, 200)

    def test_get_client_failed(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?client="CIBC"&state="Failed"')
        self.assertEqual(response.status_code, 200)

    def test_get_client_warning(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?client="CIBC"&state="Warning"')
        self.assertEqual(response.status_code, 200)


class get_technology_state_counts(TestCase):
    
    view_class = views.get_technology_state_counts
    def test_get(self):
        expected_value = True
        self.assertEqual(expected_value, callable(self.view_class))

    def test_get_technology_success(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?technology="Genesys"&state="Success"')
        self.assertEqual(response.status_code, 200)

    def test_get_technology_failed(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?technology="Genesys"&state="Failed"')
        self.assertEqual(response.status_code, 200)

    def test_get_technology_warning(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?technology="Genesys"&state="Warning"')
        self.assertEqual(response.status_code, 200)


class get_workflow_state_counts(TestCase):
    
    view_class = views.get_workflow_state_counts
    def test_get(self):
        expected_value = True
        self.assertEqual(expected_value, callable(self.view_class))

    def test_get_workflow_success(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?workflow="WORKF 1"&state="Success"')
        self.assertEqual(response.status_code, 200)

    def test_get_workflow_failed(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?workflow="WORKF 1"&state="Failed"')
        self.assertEqual(response.status_code, 200)

    def test_get_workflow_warning(self):
        response = self.client.get('http://127.0.0.1:8000/get_client_state_counts/?workflow="WORKF 1"&state="Warning"')
        self.assertEqual(response.status_code, 200)
