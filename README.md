# Learn Django 

This Learn Django repository is created to keep track of my weekly learning summary.

---

<details>
  <summary> Week 1 - 26 Feb 23 : Getting Started with Django </summary>

- python --version = Check for python version 
- pip list = [pip is the standard package manager for python. It allows you to install and manage additional packages that are not part of the Python standard library](https://realpython.com/lessons/what-is-pip-overview/)
- [python -m venv venv](https://docs.python.org/3/tutorial/venv.html#:~:text=The%20module%20used%20to%20create,or%20whichever%20version%20you%20want.)
    - Python applications will often use packages and modules that don't come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library's interface. 
    - This means it may not be possible for one python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module, but applications B needs version 2.0, then the requirements are in conflict and installing either version 1.0 and version 2.0 will leave one application unable to run. The solution for this problem is to create a virtual environment, self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. 
    - Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library to be upgraded to version 3.0, this will not affect application A's environment. 
    - The module used to create and manage virtual environments is called venv. venv will usually install the most recent version of python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running python3 or whichever version you want. 

- venv_firstapp\Scripts\activate : You might come across with the following issues. 
    - Issue 1 : cannot be loaded because running scripts is disabled on this system.
    - For this run : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine` in powershell as admin
        - [This above script will allow local scripts to execute on the VM, irrespective of whether they are signed or not.](https://stackoverflow.com/questions/54776324/powershell-bug-execution-of-scripts-is-disabled-on-this-system) 
    - Issue 2: 'Set-ExecutionPolicy' is not recognized as an internal or external command,
        - [Set-ExecutionPolicy](https://stackoverflow.com/questions/58536140/set-executionpolicy-is-not-recognized-as-an-internal-or-external-command-oper) is a PowerShell Cmdlet. You should run it in a PowerShell(Admin) session, not in cmd. 

- pip install django 
- django-admin startproject djapp = [This will create a djapp directory in your current directory](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).
- 
</details>

---

<details>
  <summary> Week 2 - 5 March 23 :  </summary>

- how to ignore venv with subdirectories in git, https://stackoverflow.com/questions/42306410/gitignore-syntax-how-to-exclude-virtualenv-sub-directories#:~:text=gitignore%20folder%20just%20add%20the,a%20slash%20at%20the%20end.&text=This%20will%20ignore%20all%20sub%20directories%20in%20the%20venv%20folder.

- call manage.py `python manage.py specifyTask`
    - python manage.py startapp AppFeatures1
- asynchronous gateway asgi,wsgi.py - used for production purposes 
- settings.py
- urls.py
- Design pattern - MVT pattern , [MVT Django](https://cupofcode.blog/wp-content/uploads/2021/04/cupofcode_blog_django_MVT_diagram.png)
    - Model - DB
        - for each model, you need to migrate. Add add
    - View - business logic
    - Template - HTML
- Djando fieldstypes.html
- Write a Student class in models.py, add the djapp in burls.
    - python manage.py makemigrations 
    - python manage.py runserver 
        - `http://127.0.0.1:8000/admin/login/?next=/admin/` or localhost:8000

</details>