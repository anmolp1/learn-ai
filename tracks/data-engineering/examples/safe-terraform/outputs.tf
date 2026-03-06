# =============================================================================
# Outputs
# =============================================================================
# These values are printed after `terraform apply` and can be referenced
# by other Terraform configurations or scripts.
# =============================================================================

output "bucket_name" {
  description = "The name of the GCS bucket created for pipeline data."
  value       = google_storage_bucket.pipeline_bucket.name
}

output "dataset_id" {
  description = "The BigQuery dataset ID."
  value       = google_bigquery_dataset.pipeline_dataset.dataset_id
}

output "service_account_email" {
  description = "The email address of the pipeline service account."
  value       = google_service_account.pipeline_sa.email
}
