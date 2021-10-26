
# For more information, please refer to https://aka.ms/vscode-docker-python
# Miniconda with Python version 3.8
FROM continuumio/miniconda3:4.8.3

COPY requirements.txt .

# install basic requirements
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["sh", "-c", "chmod +x run.sh && ./run.sh"]
