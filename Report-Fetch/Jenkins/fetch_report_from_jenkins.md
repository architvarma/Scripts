# Fetching Reports from Jenkins

## Overview
This document explains how to use different URLs to fetch reports from Jenkins. The reports include information about builds, such as build number, display name, result, timestamp, and duration.

## URL 1: Fetching Build Information
You can use the following URL to fetch build information for a job named from Jenkins:

```
http://jenkins_url/job/JOB_NAME/api/json?tree=builds[number,displayName,result,timestamp,duration]
```

Replace the value "jenkins_url","JOB_NAME" with the actual value
This URL fetches a JSON response containing build details, including the build number, display name, result, timestamp, and duration.

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
