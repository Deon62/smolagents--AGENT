import os
import base64

LANGFUSE_PUBLIC_KEY="pk-lf-d10f899a-c4cc-43d4-b358-c8e6130c2794"
LANGFUSE_SECRET_KEY="sk-lf-13ac0b14-8ad1-4343-801c-9bc113618b20"
LANGFUSE_AUTH=base64.b64encode(f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}".encode()).decode()

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://cloud.langfuse.com/api/public/otel" # EU data region
# os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://us.cloud.langfuse.com/api/public/otel" # US data region
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"