## docker_tests
# Inicial
Passo inicial
=================
<!--ts-->
   * [pyenv local 3.11.1](#pyenv)
   * [poetry initi](#petry-init)
   * [poetry env use 3.11.1](#poetry-env-use-3.11.1)
   * [petry shell](#petry-shell)

   * [github](#github)
      * [git add .](#git-add)
      * [git commit -m "{comentario}"](#git-commit)
      * [git push](#git-push)
<!--te-->
''' 
1 - pyenv local 3.11.1
2 - poetry init
3 - poetry env use 3.11.1
4 - poetry shell
5 - git add .
6 - git commit -m "initial config" 
7 - git push
'''
# app
'''
1 - poetry add streamlit
2 - poetry run streamlit run app.py
'''
# docker
'''
1 - criar o dockerfile
2 - docker build -t minha-first image .
3 - docker run -d -p 8501:8501 --name my-streamlit minha-first-image
'''