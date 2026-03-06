# Safe Terraform Template for GCP

This template deploys **only free-tier GCP resources**, designed specifically for learn-ai capstone projects. You can use it with confidence knowing it will not incur unexpected charges.

## What It Creates

| Resource | Description |
|----------|-------------|
| **GCS Bucket** | A Google Cloud Storage bucket (Standard class, `us-central1`) with a 90-day lifecycle deletion policy and versioning enabled. |
| **BigQuery Dataset** | A BigQuery dataset (`us-central1`) with a 90-day default table expiration. |
| **Service Account** | A dedicated service account for pipeline use, granted only the minimum roles needed. |
| **IAM Bindings** | The service account receives exactly two roles: `roles/bigquery.dataEditor` and `roles/storage.objectAdmin`. Nothing more. |

## Estimated Cost

**$0/month** for typical capstone usage. All resources fall within GCP's free tier or always-free quotas. BigQuery provides 1 TB of querying and 10 GB of storage free per month. GCS Standard storage in a single region has minimal cost, and the volumes used in a capstone project are negligible.

## How to Use

1. **Copy this directory** into your own project repository:

   ```bash
   cp -r examples/safe-terraform/ ~/my-capstone/terraform/
   cd ~/my-capstone/terraform/
   ```

2. **Edit `terraform.tfvars`** with your GCP project ID:

   ```bash
   cp terraform.tfvars.example terraform.tfvars
   # Open terraform.tfvars and replace "your-gcp-project-id" with your actual project ID
   ```

3. **Initialize Terraform:**

   ```bash
   terraform init
   ```

4. **Preview what will be created:**

   ```bash
   terraform plan
   ```

   Review the output carefully. You should see exactly 4 resources to be created (bucket, dataset, service account, and IAM bindings).

5. **Apply the configuration:**

   ```bash
   terraform apply
   ```

   Type `yes` when prompted.

## Tearing Down

When you are done with your capstone, clean up all resources:

```bash
terraform destroy
```

This removes everything that was created, ensuring no ongoing costs.
