# Django Commands

1. 폴더 생성

   ```bash
   mkdir [프로젝트 이름]
   cd [프로젝트 이름]
   ```

2. 가상환경 설정

   - 가상환경 생성

     ```bash
     pyenv virtualenv 3.6.7 [가상환경 이름]
     ```

   - 가상환경 삭제

     ```bash
     pyenv uninstall [가상환경 이름]
     ```

   - 가상환경 목록

     ```bash
     pyenv versions
     ```

   - 현재 폴더에 가상 환경 활성화

     ```bash
     pyenv local [가상환경 이름]
     ```

   - 현재 폴더에 활성화된 가상 환경 비활성화

     - `.python-version` 파일을 찾아 삭제한다.

2. django 프로젝트

   - django 설치

     ```bash
     pip install django
     ```

   - startproject

     ```bash
     django-admin startproject [프로젝트 이름] .
     ```

   - startapp

     ```bash
     python manage.py startapp [앱 이름]
     ```





