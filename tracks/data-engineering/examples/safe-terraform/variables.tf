# =============================================================================
# Input Variables
# =============================================================================
# These variables allow you to customize the deployment without editing main.tf.
# Set values in terraform.tfvars (see terraform.tfvars.example).
# =============================================================================

variable "project_id" {
  description = "The GCP project ID to deploy resources into (required)."
  type        = string

  validation {
    condition     = length(var.project_id) > 0
    error_message = "project_id must not be empty. Set it in terraform.tfvars."
  }
}

variable "region" {
  description = "The GCP region for all resources."
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Environment label (e.g., dev, staging, prod). Used in resource names."
  type        = string
  default     = "dev"
}

variable "bucket_name_suffix" {
  description = "Suffix appended to the GCS bucket name (after project ID and environment)."
  type        = string
  default     = "raw-data"
}

variable "dataset_id" {
  description = "The BigQuery dataset ID."
  type        = string
  default     = "pipeline_data"
}
