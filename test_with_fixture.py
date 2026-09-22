import requests
import pytest 

base_url = 'https://reqres.in/api/collections/todos/records'

project_id= {

   'project_id' : 26590

}

header_auth = {
    
    'x-api-key': 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56'
    
}
@pytest.fixture
def create_post():

    response = requests.get(base_url, headers=header_auth, params=project_id)
    print(response.json()["data"][0])
    records = response.json()["data"][0]

    record_id = records['id']
    yield record_id

    
@pytest.mark.smoke
@pytest.mark.regression        
def test_put_post():
    
    new_post = {
        
    "data": {
        
    "title":"API Testing",
    "body":"Homework task",
    "author": "Student"
} 
}
    response_create = requests.post(
    
    base_url,
    headers=header_auth,
    params=project_id,
    json=new_post   
)
    response_create_info = response_create.json()

    assert response_create.status_code == 201
    assert 'data' in response_create_info
    assert 'collection_id' in response_create_info['data']
    assert response_create_info['data']['data']['title'] == "API Testing"
    assert response_create_info['data']['data']['body'] == 'Homework task'
    assert response_create_info['data']['data']['author'] == 'Student'
    
@pytest.mark.smoke
@pytest.mark.regression    
def test_get_all_products():

    info = requests.get(

    base_url, 
    headers =header_auth,
    params=project_id
)
    product_data = info.json()
    
    assert info.status_code == 200
    assert 'data' in product_data
    assert 'meta' in product_data
    assert product_data['meta']['total'] > 0 
    
@pytest.mark.regression
def test_get_one_product(create_post):
    
    info = requests.get(
    
    f"{base_url}/{create_post}",
    headers = header_auth,
    params=project_id
    
    
)
    assert info.status_code ==200
  
@pytest.mark.regression
def test_put(create_post):
    
    new_data = {
        
    'data' : {    
              
    "title":"Testing",
    "body":"Homework task",
    "author": "Student"
}         
}
        
    response_create  = requests.put(
        
        f"{base_url}/{create_post}",   # какой id и где его брать для изменения 
        headers=header_auth,         
        params=project_id,           
        json=new_data
        
        
    )
    
    json_data = response_create.json()
  
    
    assert response_create.status_code == 200
    assert json_data["data"]["data"]['title'] == 'Testing'
    
@pytest.mark.regression  
def test_delete(create_post):

    response_create = requests.delete(
        
    base_url + '/' + str(create_post),
    headers = header_auth,
    params=project_id         


)
    print(response_create.status_code)


# фикстура возвращает id созданного товара 