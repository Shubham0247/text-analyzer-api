# Use official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.14

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies inside Lambda task root
RUN pip install -r requirements.txt

# Copy application code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set Lambda handler
CMD ["lambda_function.lambda_handler"]