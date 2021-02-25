# Cloud Service Status

Aggregate several cloud service provider status pages into one view

Built on Python with Flask

Currently this is designed to host on Google App Engine, with automated builds on commit to master.

Set project secrets:
  - PROJECT_NAME: Google Cloud project ID number
  - SERVICE_ACCOUNT: JSON credentials with access to Cloud Build and App Engine
