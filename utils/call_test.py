import subprocess

# Define the spark-submit command
spark_submit_cmd = [
    "spark-submit",
    "--master", "local",  # or "spark://<master>:<port>" for a remote Spark cluster
    "--deploy-mode", "client",  # or "cluster" for a remote Spark cluster
    "/opt/spark-apps/test.py"
]

# Execute the spark-submit command
subprocess.call(spark_submit_cmd)