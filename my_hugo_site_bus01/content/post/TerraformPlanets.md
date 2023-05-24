---
title: "Terraform Planets"
date: 2023-04-04T09:28:12+01:00
draft: true
---

This code is a Terraform configuration for creating Azure storage accounts and storage containers. It uses local values, data sources, and resources to create and manage these resources in a specified resource group.

```hcl
locals {
  target_resource_group = "rg-kubdevce0501planet"
  default_tags = tomap({
    "cohort"      = var.cohortid
    "cloud"       = "azure"
    "user"        = var.user
    "environment" = var.environment
    "podID"       = var.podID
  })
}
```

1. **Local values**: Define local variables to be used in the configuration.
   - `target_resource_group`: The name of the target resource group.
   - `default_tags`: A map containing default tags to be assigned to resources.

```hcl
data "azurerm_resource_group" "example" {
  name = local.target_resource_group
}
```

2. **Data source**: Retrieve information about the specified resource group.
   - `azurerm_resource_group`: Fetches data about the resource group with the name `local.target_resource_group`.

```hcl
resource "random_string" "random" {
  length  = var.string_length
  special = false
}
resource "azurerm_storage_account" "target" {
  resource_group_name      = data.azurerm_resource_group.example.name
  location                 = data.azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
  for_each                 = toset(values(var.storage_container_mapping))
  name                     = format("sto%s%s%s%s%s", var.cohortid, var.user, var.cloud, var.environment, each.key)
  tags                     = local.default_tags
}
resource "azurerm_storage_container" "target" {
  depends_on = [
    azurerm_storage_account.target
  ]
  for_each             = var.storage_container_mapping
  storage_account_name = azurerm_storage_account.target[each.value].name
  name                 = format("%s-%s", lower(each.key), lower(each.value))
}
```

3. **Resources**:
   - `random_string`: Generates a random string of a specified length without special characters.
   - `azurerm_storage_account`: Creates Azure storage accounts for each unique value in the `var.storage_container_mapping` variable. It sets the storage account properties such as account tier, replication type, and minimum TLS version. The storage account name is generated using the cohort ID, user, cloud, environment, and a key from the `for_each` loop.
   - `azurerm_storage_container`: Creates Azure storage containers based on the `var.storage_container_mapping` variable. It sets the storage account name using the created storage accounts and generates a storage container name using the keys and values from the `for_each` loop.

In summary, this Terraform configuration creates Azure storage accounts and storage containers based on a given mapping variable. It retrieves data about an existing resource group and applies default tags to the created resources.
