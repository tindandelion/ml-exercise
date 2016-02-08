# Implementation notes

- Programming language is fixed for me (Python) because the model comes from the
  data scientist in Python's pickle bimary format. 
  
- The common way to implement services nowadays is Web service with a REST API. 

- ``Flask`` microframework is chosen to implement the Web service; 

- The Web service is provided as a Docker image. That allows to deploy the
  application easily in test environments, as well as popular production cloud
  providers (Amazon Web Services, Google Compute Cloud, DigitalOcean). The image
  is available at Docker Hub (http://hub.docker.com) in the repository ``sergeymo/iris``.
  
- All logging is directed to the STDERR stream inside the container. Docker by
  default stores all standard output in a file, but also allows to use
  centarized logging services (syslog, Splunk, etc), which may be used in
  production to store logs from multiple service instances.
  
- The service can be easily scaled by placing it behind a load
  balancer. Production cloud platforms support automatic scaling of Docker
  applications.
  
- The incoming sample data, predicted label and processing time are logged in
  JSON format under ``iris.prediction`` tag. In combination with centralized log
  aggregators (mentioned above) that enables saving the samples and prediction
  results for further analysis and visualization. Other options for recording
  may be considered once the production deployment platform is selected.
  
- At the moment, the model itself is packaged into the Docker image. When new
  model is provided, the image may be re-deployed. Again, other options to
  provide model may be considered after the production platform is selected. At
  the moment, to distinguish model versions, the model's creation timestamp is
  logged along with the sample and predicted label. 
  
# Sample API usage

Service url: ``/iris/v1/predict``

Sample request JSON: ``{ "sample": [1.0, 1.1, 1, 1] }``

Sample output: ``{ "label": 1 }``

The service validates the incoming requests. In case of incorrect input data,
server responds with HTTP BAD_REQUEST(400) error. 

Sample error output: ``{ "message": "Sample must be an array of 4 numbers" }``

# Model performance evaluation

The Python script ``src/model_report.py`` prints the performance report for the
currently used model. The confusion matrix for provided sample file
(``example.json``) is visualized and saved into ``confusion_matrix.png``. 

# Project burndown

## Iteration 0: Project skeleton

- DONE Create an application skeleton
- DONE Create deployment package with skeleton
- DONE Take model into use

## Iteration 1: Refined API

- DONE Proper incoming request validation
- DONE Calculation error handling

## Iteration 2: Deployment
- DONE Deployment: Use production web-server 
- DONE Logging: what to use?
- DONE Observe production deployment options
- DONE Scalability 

## Iteration 3: Further improvements
- DONE Store samples and predictions for further analysis
- DONE Model file timestamp is stored with results 

## Iteration 4: Model metrics
- DONE What metrics are reasonable? 
- DONE Create test case for metrics validation
  
## Project backlog
- Iris dataset
- Metrics from production: what do we need?

## Future improvements
- Build automation
- Smoke test for created container



