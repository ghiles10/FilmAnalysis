import streamlit as st
from test_run_docker import affichage_info

# route --> /
def welcome():
    return "API Films"

def affichage_film(input_file): 

    """API Films 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: input_file
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    # apppel de la fonction
    info_film = affichage_info(str(input_file))
    return info_film 

def main():
    st.title("API FILM")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">FILM API </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

input_file = st.text_input("Titre","Type Here")

result=""

if st.button("Afficher les données"):
    result=affichage_film(input_file)
st.success('INFOS : {}'.format(result))
