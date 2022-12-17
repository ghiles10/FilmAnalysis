#!/bin/bash

# lancement 
sudo docker run --network=host -p 8501:8501 projet-linux:1.0 chromium http://localhost:8501
