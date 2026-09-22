import pytest
import requests

base_url = 'https://reqres.in/api/collections/todos/records'

project_id= {

   'project_id' : 26590

}

header_auth = {
    
    'x-api-key': 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56'
    
}

# создаём запись 
@pytest.mark.smoke
@pytest.mark.regression
def test_put_post():
    
    new_post = {
    # почему используется data
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
    
    assert response_create_info['data']['title'] == "API Testing"
 

    
@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_products():
    
# получаем список всех существующих записей , принадлежащих проекту 26590
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
  
# получаем конкретный элемент 

@pytest.mark.regression
def test_one_product():
    
    
    info = requests.get(
    
    base_url + '/780d2caf-d50d-4305-a1b3-749a2f35ffac',
    headers = {'x-api-key': 'pro_4299c0733dac257311a8c9e1412f1f7905abdf538d224b661be17fe08d740f56'},
    params=project_id
    
    
)
    assert info.status_code ==200

@pytest.mark.regression
def test_put():
    
    new_data = {
        
        
    "title":"Testing",
    "body":"Homework task",
    "author": "Student"
        
        
    }
        
    response_create  = requests.put(
        
        
        f"{base_url}/18a460ff-5570-47df-9bcb-c16211b23cdc",        # какой id и где его брать для изменения 
        headers=header_auth,         
        params=project_id,           
        json=new_data
        
        
    )
    
    json_data = response_create.json()
  
    
    assert response_create.status_code == 200
    assert json_data['title'] == 'Testing'
    
    

# 