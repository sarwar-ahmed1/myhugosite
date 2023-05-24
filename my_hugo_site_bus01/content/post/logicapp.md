---
title: "Logic Apps"
date: 2023-04-04T09:28:12+01:00
draft: true
---

## Automating Cognitive Services with Logic Apps

This tutorial demonstrates how to automate Cognitive Services using Logic Apps in Azure.

### 1. Create a Logic App:

- Go to the Azure portal and click the "Create" button.
- Search for "Logic App" and select it.
- Fill in the following details:
  - Subscription: training_ce05
  - Resource group: rg_kubce05_000_cog
  - Logic app name: la-ce05\<cloud_id>-01
  - Plan type: Consumption
  - Region: North Europe
  - Enable log analytics, Log Analytics workspace: log-ce05-00
  - Tags: cohort, pod, user
- Press the "Go to resource" button.

### 2. Configure the Logic App:

- In the Logic App Designer, add a "Recurrence" trigger with default settings.
- Add a new step for "Azure Blob Storage" and choose the "List blobs (V2)" action.
  - Connection name: blob \<cloud_id>01
  - Authentication type: Access Key
  - Azure Storage account name or blob endpoint: sakubce05000\<cloud_id>
  - Folder: /upload
  - Add a new step for "Control" and choose the "For each" action.
- Select an output from previous steps: value

### 3. Upload files to Blob Storage:

- Go to the Azure portal, navigate to the storage account (sakubce05000\<cloud_id>).
- Select "Containers" and click on the "upload" container.
- Click the "Upload" button and either drag and drop files or browse for files to upload.

### 4. Configure additional actions in the Logic App:

- Add an action for "Create SAS URL by path (V2)".
  - Storage account name or blob endpoint: Use connection settings(sakubce05000\<cloud_id>)
  - Blob path: Path
- Add an action for "Computer Vision API" and choose the "Describe Image URL (V3) (Preview)" action.
  - Connection name: cv \<cloud_id>01
  - Account Key and Site URL: Retrieve from the Cognitive Services resource (caimagekubce05000\<cloud_id>), under "Keys and Endpoints".
  - Resource Subdomain or Region: Use connection setting(northeurope)
  - Image URL: Web Url

### 5. Test the Logic App:

- Click the "Run Trigger" button in the Logic App Designer.
- Expand the "Describe Image URL (V3)" action to view the outputs.
- Click "Next" to see different outputs for each image.
