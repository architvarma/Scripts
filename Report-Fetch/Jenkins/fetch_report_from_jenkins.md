# Fetching Reports from Jenkins

## Overview
This document explains how to use different URLs to fetch reports from Jenkins. The reports include information about builds, such as build number, display name, result, timestamp, and duration.

## URL 1: Fetching Build Information
You can use the following URL to fetch build information for a job named from Jenkins:

```
http://jenkins_url/job/JOB_NAME/api/json?tree=builds[number,displayName,result,timestamp,duration]
```

Replace the value "jenkins_url","JOB_NAME" with the actual value
This URL fetches a JSON response containing build details, including the build number, display name, result, timestamp, and duration as shown below.

```
{
    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
    "builds": [
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
            "displayName": "testsecond#1.0.7-SNAPSHOT-21",
            "duration": 28750,
            "number": 773,
            "result": "SUCCESS",
            "timestamp": 1707813909983
        },
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
            "displayName": "testsecond#1.0.7-SNAPSHOT-21",
            "duration": 32799,
            "number": 772,
            "result": "FAILURE",
            "timestamp": 1707813814665
        }
    ]
}

```
#### JSON Output Explanation

The JSON output provides information about the builds of a Jenkins workflow job. Here's an explanation of each key-value pair:

- `_class`: The class of the Jenkins job, indicating that it is a workflow job.
- `builds`: An array containing information about each build of the job. Each build is represented as an object with the following keys:
  - `_class`: The class of the Jenkins run, indicating that it is a workflow run.
  - `displayName`: The display name of the build, which typically includes the job name, version, and a unique identifier.
  - `duration`: The duration of the build in milliseconds.
  - `number`: The build number, which is a unique identifier for the build.
  - `result`: The result of the build, which can be "SUCCESS", "FAILURE", "UNSTABLE", etc.
  - `timestamp`: The timestamp of when the build started, represented as the number of milliseconds since the Unix epoch.

This output can be useful for tracking the status and duration of builds in your Jenkins workflow job.

## URL 2: Fetching Workflow Information
To fetch detailed workflow information for a specific build number of the job, you can use the following URL:

```
http://jenkins_url/job/JOB_NAME/BUILD_NUMBER/wfapi/describe
```

Replace "jenkins_url","JOB_NAME","BUILD_NUMBER" with the actual value you want to fetch information for. This URL provides a detailed JSON response describing the workflow of the specified build.

## Usage
You can use these URLs in your scripts or applications to fetch Jenkins build and workflow information programmatically. Ensure you have the necessary permissions to access Jenkins and the specific job information.

For more information about Jenkins API, refer to the [Jenkins API documentation](https://www.jenkins.io/doc/book/using/remote-access-api/).
```
