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
### 5. Build
1. [Build Folder](https://github.com/nelson-bht/Python-Quiz/tree/main/build_manag)
### 7. CD
1. [Actions](https://github.com/nelson-bht/Python-Quiz/actions)
