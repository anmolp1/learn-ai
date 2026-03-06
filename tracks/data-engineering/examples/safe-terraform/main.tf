# =============================================================================
# Safe Terraform Configuration for GCP
# =============================================================================
# This configuration creates ONLY free-tier resources suitable for a capstone
# project. It provisions a GCS bucket, a BigQuery dataset, and a service
# account with minimal IAM roles.
# =============================================================================

# -----------------------------------------------------------------------------
# Provider Configuration
# -----------------------------------------------------------------------------
# The google provider lets Terraform manage GCP resources. It uses the
# project ID and region defined in variables.tf.
# -----------------------------------------------------------------------------
provider "google" {
  project = var.project_id
  region  = var.region
}

# -----------------------------------------------------------------------------
# Google Cloud Storage Bucket
# -----------------------------------------------------------------------------
# This bucket stores raw data files for the pipeline. Key settings:
# - Standard storage class (cheapest for infrequent access patterns)
# - 90-day lifecycle rule automatically deletes old objects to avoid cost creep
# - Versioning enabled so accidental overwrites can be recovered
# - Uniform bucket-level access (simplifies permissions, no per-object ACLs)
# - Public access prevention enforced (data stays private)
# -----------------------------------------------------------------------------
resource "google_storage_bucket" "pipeline_bucket" {
  name     = "${var.project_id}-${var.environment}-${var.bucket_name_suffix}"
  location = var.region

  # Standard storage class -- no additional cost beyond base storage pricing
  storage_class = "STANDARD"

  # Automatically delete objects after 90 days to prevent cost accumulation
  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }

  # Enable versioning so you can recover from accidental overwrites or deletes
  versioning {
    enabled = true
  }

  # Use uniform bucket-level access instead of per-object ACLs.
  # This is simpler and recommended by Google.
  uniform_bucket_level_access = true

  # Prevent any public access to this bucket. Data stays private.
  public_access_prevention = "enforced"

  # Allow Terraform to destroy this bucket even if it contains objects.
  # This makes cleanup with `terraform destroy` straightforward.
  force_destroy = true
}

# -----------------------------------------------------------------------------
# BigQuery Dataset
# -----------------------------------------------------------------------------
# This dataset holds the tables created by the pipeline. Key settings:
# - Located in the same region as the bucket for data locality
# - 90-day default table expiration to auto-clean unused tables
# - BigQuery's free tier includes 1 TB queries and 10 GB storage per month
# -----------------------------------------------------------------------------
resource "google_bigquery_dataset" "pipeline_dataset" {
  dataset_id = var.dataset_id
  location   = var.region

  # Friendly name and description shown in the BigQuery console
  friendly_name = "Pipeline Data (${var.environment})"
  description   = "Dataset for the data engineering capstone pipeline."

  # Tables without an explicit expiration will be automatically deleted
  # after 90 days. This prevents forgotten tables from accumulating.
  default_table_expiration_ms = 7776000000 # 90 days in milliseconds
}

# -----------------------------------------------------------------------------
# Service Account
# -----------------------------------------------------------------------------
# A dedicated service account for the pipeline. Using a service account
# (instead of your personal account) follows the principle of least privilege
# and makes it easy to revoke access later.
# -----------------------------------------------------------------------------
resource "google_service_account" "pipeline_sa" {
  account_id   = "${var.environment}-pipeline-sa"
  display_name = "Pipeline Service Account (${var.environment})"
  description  = "Service account used by the data pipeline. Has minimal permissions."
}

# -----------------------------------------------------------------------------
# IAM Bindings -- Minimal Roles Only
# -----------------------------------------------------------------------------
# We grant the service account exactly two roles and nothing more:
#
# 1. roles/bigquery.dataEditor  -- read/write tables and views in BigQuery
# 2. roles/storage.objectAdmin  -- read/write/delete objects in GCS
#
# These are the minimum permissions needed for a pipeline that reads from
# GCS and writes to BigQuery. We deliberately do NOT grant broader roles
# like roles/editor or roles/owner.
# -----------------------------------------------------------------------------

# Allow the service account to read and write BigQuery tables
resource "google_project_iam_member" "bigquery_data_editor" {
  project = var.project_id
  role    = "roles/bigquery.dataEditor"
  member  = "serviceAccount:${google_service_account.pipeline_sa.email}"
}

# Allow the service account to manage objects in GCS buckets
resource "google_project_iam_member" "storage_object_admin" {
  project = var.project_id
  role    = "roles/storage.objectAdmin"
  member  = "serviceAccount:${google_service_account.pipeline_sa.email}"
}
