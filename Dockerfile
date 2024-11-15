FROM python:3.10-alpine

EXPOSE 8014/tcp

ARG PROJECT_DIR=/project
ENV PROJECT_DIR=/project
ENV PYTHONPATH=$PROJECT_DIR/src

WORKDIR $PROJECT_DIR

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup -h "$PROJECT_DIR"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; pip install --no-cache-dir -r requirements.txt

COPY /src $PROJECT_DIR/src
RUN chmod +x "$PROJECT_DIR/src/entrypoint.sh"; chown -R appuser:appgroup "$PROJECT_DIR"
USER appuser

ENTRYPOINT ["sh", "src/entrypoint.sh"]
