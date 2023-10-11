# Improvability Score

Faced with the drop in educational levels observed following the closure of schools, the “Ministério da Educação” (Portuguese Ministry of Education) is contacting you, with the idea of using data and AI to try to remedy the situation.

The Ministry would like the educational advisors of each establishment to have a tool allowing them to prioritize the students to be supported. To do this, they are imagining a dashboard that would make it possible to prioritize the students to be supported based on the complexity and value of such support.

## Project Hierarchy

- `Imprvability_Score/`
  - `.github/`
    - `workflow/`
        - `main.yaml`
  - `code/`
    - `src/`
        - `data.py`
        - `model.py`
        - `improvability.py`
    - `utils/`
        - `data_preprocessing.py`
        - `get_files.py`
        - `vis.py`
  - `test/`
    - `test_code.py`
  - `main.py`
  - `Dockerfile`
  - `ReadMe.md`
  - `requirements.txt`
    
## Usage

If using Docker:
    
```bash
    # Build the docker image:
    $docker build -t Improvability-app .

    # Run the Docker container:
    $docker run -p 8501:8501 Improvability-app
```
Else:
```bash
    # Install virtualenv (if not already installed):
    $pip install virtualenv

    # Create a Virtual Environment:
    $virtualenv venv # You can change venv with the desired name of the virtual env

    # Activating a Virtual Environment:
    $venv\Scripts\activate

    # Install requirements and dependencies
    $pip install -r requirements.txt

    # Run the Script:
    $ streamlit run main.py

    # At the end, Do not forget to exit the venv
    $deactivate
```
    