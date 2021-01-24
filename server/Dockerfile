FROM tensorflow/tensorflow:2.1.0-py3

# Copy requirements file
COPY requirements.txt requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt
RUN pip install gunicorn

# Copy files
COPY ./ ./

# Run server
CMD ["python", "app.py"]
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
