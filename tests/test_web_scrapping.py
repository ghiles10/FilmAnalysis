import sys
sys.path.append("./src")
import os
import pytest
from flask import Flask, request
from test_flask import app

def test_file_txt() : 
    
    # assert if the file in not empty 
    assert os.path.getsize(r'src/data/data_film.txt') > 0 

def test_file_csv() :
    # assert base_nettoye.csv exists
    assert os.path.exists(r'src/data/base_nettoye.csv') == True 

# vérifier la réponse de l'application à une requête GET
def test_index_get():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Enter a title' in response.data


