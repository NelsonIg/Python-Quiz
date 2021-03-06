# SOFTWARE ENGINEERING CLASS 2020
# Python-Quiz
## Checklist
### 1. UML  
1. [Use Case Diagram](checklist/UML/usecase.png)
2. [Package Diagram](checklist/UML/package.png)
3. [Class Diagram](checklist/UML/class.png)  
### 2. DDD  
[DDD](checklist/DDD/DDD.png)  
Four Domains: **Game Flow Management**, **User Management**, **In-App PayManagement**, **Security Management**   
When the user opens the application, he must enter his login information which will grand access to the game itself and possible In-app payments. Therefour, a **customer/supplier** relationship is to be set up. Regarding the **Security Management**, the implementation of this domain shall not be visible to other domains. Here an **Anticorruption Layer** is defined.
### 3. Metrics
[Lines of Code/ Commented Lines](checklist/Metrics/lines_code_comments.JPG)  
[Classes/ Functions](checklist/Metrics/classes_functions.jpg)
### 4. CCD  
[Cheat Sheet](checklist/CCD/CCD_cheatsheet.pdf)  
* [Function](https://github.com/nelson-bht/Python-Quiz/blob/a00056d6df7eba49effaaa34c9b227612e51c13a/build_manag/src/main/python/game_data.py#L10-L15)  
Create small function with descriptive name, without side effects.  
* [Naming](https://github.com/nelson-bht/Python-Quiz/blob/a00056d6df7eba49effaaa34c9b227612e51c13a/build_manag/src/main/python/game_gui.py#L7-L23)  
Naming of classes and functions according to convention: Classes --> CamalCase, Functions --> lower_case.  
* [Comments](https://github.com/nelson-bht/Python-Quiz/blob/a00056d6df7eba49effaaa34c9b227612e51c13a/build_manag/src/main/python/game_data.py#L10-L15)  
Explaning functions and possible consequences.
* [Lines](https://github.com/nelson-bht/Python-Quiz/blob/ae51755588bb356569f1d3f049adc9b545e9d134/build_manag/src/main/python/game_gui.py#L1-L85)  
Keeping lines short.
### 5/6. Build & Unit-Tests
For this build **pyBuilder** is used, which executes a Unittest for [game_data.py](https://github.com/nelson-bht/Python-Quiz/blob/main/checklist/build_manag/src/main/python/game_data.py).
* [Unittests to be called](https://github.com/nelson-bht/Python-Quiz/blob/main/checklist/build_manag/src/unittest/python/game_data_tests.py)  
* [Run Build](https://github.com/nelson-bht/Python-Quiz/blob/main/checklist/build_manag/build_run.JPG)
### 7. CD
1. [Pipeline](https://github.com/nelson-bht/Python-Quiz/blob/main/.github/workflows/test.yml)
### 8. IDE  
Spider IDE is used, which comes with Anaconda. Shortcuts:
* Strg+1: Toggle Commented Lines
* Strg+4: Insert block comment with describtion header
* Strg+Enter: Run Code
### 9 DSL  
[Class Question as DSL](https://github.com/nelson-bht/Python-Quiz/blob/b50cd3e4397e78e0490b672486953ac8a36e1feb/checklist/DSL/question_dsl.py#L60-L63)  
Output:  
``Question:{text:7x7=?, answer:49}``
