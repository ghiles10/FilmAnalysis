import sys
sys.path.append("./src")
import os

def test_file_txt() : 
    
    # assert if the file in not empty 
    assert os.path.getsize(r'src/data/data_film.txt') > 0 