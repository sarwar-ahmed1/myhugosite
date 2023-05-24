terraform {
  backend "azurerm" {

  }
}

locals {
  target_resource_group = format("rg-%s-%s-%s-%s-%03d", var.purpose, var.env, var.cohort, var.user, var.instance)

}

resource "azurerm_resource_group" "storage_rg" {
  name     = local.target_resource_group
  location = var.location
  tags = {
    cohort      = var.cohort
    pod         = var.pod_tag
    user        = var.user
    environment = var.env
    purpose     = var.purpose
  }
}

module "ht5" {
  source   = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce05/_git/terraform_storage_accounts_hea"
  env      = var.env
  cohort   = var.cohort
  rg       = azurerm_resource_group.storage_rg.name
  instance = var.instance
  user     = var.user
  pod_tag  = var.pod_tag
  depends_on = [
    azurerm_resource_group.storage_rg
  ]
}
