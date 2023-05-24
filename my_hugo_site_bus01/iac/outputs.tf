output "storage_account_name" {
  description = "The name of the storage account"
  value       = module.ht5.storage_account_name
}

output "storage_account_URL" {
  description = "URL for the static website"
  value       = module.ht5.storage_account_URL
}
